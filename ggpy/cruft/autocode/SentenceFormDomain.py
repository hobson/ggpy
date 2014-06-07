#!/usr/bin/env python
""" generated source for module SentenceFormDomain """
# package: org.ggp.base.util.gdl.model
import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

# 
#  * A SentenceFormDomain contains information about the possible
#  * sentences of a particular sentence form within a game. In other
#  * words, it captures information about which constants can be
#  * in which positions in the SentenceForm.
#  
class SentenceFormDomain(Iterable, GdlSentence):
    """ generated source for interface SentenceFormDomain """
    __metaclass__ = ABCMeta
    # 
    # 	 * Returns the SentenceForm associated with this domain.
    # 	 
    @abstractmethod
    def getForm(self):
        """ generated source for method getForm """

    # 
    # 	 * Returns a set containing every constant that can appear in
    # 	 * the given slot index in the sentence form.
    # 	 
    @abstractmethod
    def getDomainForSlot(self, slotIndex):
        """ generated source for method getDomainForSlot """

