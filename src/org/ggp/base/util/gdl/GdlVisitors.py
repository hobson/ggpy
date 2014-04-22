#!/usr/bin/env python
""" generated source for module GdlVisitors """
# package: org.ggp.base.util.gdl
import java.util.Collection

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

class GdlVisitors(object):
    """ generated source for class GdlVisitors """
    # 
    # 	 * Visits the given Gdl object and any contained Gdl objects within
    # 	 * with the given GdlVisitor. For example, when called on a GdlRule,
    # 	 * the visitor's visitConstant function is called once for every
    # 	 * constant anywhere in the head or body of the rule.
    # 	 *
    # 	 * @author Alex Landau
    # 	 
    @classmethod
    @overloaded
    def visitAll(cls, gdl, visitor):
        """ generated source for method visitAll """
        visitor.visitGdl(gdl)
        if isinstance(gdl, (GdlTerm, )):
            visitTerm(gdl, visitor)
        elif isinstance(gdl, (GdlLiteral, )):
            visitLiteral(gdl, visitor)
        elif isinstance(gdl, (GdlRule, )):
            visitRule(gdl, visitor)
        else:
            raise RuntimeException("Unexpected Gdl type " + gdl.__class__)

    @classmethod
    @visitAll.register(object, Collection, GdlVisitor)
    def visitAll_0(cls, collection, visitor):
        """ generated source for method visitAll_0 """
        for gdl in collection:
            cls.visitAll(gdl, visitor)

    @classmethod
    def visitRule(cls, rule, visitor):
        """ generated source for method visitRule """
        visitor.visitRule(rule)
        cls.visitAll(rule.getHead(), visitor)
        cls.visitAll(rule.getBody(), visitor)

    @classmethod
    def visitLiteral(cls, literal, visitor):
        """ generated source for method visitLiteral """
        visitor.visitLiteral(literal)
        if isinstance(literal, (GdlSentence, )):
            visitSentence(literal, visitor)
        elif isinstance(literal, (GdlNot, )):
            visitNot(literal, visitor)
        elif isinstance(literal, (GdlOr, )):
            visitOr(literal, visitor)
        elif isinstance(literal, (GdlDistinct, )):
            visitDistinct(literal, visitor)
        else:
            raise RuntimeException("Unexpected GdlLiteral type " + literal.__class__)

    @classmethod
    def visitDistinct(cls, distinct, visitor):
        """ generated source for method visitDistinct """
        visitor.visitDistinct(distinct)
        cls.visitAll(distinct.getArg1(), visitor)
        cls.visitAll(distinct.getArg2(), visitor)

    @classmethod
    def visitOr(cls, or_, visitor):
        """ generated source for method visitOr """
        visitor.visitOr(or_)
        i = 0
        while i < or_.arity():
            cls.visitAll(or_.get(i), visitor)
            i += 1

    @classmethod
    def visitNot(cls, not_, visitor):
        """ generated source for method visitNot """
        visitor.visitNot(not_)
        cls.visitAll(not_.getBody(), visitor)

    @classmethod
    def visitSentence(cls, sentence, visitor):
        """ generated source for method visitSentence """
        visitor.visitSentence(sentence)
        if isinstance(sentence, (GdlProposition, )):
            visitProposition(sentence, visitor)
        elif isinstance(sentence, (GdlRelation, )):
            visitRelation(sentence, visitor)
        else:
            raise RuntimeException("Unexpected GdlSentence type " + sentence.__class__)

    @classmethod
    def visitRelation(cls, relation, visitor):
        """ generated source for method visitRelation """
        visitor.visitRelation(relation)
        cls.visitAll(relation.__name__, visitor)
        cls.visitAll(relation.getBody(), visitor)

    @classmethod
    def visitProposition(cls, proposition, visitor):
        """ generated source for method visitProposition """
        visitor.visitProposition(proposition)
        cls.visitAll(proposition.__name__, visitor)

    @classmethod
    def visitTerm(cls, term, visitor):
        """ generated source for method visitTerm """
        visitor.visitTerm(term)
        if isinstance(term, (GdlConstant, )):
            visitor.visitConstant(term)
        elif isinstance(term, (GdlVariable, )):
            visitor.visitVariable(term)
        elif isinstance(term, (GdlFunction, )):
            visitFunction(term, visitor)
        else:
            raise RuntimeException("Unexpected GdlTerm type " + term.__class__)

    @classmethod
    def visitFunction(cls, function_, visitor):
        """ generated source for method visitFunction """
        visitor.visitFunction(function_)
        cls.visitAll(function_.__name__, visitor)
        cls.visitAll(function_.getBody(), visitor)

