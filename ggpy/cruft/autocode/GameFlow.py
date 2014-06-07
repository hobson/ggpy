#!/usr/bin/env python
""" generated source for module GameFlow """
# package: org.ggp.base.util.gdl.model
import java.util.ArrayList

import java.util.Collections

import java.util.HashMap

import java.util.HashSet

import java.util.LinkedList

import java.util.List

import java.util.Map

import java.util.Queue

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.assignments.AssignmentIterator

import org.ggp.base.util.gdl.model.assignments.Assignments

import org.ggp.base.util.gdl.model.assignments.AssignmentsFactory

import org.ggp.base.util.gdl.model.assignments.FunctionInfo

import org.ggp.base.util.gdl.model.assignments.FunctionInfoImpl

import org.ggp.base.util.gdl.transforms.CommonTransforms

import org.ggp.base.util.gdl.transforms.ConstantChecker

import org.ggp.base.util.gdl.transforms.ConstantCheckerFactory

import org.ggp.base.util.gdl.transforms.DeORer

import org.ggp.base.util.gdl.transforms.GdlCleaner

import org.ggp.base.util.gdl.transforms.VariableConstrainer

import com.google.common.collect.Multimap

# 
#  * GameFlow describes the behavior of the sentences in sentence forms that depend
#  * on which turn it is, but not on the actions of the player (past or present).
#  * These include step counters and control markers.
#  *
#  * @author Alex Landau
#  
class GameFlow(object):
    """ generated source for class GameFlow """
    INIT = GdlPool.getConstant("init")
    TRUE = GdlPool.getConstant("true")
    NEXT = GdlPool.getConstant("next")
    turnAfterLast = int()

    # We end with a loop
    sentencesTrueByTurn = ArrayList()

    # The non-constant ones
    formsControlledByFlow = Set()
    constantForms = Set()
    constantChecker = ConstantChecker()

    def __init__(self, description):
        """ generated source for method __init__ """
        description = GdlCleaner.run(description)
        description = DeORer.run(description)
        description = VariableConstrainer.replaceFunctionValuedVariables(description)
        # First we use a sentence model to get the relevant sentence forms
        model = SentenceDomainModelFactory.createWithCartesianDomains(description)
        self.formsControlledByFlow = HashSet()
        self.formsControlledByFlow.addAll(model.getIndependentSentenceForms())
        self.formsControlledByFlow.removeAll(model.getConstantSentenceForms())
        self.constantForms = model.getConstantSentenceForms()
        self.constantChecker = ConstantCheckerFactory.createWithForwardChaining(model)
        # Figure out which of these sentences are true at each stage
        solveTurns(model)

    def solveTurns(self, model):
        """ generated source for method solveTurns """
        # Before we can do anything else, we need a topological ordering on our forms
        ordering = getTopologicalOrdering(model.getIndependentSentenceForms(), model.getDependencyGraph())
        ordering.retainAll(self.formsControlledByFlow)
        # Let's add function info to the consideration...
        functionInfoMap = HashMap()
        for form in constantForms:
            functionInfoMap.put(form, FunctionInfoImpl.create(form, self.constantChecker))
        # First we set the "true" values, then we get the forms controlled by the flow...
        # Use "init" values
        trueFlowSentences = HashSet()
        for form in constantForms:
            if form.__name__ == self.INIT:
                for initSentence in constantChecker.getTrueSentences(form):
                    trueFlowSentences.add(trueSentence)
        # Go through ordering, adding to trueFlowSentences
        addSentenceForms(ordering, trueFlowSentences, model, functionInfoMap)
        self.sentencesTrueByTurn.add(trueFlowSentences)
        while True:
            # Now we use the "next" values from the previous turn
            trueFlowSentences = HashSet()
            for sentence in sentencesPreviouslyTrue:
                if sentence.__name__ == self.NEXT:
                    trueFlowSentences.add(trueSentence)
            addSentenceForms(ordering, trueFlowSentences, model, functionInfoMap)
            # Test if this turn's flow is the same as an earlier one
            while i < len(self.sentencesTrueByTurn):
                if prevSet == trueFlowSentences:
                    # Complete the loop
                    self.turnAfterLast = i
                    break
                i += 1
            self.sentencesTrueByTurn.add(trueFlowSentences)

    @SuppressWarnings("unchecked")
    def addSentenceForms(self, ordering, trueFlowSentences, model, functionInfoMap):
        """ generated source for method addSentenceForms """
        for curForm in ordering:
            # Check against trueFlowSentences, add to trueFlowSentences
            # or check against constantForms if necessary
            # Use basic Assignments class, of course
            for alwaysTrueSentences in model.getSentencesListedAsTrue(curForm):
                trueFlowSentences.add(alwaysTrueSentences)
            for rule in model.getRules(curForm):
                while asnItr.hasNext():
                    if trueFlowSentences.contains(transformedHead):
                        asnItr.changeOneInNext(varsInHead, assignment)
                    # Go through the conjuncts
                    for literal in rule.getBody():
                        if isinstance(literal, (GdlSentence, )):
                            if curForm.matches(literal):
                                raise RuntimeException("Haven't implemented recursion in the game flow")
                            if self.constantForms.contains(conjForm):
                                if not self.constantChecker.isTrueConstant(transformed):
                                    isGoodAssignment = False
                                    asnItr.changeOneInNext(GdlUtils.getVariables(literal), assignment)
                            else:
                                if not trueFlowSentences.contains(transformed):
                                    # False sentence
                                    isGoodAssignment = False
                                    asnItr.changeOneInNext(GdlUtils.getVariables(literal), assignment)
                        elif isinstance(literal, (GdlNot, )):
                            if self.constantForms.contains(conjForm):
                                if self.constantChecker.isTrueConstant(transformed):
                                    isGoodAssignment = False
                                    asnItr.changeOneInNext(GdlUtils.getVariables(literal), assignment)
                            else:
                                if trueFlowSentences.contains(transformed):
                                    # False sentence
                                    isGoodAssignment = False
                                    asnItr.changeOneInNext(GdlUtils.getVariables(literal), assignment)
                        # Nothing else needs attention, really
                    # We've gone through all the conjuncts and are at the
                    # end of the rule
                    if isGoodAssignment:
                        trueFlowSentences.add(transformedHead)
                        if varsInHead.isEmpty():
                            break
                        else:
                            asnItr.changeOneInNext(varsInHead, assignment)
            # We've gone through all the rules

    def getNumTurns(self):
        """ generated source for method getNumTurns """
        return len(self.sentencesTrueByTurn)

    @classmethod
    def getTopologicalOrdering(cls, forms, dependencyGraph):
        """ generated source for method getTopologicalOrdering """
        # We want each form as a key of the dependency graph to
        # follow all the forms in the dependency graph, except maybe itself
        queue = LinkedList(forms)
        ordering = ArrayList(len(forms))
        alreadyOrdered = HashSet()
        while not queue.isEmpty():
            # Don't add if there are dependencies
            for dependency in dependencyGraph.get(curForm):
                if not dependency == curForm and not alreadyOrdered.contains(dependency):
                    readyToAdd = False
                    break
            # Add it
            if readyToAdd:
                ordering.add(curForm)
                alreadyOrdered.add(curForm)
            else:
                queue.add(curForm)
            # TODO: Add check for an infinite loop here
            # Or replace with code that does stratification of loops
        return ordering

    def getTurnsConjunctsArePossible(self, body):
        """ generated source for method getTurnsConjunctsArePossible """
        # We want to identify the conjuncts that are used by the
        # game flow.
        relevantLiterals = ArrayList()
        for literal in body:
            if isinstance(literal, (GdlSentence, )):
                if SentenceModelUtils.inSentenceFormGroup(sentence, self.formsControlledByFlow):
                    relevantLiterals.add(literal)
            elif isinstance(literal, (GdlNot, )):
                if SentenceModelUtils.inSentenceFormGroup(innerSentence, self.formsControlledByFlow):
                    relevantLiterals.add(literal)
        # If none are related to the game flow, then that's it. It can
        # happen on any turn.
        # if(relevantLiterals.isEmpty())
        # return getCompleteTurnSet();
        turnsPossible = HashSet(getCompleteTurnSet())
        # For each of the relevant literals, we need to see if there are assignments
        # such that
        for literal in relevantLiterals:
            if isinstance(literal, (GdlSentence, )):
                while t < self.getNumTurns():
                    if self.sentencesTrueByTurn.get(t).contains(literal):
                        turns.add(t)
                    else:
                        for s in sentencesTrueByTurn.get(t):
                            # Could be true if there's an assignment
                            if None != GdlUtils.getAssignmentMakingLeftIntoRight(literal, s):
                                turns.add(t)
                                break
                    t += 1
            elif isinstance(literal, (GdlNot, )):
                while t < self.getNumTurns():
                    if not self.sentencesTrueByTurn.get(t).contains(internal):
                        turns.add(t)
                    else:
                        for s in sentencesTrueByTurn.get(t):
                            if None != GdlUtils.getAssignmentMakingLeftIntoRight(internal, s):
                                turns.add(t)
                                break
                    t += 1
            # Accumulate turns
            # Note that all relevant conjuncts must be true, so this
            # is an intersection of when the individual conjuncts
            # could be true.
            turnsPossible.retainAll(turns)
        return turnsPossible

    completeTurnSet = None

    def getCompleteTurnSet(self):
        """ generated source for method getCompleteTurnSet """
        if self.completeTurnSet == None:
            self.completeTurnSet = HashSet()
            while i < self.getNumTurns():
                self.completeTurnSet.add(i)
                i += 1
            self.completeTurnSet = Collections.unmodifiableSet(self.completeTurnSet)
        return self.completeTurnSet

    def getSentenceForms(self):
        """ generated source for method getSentenceForms """
        return self.formsControlledByFlow

    def getSentencesTrueOnTurn(self, i):
        """ generated source for method getSentencesTrueOnTurn """
        return self.sentencesTrueByTurn.get(i)

    def getTurnAfterLast(self):
        """ generated source for method getTurnAfterLast """
        return self.turnAfterLast

