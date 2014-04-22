#!/usr/bin/env python
""" generated source for module GdlVisitor """
# package: org.ggp.base.util.gdl
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
#  * A visitor for Gdl objects. The GdlVisitors class has methods for going
#  * through a Gdl object or collection thereof and applying the visitor methods
#  * to all relevant Gdl objects.
#  *
#  * This visitor uses the adapter design pattern, providing empty implementations
#  * of each method so subclasses need only implement the relevant methods.
#  *
#  * @author Alex Landau
#  
class GdlVisitor(object):
    """ generated source for class GdlVisitor """
    def visitGdl(self, gdl):
        """ generated source for method visitGdl """
        #  Do nothing; override in a subclass to do something.

    def visitTerm(self, term):
        """ generated source for method visitTerm """
        #  Do nothing; override in a subclass to do something.

    def visitConstant(self, constant):
        """ generated source for method visitConstant """
        #  Do nothing; override in a subclass to do something.

    def visitVariable(self, variable):
        """ generated source for method visitVariable """
        #  Do nothing; override in a subclass to do something.

    def visitFunction(self, function_):
        """ generated source for method visitFunction """
        #  Do nothing; override in a subclass to do something.

    def visitLiteral(self, literal):
        """ generated source for method visitLiteral """
        #  Do nothing; override in a subclass to do something.

    def visitSentence(self, sentence):
        """ generated source for method visitSentence """
        #  Do nothing; override in a subclass to do something.

    def visitRelation(self, relation):
        """ generated source for method visitRelation """
        #  Do nothing; override in a subclass to do something.

    def visitProposition(self, proposition):
        """ generated source for method visitProposition """
        #  Do nothing; override in a subclass to do something.

    def visitNot(self, not_):
        """ generated source for method visitNot """
        #  Do nothing; override in a subclass to do something.

    def visitDistinct(self, distinct):
        """ generated source for method visitDistinct """
        #  Do nothing; override in a subclass to do something.

    def visitOr(self, or_):
        """ generated source for method visitOr """
        #  Do nothing; override in a subclass to do something.

    def visitRule(self, rule):
        """ generated source for method visitRule """
        #  Do nothing; override in a subclass to do something.

