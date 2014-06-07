#!/usr/bin/env python
""" generated source for module VariableConstrainer """
# package: org.ggp.base.util.gdl.transforms
import java.util.List

import java.util.Map

import java.util.Set

import java.util.concurrent.atomic.AtomicBoolean

import org.ggp.base.util.concurrency.ConcurrencyUtils

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.GdlVisitor

import org.ggp.base.util.gdl.GdlVisitors

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.ImmutableSentenceFormModel

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SentenceFormModel

import org.ggp.base.util.gdl.model.SentenceFormModelFactory

import org.ggp.base.util.gdl.model.SimpleSentenceForm

import org.junit.Assert

import com.google.common.base.Function

import com.google.common.base.Optional

import com.google.common.base.Preconditions

import com.google.common.base.Predicate

import com.google.common.collect.ArrayListMultimap

import com.google.common.collect.Collections2

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableMap

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Iterables

import com.google.common.collect.ListMultimap

import com.google.common.collect.Lists

import com.google.common.collect.Maps

import com.google.common.collect.Multimaps

import com.google.common.collect.Sets

class VariableConstrainer(object):
    """ generated source for class VariableConstrainer """
    # 
    #      * Modifies a GDL description by replacing all rules in which variables could be bound to
    #      * functions, so that the new rules will only bind constants to variables. Also automatically
    #      * removes GdlOrs from the rules using the DeORer.
    #      *
    #      * Not guaranteed to work if the GDL is written strangely, such as when they include rules
    #      * in which certain conjuncts are never or always true. Not guaranteed to work when rules
    #      * are unsafe, i.e., they contain variables only appearing in the head, a negated literal,
    #      * and/or a distinct literal. (In fact, this can be a good way to test for GDL errors, which
    #      * often result in exceptions.)
    #      *
    #      * Not guaranteed to finish in a reasonable amount of time in pathological cases, where the
    #      * number of possible functional structures is prohibitively large.
    #      *
    #      * @param description A GDL game description.
    #      * @return A modified version of the same game.
    #      
    @classmethod
    def replaceFunctionValuedVariables(cls, description):
        """ generated source for method replaceFunctionValuedVariables """
        description = GdlCleaner.run(description)
        description = DeORer.run(description)
        model = SentenceFormModelFactory.create(description)
        #  Find "ambiguities" between sentence rules: "If we have sentence form X
        #  with variables in slots [...], it could be aliased to sentence form Y instead"
        ambiguitiesByOriginalForm = getAmbiguitiesByOriginalForm(model)
        if ambiguitiesByOriginalForm.isEmpty():
            return description
        expandedRules = applyAmbiguitiesToRules(description, ambiguitiesByOriginalForm, model)
        return cleanUpIrrelevantRules(expandedRules)

    # 
    #      * An ambiguity represents a particular relationship between two
    #      * sentence forms. It says that if sentence form "original" appears
    #      * in a rule and has GdlVariables in particular slots, it could be
    #      * equivalent to the sentence form "replacement" if functions are
    #      * assigned to its variables.
    #      *
    #      * The goal of this transformation is to make it possible for users
    #      * of the game description to treat it as if functions could not be
    #      * assigned to variables. This requires adding or modifying rules to
    #      * account for the extra cases.
    #      
    class Ambiguity(object):
        """ generated source for class Ambiguity """
        original = SentenceForm()
        replacementsByOriginalTupleIndex = ImmutableMap()
        replacement = SentenceForm()

        def __init__(self, original, replacementsByOriginalTupleIndex, replacement):
            """ generated source for method __init__ """
            Preconditions.checkNotNull(original)
            Preconditions.checkNotNull(replacementsByOriginalTupleIndex)
            Preconditions.checkArgument(not replacementsByOriginalTupleIndex.isEmpty())
            Preconditions.checkNotNull(replacement)
            for varIndex in replacementsByOriginalTupleIndex.keySet():
                Preconditions.checkElementIndex(varIndex, original.getTupleSize())
            self.original = original
            self.replacementsByOriginalTupleIndex = replacementsByOriginalTupleIndex
            self.replacement = replacement

        @classmethod
        def create(cls, original, replacementsByOriginalTupleIndex, replacement):
            """ generated source for method create """
            return cls.Ambiguity(original, ImmutableMap.copyOf(replacementsByOriginalTupleIndex), replacement)

        def getOriginal(self):
            """ generated source for method getOriginal """
            return self.original

        def getReplacement(self):
            """ generated source for method getReplacement """
            return self.replacement

        def __str__(self):
            """ generated source for method toString """
            return "Ambiguity [original=" + self.original + ", replacementsByOriginalTupleIndex=" + self.replacementsByOriginalTupleIndex + ", replacement=" + self.replacement + "]"

        # 
        #          * Returns true iff the given sentence could correspond to a
        #          * sentence of the replacement form, for some variable assignment.
        #          
        def applies(self, sentence):
            """ generated source for method applies """
            if not self.original.matches(sentence):
                return False
            tuple_ = GdlUtils.getTupleFromSentence(sentence)
            for varIndex in replacementsByOriginalTupleIndex.keySet():
                if not (isinstance(, (GdlVariable, ))):
                    return False
            return True

        def getReplacementAssignment(self, sentence, varGen):
            """ generated source for method getReplacementAssignment """
            Preconditions.checkArgument(self.applies(sentence))
            assignment = Maps.newHashMap()
            tuple_ = GdlUtils.getTupleFromSentence(sentence)
            for varIndex in replacementsByOriginalTupleIndex.keySet():
                assignment.put(tuple_.get(varIndex), replacementFunction)
            return assignment

    @classmethod
    def getAmbiguitiesByOriginalForm(cls, model):
        """ generated source for method getAmbiguitiesByOriginalForm """
        result = ArrayListMultimap.create()
        formsByName = getFormsByName(model)
        for name in formsByName.keySet():
            for form in forms:
                result.putAll(form, getAmbiguities(form, forms))
        allForms = ImmutableSet.copyOf(formsByName.values())
        for ambiguity in result.values():
            Assert.assertTrue(allForms.contains(ambiguity.getOriginal()))
            Assert.assertTrue(allForms.contains(ambiguity.getReplacement()))
        return result

    @classmethod
    def getFormsByName(cls, model):
        """ generated source for method getFormsByName """
        return Multimaps.index(getAllSentenceForms(model), Function())

    @classmethod
    def getAllSentenceForms(cls, model):
        """ generated source for method getAllSentenceForms """
        # The model may only have sentence forms for sentences that can actually be
        # true. It may be missing sentence forms that are used in the rules only,
        # with no actual corresponding sentences. We want to make sure these are
        # included.
        forms = Sets.newHashSet(model.getSentenceForms())
        GdlVisitors.visitAll(model.getDescription(), GdlVisitor())
        return forms

    @classmethod
    def getAmbiguities(cls, original, forms):
        """ generated source for method getAmbiguities """
        result = Lists.newArrayList()
        for form in forms:
            if form == original:
                continue 
            if ambiguity.isPresent():
                result.add(ambiguity.get())
        return result

    @classmethod
    @overloaded
    def findAmbiguity(cls, original, replacement):
        """ generated source for method findAmbiguity """
        Preconditions.checkArgument(original.__name__ == replacement.__name__)
        Preconditions.checkArgument(not original == replacement)
        ConcurrencyUtils.checkForInterruption()
        replacementsByOriginalTupleIndex = Maps.newHashMap()
        # Make the arguments ?v0, ?v1, ?v2, ... so we can find the tuple indices easily
        originalSentence = original.getSentenceFromTuple(getNumberedTuple(original.getTupleSize()))
        replacementSentence = replacement.getSentenceFromTuple(getNumberedTuple(replacement.getTupleSize()))
        success = cls.findAmbiguity(originalSentence.getBody(), replacementSentence.getBody(), replacementsByOriginalTupleIndex)
        if success:
            return Optional.of(cls.Ambiguity.create(original, replacementsByOriginalTupleIndex, replacement))
        else:
            return Optional.absent()

    @classmethod
    @findAmbiguity.register(object, List, List, Map)
    def findAmbiguity_0(cls, originalBody, replacementBody, replacementsByOriginalTupleIndex):
        """ generated source for method findAmbiguity_0 """
        if len(originalBody) != len(replacementBody):
            return False
        i = 0
        while i < len(originalBody):
            ConcurrencyUtils.checkForInterruption()
            if isinstance(replacementTerm, (GdlVariable, )):
                if not (isinstance(originalTerm, (GdlVariable, ))):
                    return False
            elif isinstance(replacementTerm, (GdlFunction, )):
                if isinstance(originalTerm, (GdlVariable, )):
                    replacementsByOriginalTupleIndex.put(varIndex, replacementTerm)
                elif isinstance(originalTerm, (GdlFunction, )):
                    if originalFunction.__name__ != replacementFunction.__name__:
                        return False
                    if not successSoFar:
                        return False
                else:
                    raise RuntimeException()
            else:
                raise RuntimeException()
            i += 1
        return True

    @classmethod
    def getNumberedTuple(cls, tupleSize):
        """ generated source for method getNumberedTuple """
        result = Lists.newArrayList()
        i = 0
        while i < tupleSize:
            result.add(GdlPool.getVariable("?v" + Integer.toString(i)))
            i += 1
        return result

    @classmethod
    def applyAmbiguitiesToRules(cls, description, ambiguitiesByOriginalForm, model):
        """ generated source for method applyAmbiguitiesToRules """
        result = ImmutableList.builder()
        for gdl in description:
            if isinstance(gdl, (GdlRule, )):
                result.addAll(applyAmbiguities(gdl, ambiguitiesByOriginalForm, model))
            else:
                result.add(gdl)
        return result.build()

    @classmethod
    def applyAmbiguities(cls, originalRule, ambiguitiesByOriginalForm, model):
        """ generated source for method applyAmbiguities """
        rules = Lists.newArrayList(originalRule)
        # Each literal can potentially multiply the number of rules we have, so
        # we apply each literal separately to the entire list of rules so far.
        for literal in Iterables.concat(ImmutableSet.of(originalRule.getHead()), originalRule.getBody()):
            for rule in rules:
                Preconditions.checkArgument(originalRule.arity() == rule.arity())
                newRules.addAll(applyAmbiguitiesForLiteral(literal, rule, ambiguitiesByOriginalForm, model))
            rules = newRules
        return rules

    @classmethod
    def applyAmbiguitiesForLiteral(cls, literal, rule, ambiguitiesByOriginalForm, model):
        """ generated source for method applyAmbiguitiesForLiteral """
        ConcurrencyUtils.checkForInterruption()
        results = Lists.newArrayList(rule)
        varGen = getVariableGenerator(rule)
        if isinstance(literal, (GdlSentence, )):
            for ambiguity in ambiguitiesByOriginalForm.get(form):
                ConcurrencyUtils.checkForInterruption()
                if ambiguity.applies(sentence):
                    results.add(newRule)
        elif isinstance(literal, (GdlNot, )):
            #  Do nothing. Variables must appear in a positive literal in the
            #  rule, and will be handled there.
        elif isinstance(literal, (GdlOr, )):
            raise RuntimeException("ORs should have been removed")
        elif isinstance(literal, (GdlDistinct, )):
            #  Do nothing
        return results

    class UnusedVariableGenerator(object):
        """ generated source for class UnusedVariableGenerator """
        def replaceVariablesAndConstants(self, function_):
            """ generated source for method replaceVariablesAndConstants """
            assignment = Maps.newHashMap()
            termsToReplace = Sets.newHashSet()
            GdlVisitors.visitAll(function_, GdlVisitor())
            for var in GdlUtils.getVariables(function_):
                assignment.put(var, getUnusedVariable())
            return CommonTransforms.replaceVariables(function_, assignment)

        def getUnusedVariable(self):
            """ generated source for method getUnusedVariable """

    @classmethod
    def getVariableGenerator(cls, rule):
        """ generated source for method getVariableGenerator """
        # Not thread-safe
        return cls.UnusedVariableGenerator()

    # 
    #      * Removes rules with sentences with empty domains. These simply won't have
    #      * sentence forms in the generated sentence model, so this is fairly easy.
    #      * @throws InterruptedException
    #      
    @classmethod
    def cleanUpIrrelevantRules(cls, expandedRules):
        """ generated source for method cleanUpIrrelevantRules """
        model = SentenceFormModelFactory.create(expandedRules)
        return ImmutableList.copyOf(Collections2.filter(expandedRules, Predicate()))

