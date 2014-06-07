#!/usr/bin/env python
""" generated source for module GdlProposition """
# package: org.ggp.base.util.gdl.grammar
import java.util.Collections

import java.util.List

@SuppressWarnings("serial")
class GdlProposition(GdlSentence):
    """ generated source for class GdlProposition """
    name = GdlConstant()

    def __init__(self, name):
        """ generated source for method __init__ """
        super(GdlProposition, self).__init__()
        self.name = name

    def arity(self):
        """ generated source for method arity """
        return 0

    def get(self, index):
        """ generated source for method get """
        raise RuntimeException("GdlPropositions have no body!")

    def getName(self):
        """ generated source for method getName """
        return self.name

    def isGround(self):
        """ generated source for method isGround """
        return self.name.isGround()

    def __str__(self):
        """ generated source for method toString """
        return self.name.__str__()

    def toTerm(self):
        """ generated source for method toTerm """
        return self.name

    def getBody(self):
        """ generated source for method getBody """
        return Collections.emptyList()

