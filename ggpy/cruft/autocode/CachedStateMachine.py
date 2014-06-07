#!/usr/bin/env python
""" generated source for module CachedStateMachine """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.statemachine.cache
import java.util.HashMap

import java.util.List

import java.util.Map

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

import org.ggp.base.util.statemachine.StateMachine

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

class CachedStateMachine(StateMachine):
    """ generated source for class CachedStateMachine """
    backingStateMachine = StateMachine()
    ttlCache = TtlCache()

    class Entry(object):
        """ generated source for class Entry """
        goals = Map()
        moves = Map()
        nexts = Map()
        terminal = bool()

        def __init__(self):
            """ generated source for method __init__ """
            self.goals = HashMap()
            self.moves = HashMap()
            self.nexts = HashMap()
            self.terminal = None

    def __init__(self, backingStateMachine):
        """ generated source for method __init__ """
        super(CachedStateMachine, self).__init__()
        self.backingStateMachine = backingStateMachine
        self.ttlCache = TtlCache(1)

    def getEntry(self, state):
        """ generated source for method getEntry """
        if not self.ttlCache.containsKey(state):
            self.ttlCache.put(state, self.Entry())
        return self.ttlCache.get(state)

    def getGoal(self, state, role):
        """ generated source for method getGoal """
        entry = self.getEntry(state)
        with lock_for_object(entry):
            if not entry.goals.containsKey(role):
                entry.goals.put(role, self.backingStateMachine.getGoal(state, role))
            return entry.goals.get(role)

    def getLegalMoves(self, state, role):
        """ generated source for method getLegalMoves """
        entry = self.getEntry(state)
        with lock_for_object(entry):
            if not entry.moves.containsKey(role):
                entry.moves.put(role, self.backingStateMachine.getLegalMoves(state, role))
            return entry.moves.get(role)

    def getNextState(self, state, moves):
        """ generated source for method getNextState """
        entry = self.getEntry(state)
        with lock_for_object(entry):
            if not entry.nexts.containsKey(moves):
                entry.nexts.put(moves, self.backingStateMachine.getNextState(state, moves))
            return entry.nexts.get(moves)

    def isTerminal(self, state):
        """ generated source for method isTerminal """
        entry = self.getEntry(state)
        with lock_for_object(entry):
            if entry.terminal == None:
                entry.terminal = self.backingStateMachine.isTerminal(state)
            return entry.terminal

    def doPerMoveWork(self):
        """ generated source for method doPerMoveWork """
        prune()

    def prune(self):
        """ generated source for method prune """
        self.ttlCache.prune()

    def initialize(self, description):
        """ generated source for method initialize """
        self.backingStateMachine.initialize(description)

    def getRoles(self):
        """ generated source for method getRoles """
        #  TODO(schreib): Should this be cached as well?
        return self.backingStateMachine.getRoles()

    def getInitialState(self):
        """ generated source for method getInitialState """
        #  TODO(schreib): Should this be cached as well?
        return self.backingStateMachine.getInitialState()

