#!/usr/bin/env python
""" generated source for module AssignmentIterator """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.Collection

import java.util.Iterator

import java.util.Map

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlVariable

class AssignmentIterator(Iterator, Map, GdlVariable, GdlConstant):
    """ generated source for interface AssignmentIterator """
    __metaclass__ = ABCMeta
    # 
    # 	 * Request that the next assignment change at least one
    # 	 * of the listed variables from its current assignment.
    # 	 
    @abstractmethod
    def changeOneInNext(self, varsToChange, assignment):
        """ generated source for method changeOneInNext """

