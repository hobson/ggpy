#!/usr/bin/env python
""" generated source for module FunctionInfos """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.HashSet

import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

class FunctionInfos(object):
    """ generated source for class FunctionInfos """
    @classmethod
    def getProducibleVars(cls, functionInfo, sentence):
        """ generated source for method getProducibleVars """
        if not functionInfo.getSentenceForm().matches(sentence):
            raise RuntimeException("Sentence " + sentence + " does not match constant form")
        tuple_ = GdlUtils.getTupleFromSentence(sentence)
        dependentSlots = functionInfo.getDependentSlots()
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
                elif dependentSlots.get(i):
                    candidateVars.add(var)
                else:
                    nonCandidateVars.add(var)
            i += 1
        return candidateVars

