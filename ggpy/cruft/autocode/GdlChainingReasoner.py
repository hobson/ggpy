#!/usr/bin/env python
""" generated source for module GdlChainingReasoner """
# package: org.ggp.base.util.reasoner.gdl
import java.util.Collection

import java.util.Map

import java.util.Map.Entry

import java.util.Set

import org.ggp.base.util.concurrency.ConcurrencyUtils

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.SentenceDomainModel

import org.ggp.base.util.gdl.model.SentenceDomainModels

import org.ggp.base.util.gdl.model.SentenceDomainModels.VarDomainOpts

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SentenceFormModel

import org.ggp.base.util.gdl.model.assignments.AddibleFunctionInfo

import org.ggp.base.util.gdl.model.assignments.AssignmentIterator

import org.ggp.base.util.gdl.model.assignments.Assignments

import org.ggp.base.util.gdl.model.assignments.AssignmentsImpl

import org.ggp.base.util.gdl.model.assignments.FunctionInfo

import org.ggp.base.util.gdl.transforms.CommonTransforms

import org.ggp.base.util.reasoner.DifferentialForwardChainingReasoner

import com.google.common.collect.ImmutableMultimap

import com.google.common.collect.SetMultimap

# 
#  * An implementation of a ForwardChainingReasoner that uses Gdl objects
#  * directly and allows for differential processing of rules.
#  
class GdlChainingReasoner(DifferentialForwardChainingReasoner, GdlRule, GdlSentenceSet):
    """ generated source for class GdlChainingReasoner """
    model = SentenceFormModel()
    constants = ImmutableMultimap()

    def __init__(self, model, constants):
        """ generated source for method __init__ """
        super(GdlChainingReasoner, self).__init__()
        self.model = model
        self.constants = constants

    @classmethod
    def create(cls, model):
        """ generated source for method create """
        constantsBuilder = ImmutableMultimap.builder()
        for form in model.getSentenceForms():
            constantsBuilder.putAll(form, model.getSentencesListedAsTrue(form))
        return GdlChainingReasoner(model, constantsBuilder.build())

    def getConstantSentences(self):
        """ generated source for method getConstantSentences """
        return GdlSentenceSet.create(self.constants)

    def getRuleResults(self, rule, domainModel, sentencesSoFar):
        """ generated source for method getRuleResults """
        ConcurrencyUtils.checkForInterruption()
        headForm = self.model.getSentenceForm(rule.getHead())
        varDomains = SentenceDomainModels.getVarDomains(rule, domainModel, VarDomainOpts.INCLUDE_HEAD)
        functionInfoMap = sentencesSoFar.getFunctionInfo()
        completedSentenceFormValues = sentencesSoFar.getSentences().asMap()
        assignments = AssignmentsImpl(rule, varDomains, functionInfoMap, completedSentenceFormValues)
        asnItr = assignments.getIterator()
        sentencesToAdd = GdlSentenceSet.create()
        while asnItr.hasNext():
            for literal in rule.getBody():
                ConcurrencyUtils.checkForInterruption()
                if not satisfies(assignment, literal, sentencesSoFar.getSentences()):
                    asnItr.changeOneInNext(GdlUtils.getVariables(literal), assignment)
                    allSatisfied = False
                    break
            if allSatisfied:
                sentencesToAdd.put(headForm, CommonTransforms.replaceVariables(head, assignment))
                asnItr.changeOneInNext(GdlUtils.getVariables(head), assignment)
        return sentencesToAdd

    def satisfies(self, assignment, literal, sentencesSoFar):
        """ generated source for method satisfies """
        if isinstance(literal, (GdlSentence, )):
            return satisfiesSentence(assignment, literal, sentencesSoFar)
        elif isinstance(literal, (GdlNot, )):
            if not (isinstance(body, (GdlSentence, ))):
                raise IllegalStateException("Negated literal should be a sentence but isn't: " + body)
            return not satisfiesSentence(assignment, body, sentencesSoFar)
        elif isinstance(literal, (GdlDistinct, )):
            return satisfiesDistinct(assignment, literal)
        elif isinstance(literal, (GdlOr, )):
            while i < or_.arity():
                if self.satisfies(assignment, innerLiteral, sentencesSoFar):
                    return True
                i += 1
            return False
        else:
            raise IllegalArgumentException("Unrecognized type of literal " + literal.__class__ + " for literal " + literal)

    def satisfiesSentence(self, assignment, sentence, sentencesSoFar):
        """ generated source for method satisfiesSentence """
        sentence = CommonTransforms.replaceVariables(sentence, assignment)
        form = self.model.getSentenceForm(sentence)
        return sentencesSoFar.get(form).contains(sentence)

    def satisfiesDistinct(self, assignment, distinct):
        """ generated source for method satisfiesDistinct """
        distinct = CommonTransforms.replaceVariables(distinct, assignment)
        return distinct.getArg1() != distinct.getArg2()

    def getUnion(self, oldSentences, newSentences):
        """ generated source for method getUnion """
        oldSentences.putAll(newSentences.getSentences())
        return oldSentences

    def isSubsetOf(self, oldSentences, newSentences):
        """ generated source for method isSubsetOf """
        for entry in newSentences.getSentences().entries():
            if not oldSentences.containsSentence(entry.getKey(), entry.getValue()):
                return False
        return True

    def getRuleResultsForNewSentences(self, rule, domainModel, allSentences, newSentences):
        """ generated source for method getRuleResultsForNewSentences """
        results = GdlSentenceSet.create()
        for literal in rule.getBody():
            ConcurrencyUtils.checkForInterruption()
            if isinstance(literal, (GdlSentence, )):
                addRuleResultsForChosenLiteral(rule, literal, newSentences.getSentences().get(literalForm), domainModel, allSentences, results)
            elif isinstance(literal, (GdlOr, )):
                raise IllegalArgumentException("Need more implementation work for this to work with ORs here")
        return results

    def addRuleResultsForChosenLiteral(self, rule, chosenLiteral, chosenNewSentences, domainModel, allSentences, sentencesToAdd):
        """ generated source for method addRuleResultsForChosenLiteral """
        headForm = self.model.getSentenceForm(rule.getHead())
        varDomains = SentenceDomainModels.getVarDomains(rule, domainModel, VarDomainOpts.INCLUDE_HEAD)
        functionInfoMap = allSentences.getFunctionInfo()
        completedSentenceFormValues = allSentences.getSentences().asMap()
        for chosenNewSentence in chosenNewSentences:
            if preassignments != None:
                while asnItr.hasNext():
                    for literal in rule.getBody():
                        if literal == chosenLiteral:
                            # Already satisfied
                            continue 
                        if not self.satisfies(assignment, literal, allSentences.getSentences()):
                            asnItr.changeOneInNext(GdlUtils.getVariables(literal), assignment)
                            allSatisfied = False
                            break
                    if allSatisfied:
                        if not allSentences.containsSentence(headForm, newHead):
                            sentencesToAdd.put(headForm, newHead)
                        asnItr.changeOneInNext(GdlUtils.getVariables(head), assignment)

