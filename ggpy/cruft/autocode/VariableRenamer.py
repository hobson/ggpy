#!/usr/bin/env python
""" generated source for module VariableRenamer """
# package: org.ggp.base.util.prover.aima.renamer
import java.util.ArrayList

import java.util.HashMap

import java.util.List

import java.util.Map

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

class VariableRenamer(object):
    """ generated source for class VariableRenamer """
    nextName = int()

    def __init__(self):
        """ generated source for method __init__ """
        self.nextName = 0

    @overloaded
    def rename(self, rule):
        """ generated source for method rename """
        return renameRule(rule, HashMap())

    @rename.register(object, GdlSentence)
    def rename_0(self, sentence):
        """ generated source for method rename_0 """
        return renameSentence(sentence, HashMap())

    def renameConstant(self, constant, renamings):
        """ generated source for method renameConstant """
        return constant

    def renameDistinct(self, distinct, renamings):
        """ generated source for method renameDistinct """
        if distinct.isGround():
            return distinct
        else:
            return GdlPool.getDistinct(arg1, arg2)

    def renameFunction(self, function_, renamings):
        """ generated source for method renameFunction """
        if function_.isGround():
            return function_
        else:
            while i < function_.arity():
                body.add(renameTerm(function_.get(i), renamings))
                i += 1
            return GdlPool.getFunction(name, body)

    def renameLiteral(self, literal, renamings):
        """ generated source for method renameLiteral """
        if isinstance(literal, (GdlDistinct, )):
            return self.renameDistinct(literal, renamings)
        elif isinstance(literal, (GdlNot, )):
            return renameNot(literal, renamings)
        elif isinstance(literal, (GdlOr, )):
            return renameOr(literal, renamings)
        else:
            return renameSentence(literal, renamings)

    def renameNot(self, not_, renamings):
        """ generated source for method renameNot """
        if not_.isGround():
            return not_
        else:
            return GdlPool.getNot(body)

    def renameOr(self, or_, renamings):
        """ generated source for method renameOr """
        if or_.isGround():
            return or_
        else:
            while i < or_.arity():
                disjuncts.add(self.renameLiteral(or_.get(i), renamings))
                i += 1
            return GdlPool.getOr(disjuncts)

    def renameProposition(self, proposition, renamings):
        """ generated source for method renameProposition """
        return proposition

    def renameRelation(self, relation, renamings):
        """ generated source for method renameRelation """
        if relation.isGround():
            return relation
        else:
            while i < relation.arity():
                body.add(renameTerm(relation.get(i), renamings))
                i += 1
            return GdlPool.getRelation(name, body)

    def renameRule(self, rule, renamings):
        """ generated source for method renameRule """
        if rule.isGround():
            return rule
        else:
            while i < rule.arity():
                body.add(self.renameLiteral(rule.get(i), renamings))
                i += 1
            return GdlPool.getRule(head, body)

    def renameSentence(self, sentence, renamings):
        """ generated source for method renameSentence """
        if isinstance(sentence, (GdlProposition, )):
            return self.renameProposition(sentence, renamings)
        else:
            return self.renameRelation(sentence, renamings)

    def renameTerm(self, term, renamings):
        """ generated source for method renameTerm """
        if isinstance(term, (GdlConstant, )):
            return self.renameConstant(term, renamings)
        elif isinstance(term, (GdlVariable, )):
            return renameVariable(term, renamings)
        else:
            return self.renameFunction(term, renamings)

    def renameVariable(self, variable, renamings):
        """ generated source for method renameVariable """
        if not renamings.containsKey(variable):
            renamings.put(variable, newName)
        return renamings.get(variable)

