#!/usr/bin/env python
""" generated source for module GdlFunction """
# package: org.ggp.base.util.gdl.grammar
import java.util.List

@SuppressWarnings("serial")
class GdlFunction(GdlTerm):
    """ generated source for class GdlFunction """
    body = List()
    ground = bool()
    name = GdlConstant()

    def __init__(self, name, body):
        """ generated source for method __init__ """
        super(GdlFunction, self).__init__()
        self.name = name
        self.body = body
        self.ground = None

    def arity(self):
        """ generated source for method arity """
        return len(self.body)

    def computeGround(self):
        """ generated source for method computeGround """
        for term in body:
            if not term.isGround():
                return False
        return True

    def get(self, index):
        """ generated source for method get """
        return self.body.get(index)

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getBody(self):
        """ generated source for method getBody """
        return self.body

    def isGround(self):
        """ generated source for method isGround """
        if self.ground == None:
            self.ground = self.computeGround()
        return self.ground

    def toSentence(self):
        """ generated source for method toSentence """
        return GdlPool.getRelation(self.name, self.body)

    def __str__(self):
        """ generated source for method toString """
        sb = StringBuilder()
        sb.append("( " + self.name + " ")
        for term in body:
            sb.append(term + " ")
        sb.append(")")
        return sb.__str__()

