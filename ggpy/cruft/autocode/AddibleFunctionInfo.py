#!/usr/bin/env python
""" generated source for module AddibleFunctionInfo """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.List

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

class AddibleFunctionInfo(FunctionInfo):
    """ generated source for interface AddibleFunctionInfo """
    __metaclass__ = ABCMeta
    # 
    # 	 * Convenience method, equivalent to addTuple.
    # 	 
    @abstractmethod
    def addSentence(self, value):
        """ generated source for method addSentence """

    # 
    # 	 * Adds a tuple to the known values for the sentence form.
    # 	 * Adjusts the function info accordingly.
    # 	 
    @abstractmethod
    def addTuple(self, sentenceTuple):
        """ generated source for method addTuple """

