#!/usr/bin/env python
""" generated source for module CondensationIsolator """
# package: org.ggp.base.util.gdl.transforms
import java.io.BufferedWriter

import java.io.File

import java.io.FileWriter

import java.io.IOException

import java.util.ArrayList

import java.util.Collection

import java.util.Collections

import java.util.HashSet

import java.util.LinkedList

import java.util.List

import java.util.Map

import java.util.Queue

import java.util.Set

import org.ggp.base.util.concurrency.ConcurrencyUtils

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.CartesianSentenceFormDomain

import org.ggp.base.util.gdl.model.SentenceDomainModel

import org.ggp.base.util.gdl.model.SentenceDomainModelFactory

import org.ggp.base.util.gdl.model.SentenceDomainModelOptimizer

import org.ggp.base.util.gdl.model.SentenceDomainModels

import org.ggp.base.util.gdl.model.SentenceDomainModels.VarDomainOpts

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SentenceFormDomain

import org.ggp.base.util.gdl.model.SentenceFormModel

import org.ggp.base.util.gdl.model.SentenceForms

import org.ggp.base.util.gdl.model.SentenceModelUtils

import org.ggp.base.util.gdl.model.SimpleSentenceForm

import org.ggp.base.util.gdl.model.assignments.AssignmentsImpl

import com.google.common.collect.Lists

import com.google.common.collect.Multimap

import com.google.common.collect.Sets

# 
#  * The CondensationIsolator is a GDL transformation designed to split up
#  * rules in a way that results in smaller propnets. For example, we may
#  * have a rule as follows:
#  *
#  * (<= (foo ?x ?y)
#  *     (bar ?x ?y)
#  *     (baz ?y ?z))
#  *
#  * In the propnet, this will result in one AND node for each combination
#  * of ?x, ?y, and ?z. The CondensationIsolator would split it up as follows:
#  *
#  * (<= (foo ?x ?y)
#  *     (bar ?x ?y)
#  *     (baz_tmp0 ?y))
#  * (<= (baz_tmp0 ?y)
#  *     (baz ?y ?z))
#  *
#  * In the propnet, there will now be one AND node for each combination of
#  * ?x and ?y and one new link for each combination of ?y and ?z, but there
#  * will not be a cross-product of the domains of all three.
#  *
#  * "Condensation" refers to the type of rule generated, in which we simply
#  * ignore certain variables.
#  *
#  * @author Alex Landau
#  *
#  
class CondensationIsolator(object):
    """ generated source for class CondensationIsolator """
    @classmethod
    def run(cls, description):
        """ generated source for method run """
        # This class is not put together in any "optimal" way, so it's left in
        # an unpolished state for now. A better version would use estimates of
        # the impact of breaking apart rules. (It also needs to stop itself from
        # making multiple new relations with the same meaning.)
        # This version will be rather advanced.
        # In particular, it will try to incorporate
        # 1) More thorough scanning for condensations;
        # 2) Condensations that are only safe to perform because of mutexes.
        # TODO: Don't perform condensations on stuff like (add _ _ _)...
        # In general, don't perform condensations where the headroom is huge?
        # Better yet... DON'T perform condensations on recursive functions!
        # As for headroom... maybe make sure that # of vars eliminated > # "kept"
        # Or make sure none are kept? Use directional connected components?
        description = GdlCleaner.run(description)
        description = DeORer.run(description)
        description = VariableConstrainer.replaceFunctionValuedVariables(description)
        # How do we define a condensation, and what needs to be true in it?
        # Definition: A condensation set is a set of conjuncts of a
        # sentence.
        # Restrictions:
        # 1) There must be some variable not in the head of the sentence that
        #    appears exclusively in the condensation set. (This means we can
        #    easily find sets one of which must be a condensation set.)
        # 2) For any variable appearing in a distinct or not conjunct in the set,
        #    there must be a positive conjunct in the set also containing that
        #    variable. This does apply to variables found in the head.
        # 3) There must be at least one non-distinct literal outside the
        #    condensation set.
        # How mutexes work:
        # Say we have a rule
        #   (<= (r1 ?b)
        #       (r2 ?a ?b ?c)
        #       (r3 ?b ?c)
        # 		(r4 ?a)
        # 		(r5 ?c))
        # If we wanted to factor out ?a, we'd normally have to do
        #   (<= (r6 ?b ?c)
        # 		 * 		(r2 ?a ?b ?c)
        # 		 * 		(r4 ?a))
        # 		 *  (<= (r1 ?b)
        # 		 * 		(r6 ?b ?c)
        # 		 * 		(r3 ?b ?c)
        # 		 * 		(r5 ?c))
        # 		 * But if we know r2 is a mutex, instead we can do (notice r2 splitting):
        # 		 *  (<= (r6 ?b)
        # 		 * 		(r2 ?a ?b ?c)
        # 		 * 		(r4 ?a))
        # 		 *  (<= (r1 ?b)
        # 		 *  	(r2 ?a ?b ?c)
        # 		 *  	(r6 ?b)
        # 		 *  	(r3 ?b ?c)
        # 		 *  	(r5 ?c))
        # 		 * Which in turn becomes:
        # 		 *  (<= (r6 ?b)
        # 		 * 		(r2 ?a ?b ?c)
        # 		 * 		(r4 ?a))
        # 		 *  (<= (r7 ?b)
        # 		 *  	(r2 ?a ?b ?c)
        # 		 *  	(r3 ?b ?c)
        # 		 *  	(r5 ?c))
        # 		 *  (<= (r1 ?b)
        # 		 *  	(r6 ?b)
        # 		 *		(r7 ?b))
        # 		 * Both r6 and r7 can be further condensed to ignore ?c and ?a,
        # 		 * respectively. What just happened?
        # 		 * 1) The condensation set for ?a included the mutex r2.
        # 		 * 2) r2 (by itself) would have required ?c to be included as an
        # 		 *    argument passed back to the original rule, which is undesirable.
        # 		 *    Instead, as it's a mutex, we leave a copy in the original rule
        # 		 *    and don't include the ?c.
        # 		 *
        # 		 * So, what kind of algorithm can we find to solve this task?
        # 		 
        newDescription = ArrayList()
        rulesToAdd = LinkedList()
        for gdl in description:
            if isinstance(gdl, (GdlRule, )):
                rulesToAdd.add(gdl)
            else:
                newDescription.add(gdl)
        # Don't use the model indiscriminately; it reflects the old description,
        # not necessarily the new one
        model = SentenceDomainModelFactory.createWithCartesianDomains(description)
        model = SentenceDomainModelOptimizer.restrictDomainsToUsefulValues(model)
        sentenceNameSource = UnusedSentenceNameSource.create(model)
        constantChecker = ConstantCheckerFactory.createWithForwardChaining(model)
        constantForms = model.getConstantSentenceForms()
        ConcurrencyUtils.checkForInterruption()
        curDescription = Lists.newArrayList(description)
        while not rulesToAdd.isEmpty():
            if isRecursive(curRule):
                # Don't mess with it!
                newDescription.add(curRule)
                continue 
            if SentenceModelUtils.inSentenceFormGroup(curRuleHead, constantForms):
                newDescription.add(curRule)
                continue 
            ConcurrencyUtils.checkForInterruption()
            if condensationSet != None:
                rulesToAdd.addAll(newRules)
                # Since we're making only small changes, we can readjust
                # the model as we go, instead of recomputing it
                replacementDescription.removeAll(oldRules)
                replacementDescription.addAll(newRules)
                curDescription = replacementDescription
                model = augmentModelWithNewForm(model, newRules)
            else:
                newDescription.add(curRule)
        return newDescription

    @classmethod
    @SuppressWarnings("unused")
    def saveKif(cls, description):
        """ generated source for method saveKif """
        # Save the description in a new file
        # Useful for debugging chains of condensations to see
        # which cause decreased performance
        filename = "ci0.kif"
        filenum = 0
        file_ = None
        while file_ == None or file_.exists():
            filenum += 1
            filename = "ci" + filenum + ".kif"
            file_ = File(filename)
            file_ = File("games/rulesheets", filename)
        out = None
        try:
            out = BufferedWriter(FileWriter(file_))
            for gdl in description:
                out.append(gdl.__str__() + "\n")
        except IOException as e:
            e.printStackTrace()
        finally:
            try:
                if out != None:
                    out.close()
            except IOException as e:
                pass

    @classmethod
    def isRecursive(cls, rule):
        """ generated source for method isRecursive """
        for literal in rule.getBody():
            if isinstance(literal, (GdlSentence, )):
                if (literal).__name__ == rule.getHead(.__name__):
                    return True
        return False

    class UnusedSentenceNameSource(object):
        """ generated source for class UnusedSentenceNameSource """
        allNamesSoFar = Set()

        def __init__(self, initialNames):
            """ generated source for method __init__ """
            self.allNamesSoFar = Sets.newHashSet(initialNames)

        @classmethod
        def create(cls, model):
            """ generated source for method create """
            sentenceFormNames = SentenceForms.getNames(model.getSentenceForms())
            return cls.UnusedSentenceNameSource(sentenceFormNames)

        def getNameWithPrefix(self, prefix):
            """ generated source for method getNameWithPrefix """
            i = 0
            while True:
                if not self.allNamesSoFar.contains(candidateName):
                    self.allNamesSoFar.add(candidateName)
                    return GdlPool.getConstant(candidateName)
                i += 1

    @classmethod
    def applyCondensation(cls, condensationSet, rule, sentenceNameSource):
        """ generated source for method applyCondensation """
        varsInCondensationSet = HashSet()
        for literal in condensationSet:
            varsInCondensationSet.addAll(GdlUtils.getVariables(literal))
        varsToKeep = HashSet()
        for literal in condensationSet:
            varsToKeep.addAll(GdlUtils.getVariables(literal))
        varsToKeep2 = HashSet()
        varsToKeep2.addAll(GdlUtils.getVariables(rule.getHead()))
        for literal in rule.getBody():
            if not condensationSet.contains(literal):
                varsToKeep2.addAll(GdlUtils.getVariables(literal))
        varsToKeep.retainAll(varsToKeep2)
        orderedVars = ArrayList(varsToKeep)
        condenserName = sentenceNameSource.getNameWithPrefix(rule.getHead().__name__)
        condenserHead = GdlSentence()
        if orderedVars.isEmpty():
            condenserHead = GdlPool.getProposition(condenserName)
        else:
            condenserHead = GdlPool.getRelation(condenserName, orderedVars)
        condenserBody = ArrayList(condensationSet)
        condenserRule = GdlPool.getRule(condenserHead, condenserBody)
        remainingLiterals = ArrayList()
        for literal in rule.getBody():
            if not condensationSet.contains(literal):
                remainingLiterals.add(literal)
        remainingLiterals.add(condenserHead)
        modifiedRule = GdlPool.getRule(rule.getHead(), remainingLiterals)
        newRules = ArrayList(2)
        newRules.add(condenserRule)
        newRules.add(modifiedRule)
        return newRules

    @classmethod
    def getCondensationSet(cls, rule, model, checker, sentenceNameSource):
        """ generated source for method getCondensationSet """
        varsInRule = GdlUtils.getVariables(rule)
        varsInHead = GdlUtils.getVariables(rule.getHead())
        varsNotInHead = ArrayList(varsInRule)
        varsNotInHead.removeAll(varsInHead)
        for var in varsNotInHead:
            ConcurrencyUtils.checkForInterruption()
            for literal in rule.getBody():
                if GdlUtils.getVariables(literal).contains(var):
                    minSet.add(literal)
            for literal in minSet:
                if isinstance(literal, (GdlRelation, )):
                    varsSupplied.addAll(GdlUtils.getVariables(literal))
                elif isinstance(literal, (GdlDistinct, )) or isinstance(literal, (GdlNot, )):
                    varsNeeded.addAll(GdlUtils.getVariables(literal))
            varsNeeded.removeAll(varsSupplied)
            if not varsNeeded.isEmpty():
                continue 
            for varNeeded in varsNeeded:
                for literal in rule.getBody():
                    if isinstance(literal, (GdlRelation, )):
                        if GdlUtils.getVariables(literal).contains(varNeeded):
                            suppliers.add(literal)
                candidateSuppliersList.add(suppliers)
            for suppliers in candidateSuppliersList:
                if Collections.disjoint(suppliers, literalsToAdd):
                    literalsToAdd.add(suppliers.iterator().next())
            minSet.addAll(literalsToAdd)
            if goodCondensationSetByHeuristic(minSet, rule, model, checker, sentenceNameSource):
                return minSet
        return None

    @classmethod
    def goodCondensationSetByHeuristic(cls, minSet, rule, model, checker, sentenceNameSource):
        """ generated source for method goodCondensationSetByHeuristic """
        assignments = AssignmentsImpl.getNumAssignmentsEstimate(rule, SentenceDomainModels.getVarDomains(rule, model, VarDomainOpts.INCLUDE_HEAD), checker)
        literals = rule.arity()
        if literals > 1:
            literals += 1
        curRuleHeuristic = assignments * literals
        newRules = cls.applyCondensation(minSet, rule, sentenceNameSource)
        r1 = newRules.get(0)
        r2 = newRules.get(1)
        newModel = augmentModelWithNewForm(model, newRules)
        a1 = AssignmentsImpl.getNumAssignmentsEstimate(r1, SentenceDomainModels.getVarDomains(r1, newModel, VarDomainOpts.INCLUDE_HEAD), checker)
        a2 = AssignmentsImpl.getNumAssignmentsEstimate(r2, SentenceDomainModels.getVarDomains(r2, newModel, VarDomainOpts.INCLUDE_HEAD), checker)
        l1 = r1.arity()
        if l1 > 1:
            l1 += 1
        l2 = r2.arity()
        if l2 > 1:
            l2 += 1
        newRulesHeuristic = a1 * l1 + a2 * l2
        return newRulesHeuristic < curRuleHeuristic

    @classmethod
    def augmentModelWithNewForm(cls, oldModel, newRules):
        """ generated source for method augmentModelWithNewForm """
        newForm = SimpleSentenceForm.create(newRules.get(0).getHead())
        newFormDomain = getNewFormDomain(newRules.get(0), oldModel, newForm)
        return SentenceDomainModel()

    @classmethod
    def getNewFormDomain(cls, condensingRule, oldModel, newForm):
        """ generated source for method getNewFormDomain """
        varDomains = SentenceDomainModels.getVarDomains(condensingRule, oldModel, VarDomainOpts.BODY_ONLY)
        domainsForSlots = Lists.newArrayList()
        for term in GdlUtils.getTupleFromSentence(condensingRule.getHead()):
            if not (isinstance(term, (GdlVariable, ))):
                raise RuntimeException("Expected all slots in the head of a condensing rule to be variables, but the rule was: " + condensingRule)
            domainsForSlots.add(varDomains.get(term))
        return CartesianSentenceFormDomain.create(newForm, domainsForSlots)

