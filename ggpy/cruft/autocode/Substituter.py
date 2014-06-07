#!/usr/bin/env python
""" generated source for module Substituter """
# package: org.ggp.base.util.prover.aima.substituter
import java.util.ArrayList

import java.util.List

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.prover.aima.substitution.Substitution

class Substituter(object):
    """ generated source for class Substituter """
    @classmethod
    @overloaded
    def substitute(cls, literal, theta):
        """ generated source for method substitute """
        return substituteLiteral(literal, theta)

    @classmethod
    @substitute.register(object, GdlSentence, Substitution)
    def substitute_0(cls, sentence, theta):
        """ generated source for method substitute_0 """
        return substituteSentence(sentence, theta)

    @classmethod
    @substitute.register(object, GdlRule, Substitution)
    def substitute_1(cls, rule, theta):
        """ generated source for method substitute_1 """
        return substituteRule(rule, theta)

    @classmethod
    def substituteConstant(cls, constant, theta):
        """ generated source for method substituteConstant """
        return constant

    @classmethod
    def substituteDistinct(cls, distinct, theta):
        """ generated source for method substituteDistinct """
        if distinct.isGround():
            return distinct
        else:
            return GdlPool.getDistinct(arg1, arg2)

    @classmethod
    def substituteFunction(cls, function_, theta):
        """ generated source for method substituteFunction """
        if function_.isGround():
            return function_
        else:
            while i < function_.arity():
                body.add(substituteTerm(function_.get(i), theta))
                i += 1
            return GdlPool.getFunction(name, body)

    @classmethod
    def substituteLiteral(cls, literal, theta):
        """ generated source for method substituteLiteral """
        if isinstance(literal, (GdlDistinct, )):
            return cls.substituteDistinct(literal, theta)
        elif isinstance(literal, (GdlNot, )):
            return substituteNot(literal, theta)
        elif isinstance(literal, (GdlOr, )):
            return substituteOr(literal, theta)
        else:
            return substituteSentence(literal, theta)

    @classmethod
    def substituteNot(cls, not_, theta):
        """ generated source for method substituteNot """
        if not_.isGround():
            return not_
        else:
            return GdlPool.getNot(body)

    @classmethod
    def substituteOr(cls, or_, theta):
        """ generated source for method substituteOr """
        if or_.isGround():
            return or_
        else:
            while i < or_.arity():
                disjuncts.add(cls.substituteLiteral(or_.get(i), theta))
                i += 1
            return GdlPool.getOr(disjuncts)

    @classmethod
    def substituteProposition(cls, proposition, theta):
        """ generated source for method substituteProposition """
        return proposition

    @classmethod
    def substituteRelation(cls, relation, theta):
        """ generated source for method substituteRelation """
        if relation.isGround():
            return relation
        else:
            while i < relation.arity():
                body.add(substituteTerm(relation.get(i), theta))
                i += 1
            return GdlPool.getRelation(name, body)

    @classmethod
    def substituteSentence(cls, sentence, theta):
        """ generated source for method substituteSentence """
        if isinstance(sentence, (GdlProposition, )):
            return cls.substituteProposition(sentence, theta)
        else:
            return cls.substituteRelation(sentence, theta)

    @classmethod
    def substituteTerm(cls, term, theta):
        """ generated source for method substituteTerm """
        if isinstance(term, (GdlConstant, )):
            return cls.substituteConstant(term, theta)
        elif isinstance(term, (GdlVariable, )):
            return substituteVariable(term, theta)
        else:
            return cls.substituteFunction(term, theta)

    @classmethod
    def substituteVariable(cls, variable, theta):
        """ generated source for method substituteVariable """
        if not theta.contains(variable):
            return variable
        else:
            while not (betterResult = cls.substituteTerm(result, theta)) == result:
                result = betterResult
            theta.put(variable, result)
            return result

    @classmethod
    def substituteRule(cls, rule, theta):
        """ generated source for method substituteRule """
        head = cls.substitute(rule.getHead(), theta)
        body = ArrayList()
        for literal in rule.getBody():
            body.add(cls.substituteLiteral(literal, theta))
        return GdlPool.getRule(head, body)

