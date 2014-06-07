#!/usr/bin/env python
""" generated source for module ForwardChainingReasoner """
# package: org.ggp.base.util.reasoner
import org.ggp.base.util.gdl.model.SentenceDomainModel

import org.ggp.base.util.gdl.transforms.VariableConstrainer

import org.ggp.base.util.reasoner.gdl.GdlChainingReasoner

# 
#  * An interface for a forward-chaining reasoner. The interface is
#  * parameterized in such a way that if a state machine (or other
#  * code) is based on it, the underlying reasoner (and associated
#  * representations of rules and sentences) can easily be swapped
#  * out for another.
#  *
#  * See {@link GdlChainingReasoner} for one such implementation.
#  
class ForwardChainingReasoner(object):
    """ generated source for interface ForwardChainingReasoner """
    __metaclass__ = ABCMeta
    # 
    # 	 * Returns a set of sentences that are always true, which can be
    # 	 * used as a basis and added to via getUnion. This includes all
    # 	 * constant values defined explicitly in the game description. It
    # 	 * may include other sentences that are always true based on game
    # 	 * rules, depending on the implementation and how it is
    # 	 * instantiated.
    # 	 
    @abstractmethod
    def getConstantSentences(self):
        """ generated source for method getConstantSentences """

    # 
    # 	 * Given a rule and all sentences known to be true so far, returns
    # 	 * all new results of applying the rule.
    # 	 *
    # 	 * For the outputs of this method to be valid, the GDL that the rule
    # 	 * is derived from should have had the {@link VariableConstrainer}
    # 	 * transformation applied to it.
    # 	 
    @abstractmethod
    def getRuleResults(self, rule, domainModel, sentencesSoFar):
        """ generated source for method getRuleResults """

    # 
    # 	 * Returns the union of the two sets of sentences. Calling this
    # 	 * method invalidates oldSentences.
    # 	 
    @abstractmethod
    def getUnion(self, oldSentences, newSentences):
        """ generated source for method getUnion """

    # 
    # 	 * Returns true iff newSentences is a subset of oldSentences.
    # 	 
    @abstractmethod
    def isSubsetOf(self, oldSentences, newSentences):
        """ generated source for method isSubsetOf """

