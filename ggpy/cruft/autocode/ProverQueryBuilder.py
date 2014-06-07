#!/usr/bin/env python
""" generated source for module ProverQueryBuilder """
# package: org.ggp.base.util.statemachine.implementation.prover.query
import java.util.HashSet

import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

class ProverQueryBuilder(object):
    """ generated source for class ProverQueryBuilder """
    DOES = GdlPool.getConstant("does")
    GOAL = GdlPool.getConstant("goal")
    INIT_QUERY = GdlPool.getRelation(GdlPool.getConstant("init"), [None]*)
    LEGAL = GdlPool.getConstant("legal")
    NEXT_QUERY = GdlPool.getRelation(GdlPool.getConstant("next"), [None]*)
    ROLE_QUERY = GdlPool.getRelation(GdlPool.getConstant("role"), [None]*)
    TERMINAL_QUERY = GdlPool.getProposition(GdlPool.getConstant("terminal"))
    VARIABLE = GdlPool.getVariable("?x")

    @classmethod
    @overloaded
    def getContext(cls, state):
        """ generated source for method getContext """
        return state.getContents()

    @classmethod
    @getContext.register(object, MachineState, List, List)
    def getContext_0(cls, state, roles, moves):
        """ generated source for method getContext_0 """
        context = HashSet(state.getContents())
        i = 0
        while i < len(roles):
            context.add(toDoes(roles.get(i), moves.get(i)))
            i += 1
        return context

    @classmethod
    def getGoalQuery(cls, role):
        """ generated source for method getGoalQuery """
        return GdlPool.getRelation(cls.GOAL, [None]*)

    @classmethod
    def getInitQuery(cls):
        """ generated source for method getInitQuery """
        return cls.INIT_QUERY

    @classmethod
    def getLegalQuery(cls, role):
        """ generated source for method getLegalQuery """
        return GdlPool.getRelation(cls.LEGAL, [None]*)

    @classmethod
    def getNextQuery(cls):
        """ generated source for method getNextQuery """
        return cls.NEXT_QUERY

    @classmethod
    def getRoleQuery(cls):
        """ generated source for method getRoleQuery """
        return cls.ROLE_QUERY

    @classmethod
    def getTerminalQuery(cls):
        """ generated source for method getTerminalQuery """
        return cls.TERMINAL_QUERY

    @classmethod
    def toDoes(cls, role, move):
        """ generated source for method toDoes """
        return GdlPool.getRelation(cls.DOES, [None]*)

