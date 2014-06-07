#!/usr/bin/env python
""" generated source for module GdlDistinct """
# package: org.ggp.base.util.gdl.grammar
@SuppressWarnings("serial")
class GdlDistinct(GdlLiteral):
    """ generated source for class GdlDistinct """
    arg1 = GdlTerm()
    arg2 = GdlTerm()
    ground = bool()

    def __init__(self, arg1, arg2):
        """ generated source for method __init__ """
        super(GdlDistinct, self).__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.ground = None

    def getArg1(self):
        """ generated source for method getArg1 """
        return self.arg1

    def getArg2(self):
        """ generated source for method getArg2 """
        return self.arg2

    def isGround(self):
        """ generated source for method isGround """
        if self.ground == None:
            self.ground = self.arg1.isGround() and self.arg2.isGround()
        return self.ground

    def __str__(self):
        """ generated source for method toString """
        return "( distinct " + self.arg1 + " " + self.arg2 + " )"

