#!/usr/bin/env python
""" generated source for module SentenceDomainModelOptimizer """
# package: org.ggp.base.util.gdl.model
import java.util.Iterator

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.concurrency.ConcurrencyUtils

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.GdlVisitor

import org.ggp.base.util.gdl.GdlVisitors

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.SentenceDomainModels.VarDomainOpts

import org.ggp.base.util.gdl.transforms.VariableConstrainer

import com.google.common.base.Function

import com.google.common.base.Preconditions

import com.google.common.base.Predicate

import com.google.common.collect.HashMultimap

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Iterables

import com.google.common.collect.Lists

import com.google.common.collect.Maps

import com.google.common.collect.SetMultimap

import com.google.common.collect.Sets

class SentenceDomainModelOptimizer(object):
    """ generated source for class SentenceDomainModelOptimizer """
    # 
    # 	 * Given a SentenceDomainModel, returns an ImmutableSentenceDomainModel
    # 	 * with Cartesian domains that tries to minimize the domains of sentence
    # 	 * forms without impacting the game rules. In particular, when sentences
    # 	 * are restricted to these domains, the answers to queries about terminal,
    # 	 * legal, goal, next, and init sentences will not change.
    # 	 *
    # 	 * Note that if a sentence form is not used in a meaningful way by the
    # 	 * game, it may end up with an empty domain.
    # 	 *
    # 	 * The description for the game must have had the {@link VariableConstrainer}
    # 	 * applied to it.
    # 	 
    @classmethod
    def restrictDomainsToUsefulValues(cls, oldModel):
        """ generated source for method restrictDomainsToUsefulValues """
        #  Start with everything from the current domain model.
        neededAndPossibleConstantsByForm = Maps.newHashMap()
        for form in oldModel.getSentenceForms():
            neededAndPossibleConstantsByForm.put(form, HashMultimap.create())
            addDomain(neededAndPossibleConstantsByForm.get(form), oldModel.getDomain(form), form)
        # 
        # 		 * To minimize the contents of the domains, we repeatedly go through two processes to reduce
        # 		 * the domain:
        # 		 *
        # 		 * 1) We remove unneeded constants from the domain. These are constants which (in their
        # 		 *    position) do not contribute to any sentences with a GDL keyword as its name; that
        # 		 *    is, it never matters whether a sentence with that constant in that position is
        # 		 *    true or false.
        # 		 * 2) We remove impossible constants from the domain. These are constants which cannot
        # 		 *    end up in their position via any rule or sentence in the game description, given
        # 		 *    the current domain.
        # 		 *
        # 		 * Constants removed because of one type of pass or the other may cause other constants
        # 		 * in other sentence forms to become unneeded or impossible, so we make multiple passes
        # 		 * until everything is stable.
        # 		 
        somethingChanged = True
        while somethingChanged:
            somethingChanged = removeUnneededConstants(neededAndPossibleConstantsByForm, oldModel)
            somethingChanged |= removeImpossibleConstants(neededAndPossibleConstantsByForm, oldModel)
        return toSentenceDomainModel(neededAndPossibleConstantsByForm, oldModel)

    @classmethod
    def addDomain(cls, setMultimap, domain, form):
        """ generated source for method addDomain """
        i = 0
        while i < form.getTupleSize():
            setMultimap.putAll(i, domain.getDomainForSlot(i))
            i += 1

    @classmethod
    def removeImpossibleConstants(cls, curDomains, model):
        """ generated source for method removeImpossibleConstants """
        newPossibleConstantsByForm = Maps.newHashMap()
        for form in curDomains.keySet():
            newPossibleConstantsByForm.put(form, HashMultimap.create())
        populateInitialPossibleConstants(newPossibleConstantsByForm, curDomains, model)
        somethingChanged = True
        while somethingChanged:
            somethingChanged = propagatePossibleConstants(newPossibleConstantsByForm, curDomains, model)
        return retainNewDomains(curDomains, newPossibleConstantsByForm)

    @classmethod
    def populateInitialPossibleConstants(cls, newPossibleConstantsByForm, curDomains, model):
        """ generated source for method populateInitialPossibleConstants """
        # Add anything in the head of a rule...
        for rule in getRules(model.getDescription()):
            addConstantsFromSentenceIfInOldDomain(newPossibleConstantsByForm, curDomains, model, head)
        # ... and any true sentences
        for form in model.getSentenceForms():
            for sentence in model.getSentencesListedAsTrue(form):
                addConstantsFromSentenceIfInOldDomain(newPossibleConstantsByForm, curDomains, model, sentence)

    @classmethod
    def propagatePossibleConstants(cls, newPossibleConstantsByForm, curDomain, model):
        """ generated source for method propagatePossibleConstants """
        # Injection: Go from the intersections of variable values in rules to the
        # values in their heads
        somethingChanged = False
        for rule in getRules(model.getDescription()):
            for varInHead in ImmutableSet.copyOf(GdlUtils.getVariables(rule.getHead())):
                domainsOfHeadVars.put(varInHead, domain)
                somethingChanged |= addPossibleValuesToSentence(domain, head, varInHead, newPossibleConstantsByForm, model)
        # Language-based injections
        somethingChanged |= applyLanguageBasedInjections(GdlPool.INIT, GdlPool.TRUE, newPossibleConstantsByForm)
        somethingChanged |= applyLanguageBasedInjections(GdlPool.NEXT, GdlPool.TRUE, newPossibleConstantsByForm)
        somethingChanged |= applyLanguageBasedInjections(GdlPool.LEGAL, GdlPool.DOES, newPossibleConstantsByForm)
        return somethingChanged

    @classmethod
    def applyLanguageBasedInjections(cls, curName, resultingName, newPossibleConstantsByForm):
        """ generated source for method applyLanguageBasedInjections """
        somethingChanged = False
        for form in newPossibleConstantsByForm.keySet():
            ConcurrencyUtils.checkForInterruption()
            if form.__name__ == curName:
                somethingChanged |= resultingFormDomain.putAll(curFormDomain)
        return somethingChanged

    @classmethod
    def getVarDomainInRuleBody(cls, varInHead, rule, newPossibleConstantsByForm, curDomain, model):
        """ generated source for method getVarDomainInRuleBody """
        try:
            for conjunct in getPositiveConjuncts(rule.getBody()):
                if GdlUtils.getVariables(conjunct).contains(varInHead):
                    domains.add(getVarDomainInSentence(varInHead, conjunct, newPossibleConstantsByForm, curDomain, model))
            return getIntersection(domains)
        except RuntimeException as e:
            raise RuntimeException("Error in rule " + rule + " for variable " + varInHead, e)

    @classmethod
    def getVarDomainInSentence(cls, var, conjunct, newPossibleConstantsByForm, curDomain, model):
        """ generated source for method getVarDomainInSentence """
        form = model.getSentenceForm(conjunct)
        tuple_ = GdlUtils.getTupleFromSentence(conjunct)
        domains = Lists.newArrayList()
        i = 0
        while i < len(tuple_):
            if tuple_.get(i) == var:
                domains.add(newPossibleConstantsByForm.get(form).get(i))
                domains.add(curDomain.get(form).get(i))
            i += 1
        return getIntersection(domains)

    @classmethod
    def getIntersection(cls, domains):
        """ generated source for method getIntersection """
        if domains.isEmpty():
            raise IllegalArgumentException("Unsafe rule has no positive conjuncts")
        intersection = Sets.newHashSet(domains.get(0))
        i = 1
        while i < len(domains):
            intersection.retainAll(curDomain)
            i += 1
        return intersection

    @classmethod
    def removeUnneededConstants(cls, curDomains, model):
        """ generated source for method removeUnneededConstants """
        newNeededConstantsByForm = Maps.newHashMap()
        for form in curDomains.keySet():
            newNeededConstantsByForm.put(form, HashMultimap.create())
        populateInitialNeededConstants(newNeededConstantsByForm, curDomains, model)
        somethingChanged = True
        while somethingChanged:
            somethingChanged = propagateNeededConstants(newNeededConstantsByForm, curDomains, model)
        return retainNewDomains(curDomains, newNeededConstantsByForm)

    @classmethod
    def retainNewDomains(cls, curDomains, newDomains):
        """ generated source for method retainNewDomains """
        somethingChanged = False
        for form in curDomains.keySet():
            somethingChanged |= curDomains.get(form).entries().retainAll(newDomain.entries())
        return somethingChanged

    @classmethod
    def propagateNeededConstants(cls, neededConstantsByForm, curDomains, model):
        """ generated source for method propagateNeededConstants """
        somethingChanged = False
        somethingChanged |= applyRuleHeadPropagation(neededConstantsByForm, curDomains, model)
        somethingChanged |= applyRuleBodyOnlyPropagation(neededConstantsByForm, curDomains, model)
        return somethingChanged

    @classmethod
    def applyRuleBodyOnlyPropagation(cls, neededConstantsByForm, curDomains, model):
        """ generated source for method applyRuleBodyOnlyPropagation """
        somethingChanged = False
        for rule in getRules(model.getDescription()):
            for var in ImmutableSet.copyOf(GdlUtils.getVariables(rule)):
                if not varsInHead.contains(var):
                    if neededConstants == None:
                        raise IllegalStateException("var is " + var + ";\nvarDomains key set is " + varDomains.keySet() + ";\nvarsInHead is " + varsInHead + ";\nrule is " + rule)
                    for conjunct in rule.getBody():
                        somethingChanged |= addPossibleValuesToConjunct(neededConstants, conjunct, var, neededConstantsByForm, model)
        return somethingChanged

    @classmethod
    def getVarDomains(cls, rule, curDomains, model):
        """ generated source for method getVarDomains """
        return SentenceDomainModels.getVarDomains(rule, AbstractSentenceDomainModel(model), VarDomainOpts.INCLUDE_HEAD)

    @classmethod
    def applyRuleHeadPropagation(cls, neededConstantsByForm, curDomains, model):
        """ generated source for method applyRuleHeadPropagation """
        somethingChanged = False
        for rule in getRules(model.getDescription()):
            while i < len(headTuple):
                ConcurrencyUtils.checkForInterruption()
                if isinstance(, (GdlVariable, )):
                    neededAndPossibleConstants.retainAll(varDomains.get(curVar))
                    for conjunct in rule.getBody():
                        somethingChanged |= addPossibleValuesToConjunct(neededAndPossibleConstants, conjunct, curVar, neededConstantsByForm, model)
                i += 1
        return somethingChanged

    @classmethod
    def addPossibleValuesToConjunct(cls, neededAndPossibleConstants, conjunct, curVar, neededConstantsByForm, model):
        """ generated source for method addPossibleValuesToConjunct """
        if isinstance(conjunct, (GdlSentence, )):
            return addPossibleValuesToSentence(neededAndPossibleConstants, conjunct, curVar, neededConstantsByForm, model)
        elif isinstance(conjunct, (GdlNot, )):
            return addPossibleValuesToSentence(neededAndPossibleConstants, innerSentence, curVar, neededConstantsByForm, model)
        elif isinstance(conjunct, (GdlOr, )):
            raise IllegalArgumentException("The SentenceDomainModelOptimizer is not designed for game descriptions with OR. Use the DeORer.")
        elif isinstance(conjunct, (GdlDistinct, )):
            return False
        else:
            raise IllegalArgumentException("Unexpected literal type " + conjunct.__class__ + " for literal " + conjunct)

    @classmethod
    def addPossibleValuesToSentence(cls, neededAndPossibleConstants, sentence, curVar, neededConstantsByForm, model):
        """ generated source for method addPossibleValuesToSentence """
        ConcurrencyUtils.checkForInterruption()
        somethingChanged = False
        form = model.getSentenceForm(sentence)
        tuple_ = GdlUtils.getTupleFromSentence(sentence)
        Preconditions.checkArgument(form.getTupleSize() == len(tuple_))
        i = 0
        while i < len(tuple_):
            if tuple_.get(i) == curVar:
                Preconditions.checkNotNull(neededConstantsByForm.get(form))
                Preconditions.checkNotNull(neededAndPossibleConstants)
                somethingChanged |= neededConstantsByForm.get(form).putAll(i, neededAndPossibleConstants)
            i += 1
        return somethingChanged

    @classmethod
    def getPositiveConjuncts(cls, body):
        """ generated source for method getPositiveConjuncts """
        return Iterables.transform(Iterables.filter(body, Predicate()), Function())

    @classmethod
    def getAllSentencesInBody(cls, body):
        """ generated source for method getAllSentencesInBody """
        sentences = Lists.newArrayList()
        GdlVisitors.visitAll(body, GdlVisitor())
        return sentences

    @classmethod
    def getRules(cls, description):
        """ generated source for method getRules """
        return Iterables.transform(Iterables.filter(description, Predicate()), Function())

    ALWAYS_NEEDED_SENTENCE_NAMES = ImmutableSet.of(GdlPool.NEXT, GdlPool.GOAL, GdlPool.LEGAL, GdlPool.INIT, GdlPool.ROLE, GdlPool.BASE, GdlPool.INPUT, GdlPool.TRUE, GdlPool.DOES)

    @classmethod
    def populateInitialNeededConstants(cls, newNeededConstantsByForm, curDomains, model):
        """ generated source for method populateInitialNeededConstants """
        for form in model.getSentenceForms():
            ConcurrencyUtils.checkForInterruption()
            if cls.ALWAYS_NEEDED_SENTENCE_NAMES.contains(name):
                newNeededConstantsByForm.get(form).putAll(curDomains.get(form))
        for rule in getRules(model.getDescription()):
            for sentence in getAllSentencesInBody(rule.getBody()):
                addConstantsFromSentenceIfInOldDomain(newNeededConstantsByForm, curDomains, model, sentence)

    @classmethod
    def addConstantsFromSentenceIfInOldDomain(cls, newConstantsByForm, oldDomain, model, sentence):
        """ generated source for method addConstantsFromSentenceIfInOldDomain """
        form = model.getSentenceForm(sentence)
        tuple_ = GdlUtils.getTupleFromSentence(sentence)
        if len(tuple_) != form.getTupleSize():
            raise IllegalStateException()
        i = 0
        while i < form.getTupleSize():
            ConcurrencyUtils.checkForInterruption()
            if isinstance(term, (GdlConstant, )):
                if oldDomainForTerm.contains(term):
                    newConstantsByForm.get(form).put(i, term)
            i += 1

    @classmethod
    def toSentenceDomainModel(cls, neededAndPossibleConstantsByForm, formModel):
        """ generated source for method toSentenceDomainModel """
        domains = Maps.newHashMap()
        for form in formModel.getSentenceForms():
            ConcurrencyUtils.checkForInterruption()
            domains.put(form, CartesianSentenceFormDomain.create(form, neededAndPossibleConstantsByForm.get(form)))
        return ImmutableSentenceDomainModel.create(formModel, domains)

