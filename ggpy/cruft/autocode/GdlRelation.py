#!/usr/bin/env python
""" generated source for module GdlRelation """
# package: org.ggp.base.util.gdl.grammar
import java.util.List

@SuppressWarnings("serial")
class GdlRelation(GdlSentence):
    """ generated source for class GdlRelation """
    body = List()
    ground = bool()
    name = GdlConstant()

    def __init__(self, name, body):
        """ generated source for method __init__ """
        super(GdlRelation, self).__init__()
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

    def isGround(self):
        """ generated source for method isGround """
        if self.ground == None:
            self.ground = self.computeGround()
        return self.ground

    def __str__(self):
        """ generated source for method toString """
        sb = StringBuilder()
        sb.append("( " + self.name + " ")
        for term in body:
            sb.append(term + " ")
        sb.append(")")
        return sb.__str__()

    def toTerm(self):
        """ generated source for method toTerm """
        return GdlPool.getFunction(self.name, self.body)

    def getBody(self):
        """ generated source for method getBody """
        return self.body

