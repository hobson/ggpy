#!/usr/bin/env python
""" generated source for module ProverStateMachine """
# package: org.ggp.base.util.statemachine.implementation.prover
import java.util.HashSet

import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.prover.Prover

import org.ggp.base.util.prover.aima.AimaProver

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

import org.ggp.base.util.statemachine.StateMachine

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

import org.ggp.base.util.statemachine.implementation.prover.query.ProverQueryBuilder

import org.ggp.base.util.statemachine.implementation.prover.result.ProverResultParser

class ProverStateMachine(StateMachine):
    """ generated source for class ProverStateMachine """
    initialState = MachineState()
    prover = Prover()
    roles = List()

    # 
    # 	 * Initialize must be called before using the StateMachine
    # 	 
    def __init__(self):
        """ generated source for method __init__ """
        super(ProverStateMachine, self).__init__()

    def initialize(self, description):
        """ generated source for method initialize """
        self.prover = AimaProver(description)
        self.roles = Role.computeRoles(description)
        self.initialState = computeInitialState()

    def computeInitialState(self):
        """ generated source for method computeInitialState """
        results = self.prover.askAll(ProverQueryBuilder.getInitQuery(), HashSet())
        return ProverResultParser().toState(results)

    def getGoal(self, state, role):
        """ generated source for method getGoal """
        results = self.prover.askAll(ProverQueryBuilder.getGoalQuery(role), ProverQueryBuilder.getContext(state))
        if len(results) != 1:
            GamerLogger.logError("StateMachine", "Got goal results of size: " + len(results) + " when expecting size one.")
            raise GoalDefinitionException(state, role)
        try:
            return Integer.parseInt(constant.__str__())
        except Exception as e:
            raise GoalDefinitionException(state, role)

    def getInitialState(self):
        """ generated source for method getInitialState """
        return self.initialState

    def getLegalMoves(self, state, role):
        """ generated source for method getLegalMoves """
        results = self.prover.askAll(ProverQueryBuilder.getLegalQuery(role), ProverQueryBuilder.getContext(state))
        if len(results) == 0:
            raise MoveDefinitionException(state, role)
        return ProverResultParser().toMoves(results)

    def getNextState(self, state, moves):
        """ generated source for method getNextState """
        results = self.prover.askAll(ProverQueryBuilder.getNextQuery(), ProverQueryBuilder.getContext(state, getRoles(), moves))
        for sentence in results:
            if not sentence.isGround():
                raise TransitionDefinitionException(state, moves)
        return ProverResultParser().toState(results)

    def getRoles(self):
        """ generated source for method getRoles """
        return self.roles

    def isTerminal(self, state):
        """ generated source for method isTerminal """
        return self.prover.prove(ProverQueryBuilder.getTerminalQuery(), ProverQueryBuilder.getContext(state))

