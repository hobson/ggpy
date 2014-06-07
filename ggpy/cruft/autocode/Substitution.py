#!/usr/bin/env python
""" generated source for module Substitution """
# package: org.ggp.base.util.prover.aima.substitution
import java.util.HashMap

import java.util.Map

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

class Substitution(object):
    """ generated source for class Substitution """
    contents = Map()

    def __init__(self):
        """ generated source for method __init__ """
        self.contents = HashMap()

    def compose(self, thetaPrime):
        """ generated source for method compose """
        result = Substitution()
        result.contents.putAll(self.contents)
        result.contents.putAll(thetaPrime.contents)
        return result

    def contains(self, variable):
        """ generated source for method contains """
        return self.contents.containsKey(variable)

    def equals(self, o):
        """ generated source for method equals """
        if (o != None) and (isinstance(o, (Substitution, ))):
            return substitution.contents == self.contents
        return False

    def get(self, variable):
        """ generated source for method get """
        return self.contents.get(variable)

    def hashCode(self):
        """ generated source for method hashCode """
        return self.contents.hashCode()

    def put(self, variable, term):
        """ generated source for method put """
        self.contents.put(variable, term)

    # 
    # 	 * Creates an identical substitution.
    # 	 *
    # 	 * @return A new, identical substitution.
    # 	 
    def copy(self):
        """ generated source for method copy """
        copy = Substitution()
        copy.contents.putAll(self.contents)
        return copy

    def __str__(self):
        """ generated source for method toString """
        sb = StringBuilder()
        sb.append("{ ")
        for variable in contents.keySet():
            sb.append(variable + "/" + self.contents.get(variable) + " ")
        sb.append("}")
        return sb.__str__()

