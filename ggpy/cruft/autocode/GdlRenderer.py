#!/usr/bin/env python
""" generated source for module GdlRenderer """
# package: org.ggp.base.util.gdl.scrambler
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

# 
#  * A renderer for Gdl objects. On its own, this class renders a Gdl object
#  * in the way you'd expect. It can be subclassed to override particular parts
#  * of the rendering scheme; for example, to render GdlConstants scrambled via
#  * a mapping.
#  *
#  * TODO(schreib): Would it ever make sense for this to replace the regular
#  * toString methods in the Gdl objects?
#  *
#  * TODO(schreib): What is the relationship between this and the GdlVisitor
#  * framework that Alex put together? Can they be combined?
#  *
#  * @author Sam Schreiber
#  
class GdlRenderer(object):
    """ generated source for class GdlRenderer """
    def renderGdl(self, gdl):
        """ generated source for method renderGdl """
        if isinstance(gdl, (GdlTerm, )):
            return renderTerm(gdl)
        elif isinstance(gdl, (GdlLiteral, )):
            return renderLiteral(gdl)
        elif isinstance(gdl, (GdlRule, )):
            return renderRule(gdl)
        else:
            raise RuntimeException("Unexpected Gdl type " + gdl.__class__)

    def renderTerm(self, term):
        """ generated source for method renderTerm """
        if isinstance(term, (GdlConstant, )):
            return renderConstant(term)
        elif isinstance(term, (GdlVariable, )):
            return renderVariable(term)
        elif isinstance(term, (GdlFunction, )):
            return renderFunction(term)
        else:
            raise RuntimeException("Unexpected GdlTerm type " + term.__class__)

    def renderSentence(self, sentence):
        """ generated source for method renderSentence """
        if isinstance(sentence, (GdlProposition, )):
            return renderProposition(sentence)
        elif isinstance(sentence, (GdlRelation, )):
            return renderRelation(sentence)
        else:
            raise RuntimeException("Unexpected GdlSentence type " + sentence.__class__)

    def renderLiteral(self, literal):
        """ generated source for method renderLiteral """
        if isinstance(literal, (GdlSentence, )):
            return self.renderSentence(literal)
        elif isinstance(literal, (GdlNot, )):
            return renderNot(literal)
        elif isinstance(literal, (GdlOr, )):
            return renderOr(literal)
        elif isinstance(literal, (GdlDistinct, )):
            return renderDistinct(literal)
        else:
            raise RuntimeException("Unexpected GdlLiteral type " + literal.__class__)

    def renderConstant(self, constant):
        """ generated source for method renderConstant """
        return constant.__str__()

    def renderVariable(self, variable):
        """ generated source for method renderVariable """
        return variable.__str__()

    def renderFunction(self, function_):
        """ generated source for method renderFunction """
        sb = StringBuilder()
        sb.append("( " + self.renderConstant(function_.__name__) + " ")
        for term in function_.getBody():
            sb.append(self.renderTerm(term) + " ")
        sb.append(")")
        return sb.__str__()

    def renderRelation(self, relation):
        """ generated source for method renderRelation """
        sb = StringBuilder()
        sb.append("( " + self.renderConstant(relation.__name__) + " ")
        for term in relation.getBody():
            sb.append(self.renderTerm(term) + " ")
        sb.append(")")
        return sb.__str__()

    def renderProposition(self, proposition):
        """ generated source for method renderProposition """
        return self.renderConstant(proposition.__name__)

    def renderNot(self, not_):
        """ generated source for method renderNot """
        return "( not " + self.renderLiteral(not_.getBody()) + " )"

    def renderDistinct(self, distinct):
        """ generated source for method renderDistinct """
        return "( distinct " + self.renderTerm(distinct.getArg1()) + " " + self.renderTerm(distinct.getArg2()) + " )"

    def renderOr(self, or_):
        """ generated source for method renderOr """
        sb = StringBuilder()
        sb.append("( or ")
        i = 0
        while i < or_.arity():
            sb.append(self.renderLiteral(or_.get(i)) + " ")
            i += 1
        sb.append(")")
        return sb.__str__()

    def renderRule(self, rule):
        """ generated source for method renderRule """
        sb = StringBuilder()
        sb.append("( <= " + self.renderSentence(rule.getHead()) + " ")
        for literal in rule.getBody():
            sb.append(self.renderLiteral(literal) + " ")
        sb.append(")")
        return sb.__str__()

