#!/usr/bin/env python
""" generated source for module DistinctAndNotMover """
# package: org.ggp.base.util.gdl.transforms
import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlVariable

import com.google.common.collect.Lists

import com.google.common.collect.Sets

# 
#  * As a GDL transformer, this class takes in a GDL description of a game,
#  * transforms it in some way, and outputs a new GDL descriptions of a game
#  * which is functionally equivalent to the original game.
#  *
#  * The AimaProver does not correctly apply "distinct" literals in rules if
#  * they have not yet been bound. (See test_distinct_beginning_rule.kif for
#  * an example where this comes up.) The same is true for "not" literals.
#  * This transformation moves "distinct" and "not" literals later in the
#  * rule, so they always appear after sentence literals have defined those
#  * variables.
#  *
#  * This should be applied to the input to the ProverStateMachine until this
#  * bug is fixed some other way.
#  
class DistinctAndNotMover(object):
    """ generated source for class DistinctAndNotMover """
    @classmethod
    def run(cls, oldRules):
        """ generated source for method run """
        oldRules = DeORer.run(oldRules)
        newRules = Lists.newArrayListWithCapacity(len(oldRules))
        for gdl in oldRules:
            if isinstance(gdl, (GdlRule, )):
                newRules.add(reorderRule(rule))
            else:
                newRules.add(gdl)
        return newRules

    @classmethod
    def reorderRule(cls, oldRule):
        """ generated source for method reorderRule """
        newBody = Lists.newArrayList(oldRule.getBody())
        rearrangeDistinctsAndNots(newBody)
        return GdlPool.getRule(oldRule.getHead(), newBody)

    @classmethod
    def rearrangeDistinctsAndNots(cls, ruleBody):
        """ generated source for method rearrangeDistinctsAndNots """
        oldIndex = findDistinctOrNotToMoveIndex(ruleBody)
        while oldIndex != None:
            ruleBody.remove(int(oldIndex))
            reinsertLiteralInRightPlace(ruleBody, literalToMove)
            oldIndex = findDistinctOrNotToMoveIndex(ruleBody)

    # Returns null if no distincts have to be moved.
    @classmethod
    def findDistinctOrNotToMoveIndex(cls, ruleBody):
        """ generated source for method findDistinctOrNotToMoveIndex """
        setVars = Sets.newHashSet()
        i = 0
        while i < len(ruleBody):
            if isinstance(literal, (GdlSentence, )):
                setVars.addAll(GdlUtils.getVariables(literal))
            elif isinstance(literal, (GdlDistinct, )) or isinstance(literal, (GdlNot, )):
                if not allVarsInLiteralAlreadySet(literal, setVars):
                    return i
            i += 1
        return None

    @classmethod
    def reinsertLiteralInRightPlace(cls, ruleBody, literalToReinsert):
        """ generated source for method reinsertLiteralInRightPlace """
        setVars = Sets.newHashSet()
        i = 0
        while i < len(ruleBody):
            if isinstance(literal, (GdlSentence, )):
                setVars.addAll(GdlUtils.getVariables(literal))
                if allVarsInLiteralAlreadySet(literalToReinsert, setVars):
                    ruleBody.add(i + 1, literalToReinsert)
                    return
            i += 1

    @classmethod
    def allVarsInLiteralAlreadySet(cls, literal, setVars):
        """ generated source for method allVarsInLiteralAlreadySet """
        varsInLiteral = GdlUtils.getVariables(literal)
        for varInLiteral in varsInLiteral:
            if not setVars.contains(varInLiteral):
                return False
        return True

