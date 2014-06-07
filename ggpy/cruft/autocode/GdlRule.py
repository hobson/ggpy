#!/usr/bin/env python
""" generated source for module GdlRule """
# package: org.ggp.base.util.gdl.grammar
import java.util.List

@SuppressWarnings("serial")
class GdlRule(Gdl):
    """ generated source for class GdlRule """
    body = List()
    ground = bool()
    head = GdlSentence()

    def __init__(self, head, body):
        """ generated source for method __init__ """
        super(GdlRule, self).__init__()
        self.head = head
        self.body = body
        self.ground = None

    def arity(self):
        """ generated source for method arity """
        return len(self.body)

    def computeGround(self):
        """ generated source for method computeGround """
        for literal in body:
            if not literal.isGround():
                return False
        return True

    def get(self, index):
        """ generated source for method get """
        return self.body.get(index)

    def getHead(self):
        """ generated source for method getHead """
        return self.head

    def getBody(self):
        """ generated source for method getBody """
        return self.body

    def isGround(self):
        """ generated source for method isGround """
        if self.ground == None:
            self.ground = self.computeGround()
        return self.ground

    def __str__(self):
        """ generated source for method toString """
        sb = StringBuilder()
        sb.append("( <= " + self.head + " ")
        for literal in body:
            sb.append(literal + " ")
        sb.append(")")
        return sb.__str__()

