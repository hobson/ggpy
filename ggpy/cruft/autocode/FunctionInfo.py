#!/usr/bin/env python
""" generated source for module FunctionInfo """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.SentenceForm

import com.google.common.collect.ImmutableList

class FunctionInfo(object):
    """ generated source for interface FunctionInfo """
    __metaclass__ = ABCMeta
    # 
    # 	 * Returns the SentenceForm that this functionality information
    # 	 * is defined for.
    # 	 
    @abstractmethod
    def getSentenceForm(self):
        """ generated source for method getSentenceForm """

    # 
    # 	 * Returns a list of boolean values indicating which slots in
    # 	 * the given sentence form can be determined from the remaining
    # 	 * slots. (For example, in a successor function, either slot's
    # 	 * value would be uniquely determined by the other slot's, so
    # 	 * this would return [true, true].)
    # 	 
    @abstractmethod
    def getDependentSlots(self):
        """ generated source for method getDependentSlots """

    # 
    # 	 * Given a sentence of the constant form's sentence form, finds all
    # 	 * the variables in the sentence that can be produced functionally.
    # 	 * That is, the value of any one variable in this set can be determined
    # 	 * given that every other variable in the sentence is already defined.
    # 	 *
    # 	 * Note the corner case: If a variable appears twice in a sentence,
    # 	 * it CANNOT be produced in this way.
    # 	 
    # TODO: Replace with utility function in FunctionInfos
    @abstractmethod
    def getProducibleVars(self, sentence):
        """ generated source for method getProducibleVars """

    # 
    # 	 * Returns a map from input tuples to results for the given slot of
    # 	 * the sentence form. The format for input tuples is a list of
    # 	 * GdlConstants of size (n-1), where n is the tuple size of the
    # 	 * sentence form. The input tuple contains every constant in the
    # 	 * sentence, in order, except for the slot of interest, which is
    # 	 * omitted from that list.
    # 	 
    @abstractmethod
    def getValueMap(self, varIndex):
        """ generated source for method getValueMap """

