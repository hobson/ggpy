#!/usr/bin/env python
""" generated source for module GdlVariable """
# package: org.ggp.base.util.gdl.grammar
@SuppressWarnings("serial")
class GdlVariable(GdlTerm):
    """ generated source for class GdlVariable """
    name = str()

    def __init__(self, name):
        """ generated source for method __init__ """
        super(GdlVariable, self).__init__()
        self.name = name.intern()

    def getName(self):
        """ generated source for method getName """
        return self.name

    def isGround(self):
        """ generated source for method isGround """
        return False

    def toSentence(self):
        """ generated source for method toSentence """
        raise RuntimeException("Unable to convert a GdlVariable to a GdlSentence!")

    def __str__(self):
        """ generated source for method toString """
        return self.name

