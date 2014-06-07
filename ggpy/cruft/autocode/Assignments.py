#!/usr/bin/env python
""" generated source for module Assignments """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.Map

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlVariable

# TODO: Get rid of this class in some way...
# Or, just remake into AssignmentIterationPlan
class Assignments(Iterable, Map, GdlVariable, GdlConstant):
    """ generated source for interface Assignments """
    __metaclass__ = ABCMeta
    @abstractmethod
    def getIterator(self):
        """ generated source for method getIterator """

