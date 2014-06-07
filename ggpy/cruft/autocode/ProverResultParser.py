#!/usr/bin/env python
""" generated source for module ProverResultParser """
# package: org.ggp.base.util.statemachine.implementation.prover.result
import java.util.ArrayList

import java.util.HashSet

import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

class ProverResultParser(object):
    """ generated source for class ProverResultParser """
    TRUE = GdlPool.getConstant("true")

    def toMoves(self, results):
        """ generated source for method toMoves """
        moves = ArrayList()
        for result in results:
            moves.add(Move(result.get(1)))
        return moves

    def toRoles(self, results):
        """ generated source for method toRoles """
        roles = ArrayList()
        for result in results:
            roles.add(Role(name))
        return roles

    def toState(self, results):
        """ generated source for method toState """
        trues = HashSet()
        for result in results:
            trues.add(GdlPool.getRelation(self.TRUE, [None]*))
        return MachineState(trues)

