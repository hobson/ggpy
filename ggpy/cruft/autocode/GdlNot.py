#!/usr/bin/env python
""" generated source for module GdlNot """
# package: org.ggp.base.util.gdl.grammar
@SuppressWarnings("serial")
class GdlNot(GdlLiteral):
    """ generated source for class GdlNot """
    body = GdlLiteral()
    ground = bool()

    def __init__(self, body):
        """ generated source for method __init__ """
        super(GdlNot, self).__init__()
        self.body = body
        self.ground = None

    def getBody(self):
        """ generated source for method getBody """
        return self.body

    def isGround(self):
        """ generated source for method isGround """
        if self.ground == None:
            self.ground = self.body.isGround()
        return self.ground

    def __str__(self):
        """ generated source for method toString """
        return "( not " + self.body + " )"

