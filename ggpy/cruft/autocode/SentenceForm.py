#!/usr/bin/env python
""" generated source for module SentenceForm """
# package: org.ggp.base.util.gdl.model
import java.util.List

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

# 
#  * A sentence form captures the structure of a group of possible
#  * GdlSentences. Two sentences have the same form if they have the
#  * same name and include the same functions in the same place
#  *
#  * Implementations of SentenceForm should be immutable. They
#  * should extend {@link AbstractSentenceForm} for implementations
#  * of hashCode and equals that will be compatible with other
#  * SentenceForms, as well as a recommended implementation of
#  * toString.
#  
class SentenceForm(object):
    """ generated source for interface SentenceForm """
    __metaclass__ = ABCMeta
    # 
    # 	 * Returns the name of all sentences with this form.
    # 	 
    @abstractmethod
    def getName(self):
        """ generated source for method getName """

    # 
    # 	 * Returns a sentence form exactly like this one, except
    # 	 * with a new name.
    # 	 
    @abstractmethod
    def withName(self, name):
        """ generated source for method withName """

    # 
    # 	 * Returns true iff the given sentence is of this sentence form.
    # 	 
    @abstractmethod
    def matches(self, relation):
        """ generated source for method matches """

    # 
    # 	 * Returns the number of constants and/or variables that a sentence
    # 	 * of this form contains.
    # 	 
    @abstractmethod
    def getTupleSize(self):
        """ generated source for method getTupleSize """

    # 
    # 	 * Given a list of GdlConstants and/or GdlVariables in the
    # 	 * order they would appear in a sentence of this sentence form,
    # 	 * returns that sentence.
    # 	 *
    # 	 * For the opposite operation (getting a tuple from a sentence),
    # 	 * see {@link GdlUtils#getTupleFromSentence(GdlSentence)} and
    # 	 * {@link GdlUtils#getTupleFromGroundSentence(GdlSentence)}.
    # 	 
    @abstractmethod
    def getSentenceFromTuple(self, tuple_):
        """ generated source for method getSentenceFromTuple """

