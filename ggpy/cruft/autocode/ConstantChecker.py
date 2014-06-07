#!/usr/bin/env python
""" generated source for module ConstantChecker """
# package: org.ggp.base.util.gdl.transforms
import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SentenceFormModel

# 
#  * A ConstantChecker provides information about which sentences are true
#  * for the constant sentence forms in a game. These can be computed once
#  * at the beginning of a match, to avoid redundant computations.
#  *
#  * The preferred way to create a ConstantChecker is with
#  * {@link ConstantCheckerFactory#createWithForwardChaining(org.ggp.base.util.gdl.model.SentenceDomainModel)}.
#  
class ConstantChecker(object):
    """ generated source for interface ConstantChecker """
    __metaclass__ = ABCMeta
    # 
    # 	 * Returns true iff the sentence is of a constant form included in
    # 	 * this ConstantChecker.
    # 	 
    @abstractmethod
    def hasConstantForm(self, sentence):
        """ generated source for method hasConstantForm """

    # 
    # 	 * Returns true iff the given sentence form is constant and is included
    # 	 * in this ConstantChecker.
    # 	 
    @abstractmethod
    def isConstantForm(self, form):
        """ generated source for method isConstantForm """

    # 
    # 	 * Returns the set of all true sentences of the given constant
    # 	 * sentence form.
    # 	 
    @abstractmethod
    def getTrueSentences(self, form):
        """ generated source for method getTrueSentences """

    # 
    # 	 * Returns the set of all constant sentence forms included
    # 	 * in this ConstantChecker.
    # 	 
    @abstractmethod
    def getConstantSentenceForms(self):
        """ generated source for method getConstantSentenceForms """

    # 
    # 	 * Returns true iff the given sentence is of a constant
    # 	 * sentence form and is always true.
    # 	 
    @abstractmethod
    def isTrueConstant(self, sentence):
        """ generated source for method isTrueConstant """

    # 
    # 	 * Returns the sentence form model that the constant checker is based on.
    # 	 
    @abstractmethod
    def getSentenceFormModel(self):
        """ generated source for method getSentenceFormModel """

