#!/usr/bin/env python
""" generated source for module GdlConstant """
# package: org.ggp.base.util.gdl.grammar
@SuppressWarnings("serial")
class GdlConstant(GdlTerm):
    """ generated source for class GdlConstant """
    value = str()

    def __init__(self, value):
        """ generated source for method __init__ """
        super(GdlConstant, self).__init__()
        self.value = value.intern()

    def getValue(self):
        """ generated source for method getValue """
        return self.value

    def isGround(self):
        """ generated source for method isGround """
        return True

    def toSentence(self):
        """ generated source for method toSentence """
        return GdlPool.getProposition(self)

    def __str__(self):
        """ generated source for method toString """
        return self.value

