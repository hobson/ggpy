#!/usr/bin/env python
""" generated source for module GdlOr """
# package: org.ggp.base.util.gdl.grammar
import java.util.List

@SuppressWarnings("serial")
class GdlOr(GdlLiteral):
    """ generated source for class GdlOr """
    disjuncts = List()
    ground = bool()

    def __init__(self, disjuncts):
        """ generated source for method __init__ """
        super(GdlOr, self).__init__()
        self.disjuncts = disjuncts
        self.ground = None

    def arity(self):
        """ generated source for method arity """
        return len(self.disjuncts)

    def computeGround(self):
        """ generated source for method computeGround """
        for literal in disjuncts:
            if not literal.isGround():
                return False
        return True

    def get(self, index):
        """ generated source for method get """
        return self.disjuncts.get(index)

    def isGround(self):
        """ generated source for method isGround """
        if self.ground == None:
            self.ground = self.computeGround()
        return self.ground

    def __str__(self):
        """ generated source for method toString """
        sb = StringBuilder()
        sb.append("( or ")
        for literal in disjuncts:
            sb.append(literal + " ")
        sb.append(")")
        return sb.__str__()

