#!/usr/bin/env python
""" generated source for module FunctionInfoImpl """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.ArrayList

import java.util.HashSet

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.concurrency.ConcurrencyUtils

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.transforms.ConstantChecker

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Lists

import com.google.common.collect.Maps

# Represents information about a sentence form that is constant.
class FunctionInfoImpl(FunctionInfo):
    """ generated source for class FunctionInfoImpl """
    form = SentenceForm()

    # True iff the slot has at most one value given the other slots' values
    dependentSlots = ArrayList()
    valueMaps = Lists.newArrayList()

    def __init__(self, form, trueSentences):
        """ generated source for method __init__ """
        super(FunctionInfoImpl, self).__init__()
        self.form = form
        numSlots = form.getTupleSize()
        i = 0
        while i < numSlots:
            # We want to establish whether or not this is a constant...
            for sentence in trueSentences:
                ConcurrencyUtils.checkForInterruption()
                tuplePart.addAll(tuple_.subList(0, i))
                tuplePart.addAll(tuple_.subList(i + 1, len(tuple_)))
                if functionMap.containsKey(tuplePart):
                    # We have two tuples with different values in just this slot
                    functional = False
                    break
                # Otherwise, we record it
                functionMap.put(ImmutableList.copyOf(tuplePart), tuple_.get(i))
            if functional:
                # Record the function
                self.dependentSlots.add(True)
                self.valueMaps.add(functionMap)
            else:
                # Forget it
                self.dependentSlots.add(False)
                self.valueMaps.add(None)
            i += 1

    def getValueMap(self, index):
        """ generated source for method getValueMap """
        return self.valueMaps.get(index)

    def getDependentSlots(self):
        """ generated source for method getDependentSlots """
        return self.dependentSlots

    # 
    # 	 * Given a sentence of the constant form's sentence form, finds all
    # 	 * the variables in the sentence that can be produced functionally.
    # 	 *
    # 	 * Note the corner case: If a variable appears twice in a sentence,
    # 	 * it CANNOT be produced in this way.
    # 	 
    def getProducibleVars(self, sentence):
        """ generated source for method getProducibleVars """
        if not self.form.matches(sentence):
            raise RuntimeException("Sentence " + sentence + " does not match constant form")
        tuple_ = GdlUtils.getTupleFromSentence(sentence)
        candidateVars = HashSet()
        # Variables that appear multiple times go into multipleVars
        multipleVars = HashSet()
        # ...which, of course, means we have to spot non-candidate vars
        nonCandidateVars = HashSet()
        i = 0
        while i < len(tuple_):
            if isinstance(term, (GdlVariable, )) and not multipleVars.contains(term):
                if candidateVars.contains(var) or nonCandidateVars.contains(var):
                    multipleVars.add(var)
                    candidateVars.remove(var)
                elif self.dependentSlots.get(i):
                    candidateVars.add(var)
                else:
                    nonCandidateVars.add(var)
            i += 1
        return candidateVars

    @classmethod
    @overloaded
    def create(cls, form, constantChecker):
        """ generated source for method create """
        return FunctionInfoImpl(form, ImmutableSet.copyOf(constantChecker.getTrueSentences(form)))

    @classmethod
    @create.register(object, SentenceForm, Set)
    def create_0(cls, form, set):
        """ generated source for method create_0 """
        return FunctionInfoImpl(form, set)

    def getSentenceForm(self):
        """ generated source for method getSentenceForm """
        return self.form

    def __str__(self):
        """ generated source for method toString """
        return "FunctionInfoImpl [form=" + self.form + ", dependentSlots=" + self.dependentSlots + ", valueMaps=" + self.valueMaps + "]"

