#!/usr/bin/env python
""" generated source for module Unifier """
# package: org.ggp.base.util.prover.aima.unifier
import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.prover.aima.substitution.Substitution

class Unifier(object):
    """ generated source for class Unifier """
    @classmethod
    def unify(cls, x, y):
        """ generated source for method unify """
        theta = Substitution()
        isGood = unifyTerm(x.toTerm(), y.toTerm(), theta)
        if isGood:
            return theta
        else:
            return None

    @classmethod
    def unifyTerm(cls, x, y, theta):
        """ generated source for method unifyTerm """
        if x == y:
            return True
        if (isinstance(x, (GdlConstant, ))) and (isinstance(y, (GdlConstant, ))):
            if not x == y:
                return False
        elif isinstance(x, (GdlVariable, )):
            if not unifyVariable(x, y, theta):
                return False
        elif isinstance(y, (GdlVariable, )):
            if not unifyVariable(y, x, theta):
                return False
        elif (isinstance(x, (GdlFunction, ))) and (isinstance(y, (GdlFunction, ))):
            if not cls.unifyTerm(xFunction.__name__, yFunction.__name__, theta):
                return False
            while i < xFunction.arity():
                if not cls.unifyTerm(xFunction.get(i), yFunction.get(i), theta):
                    return False
                i += 1
        else:
            return False
        return True

    @classmethod
    def unifyVariable(cls, var, x, theta):
        """ generated source for method unifyVariable """
        if theta.contains(var):
            return cls.unifyTerm(theta.get(var), x, theta)
        elif (isinstance(x, (GdlVariable, ))) and theta.contains(x):
            return cls.unifyTerm(var, theta.get(x), theta)
        else:
            theta.put(var, x)
            return True

