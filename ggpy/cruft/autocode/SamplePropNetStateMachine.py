#!/usr/bin/env python
""" generated source for module SamplePropNetStateMachine """
# package: org.ggp.base.util.statemachine.implementation.propnet
import java.util.ArrayList

import java.util.HashSet

import java.util.LinkedList

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.propnet.architecture.Component

import org.ggp.base.util.propnet.architecture.PropNet

import org.ggp.base.util.propnet.architecture.components.Proposition

import org.ggp.base.util.propnet.factory.PropNetFactory

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

import org.ggp.base.util.statemachine.StateMachine

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

import org.ggp.base.util.statemachine.implementation.prover.query.ProverQueryBuilder

@SuppressWarnings("unused")
class SamplePropNetStateMachine(StateMachine):
    """ generated source for class SamplePropNetStateMachine """
    #  The underlying proposition network  
    propNet = PropNet()

    #  The topological ordering of the propositions 
    ordering = List()

    #  The player roles 
    roles = List()

    # 
    #      * Initializes the PropNetStateMachine. You should compute the topological
    #      * ordering here. Additionally you may compute the initial state here, at
    #      * your discretion.
    #      
    def initialize(self, description):
        """ generated source for method initialize """
        self.propNet = PropNetFactory.create(description)
        self.roles = self.propNet.getRoles()
        self.ordering = getOrdering()

    # 
    # 	 * Computes if the state is terminal. Should return the value
    # 	 * of the terminal proposition for the state.
    # 	 
    def isTerminal(self, state):
        """ generated source for method isTerminal """
        #  TODO: Compute whether the MachineState is terminal.
        return False

    # 
    # 	 * Computes the goal for a role in the current state.
    # 	 * Should return the value of the goal proposition that
    # 	 * is true for that role. If there is not exactly one goal
    # 	 * proposition true for that role, then you should throw a
    # 	 * GoalDefinitionException because the goal is ill-defined.
    # 	 
    def getGoal(self, state, role):
        """ generated source for method getGoal """
        #  TODO: Compute the goal for role in state.
        return -1

    # 
    # 	 * Returns the initial state. The initial state can be computed
    # 	 * by only setting the truth value of the INIT proposition to true,
    # 	 * and then computing the resulting state.
    # 	 
    def getInitialState(self):
        """ generated source for method getInitialState """
        #  TODO: Compute the initial state.
        return None

    # 
    # 	 * Computes the legal moves for role in state.
    # 	 
    def getLegalMoves(self, state, role):
        """ generated source for method getLegalMoves """
        #  TODO: Compute legal moves.
        return None

    # 
    # 	 * Computes the next state given state and the list of moves.
    # 	 
    def getNextState(self, state, moves):
        """ generated source for method getNextState """
        #  TODO: Compute the next state.
        return None

    # 
    # 	 * This should compute the topological ordering of propositions.
    # 	 * Each component is either a proposition, logical gate, or transition.
    # 	 * Logical gates and transitions only have propositions as inputs.
    # 	 *
    # 	 * The base propositions and input propositions should always be exempt
    # 	 * from this ordering.
    # 	 *
    # 	 * The base propositions values are set from the MachineState that
    # 	 * operations are performed on and the input propositions are set from
    # 	 * the Moves that operations are performed on as well (if any).
    # 	 *
    # 	 * @return The order in which the truth values of propositions need to be set.
    # 	 
    def getOrdering(self):
        """ generated source for method getOrdering """
        #  List to contain the topological ordering.
        order = LinkedList()
        #  All of the components in the PropNet
        components = ArrayList(self.propNet.getComponents())
        #  All of the propositions in the PropNet.
        propositions = ArrayList(self.propNet.getPropositions())
        #  TODO: Compute the topological ordering.
        return order

    #  Already implemented for you 
    def getRoles(self):
        """ generated source for method getRoles """
        return self.roles

    #  Helper methods 
    # 
    # 	 * The Input propositions are indexed by (does ?player ?action).
    # 	 *
    # 	 * This translates a list of Moves (backed by a sentence that is simply ?action)
    # 	 * into GdlSentences that can be used to get Propositions from inputPropositions.
    # 	 * and accordingly set their values etc.  This is a naive implementation when coupled with
    # 	 * setting input values, feel free to change this for a more efficient implementation.
    # 	 *
    # 	 * @param moves
    # 	 * @return
    # 	 
    def toDoes(self, moves):
        """ generated source for method toDoes """
        doeses = ArrayList(len(moves))
        roleIndices = getRoleIndices()
        i = 0
        while i < len(self.roles):
            doeses.add(ProverQueryBuilder.toDoes(self.roles.get(i), moves.get(index)))
            i += 1
        return doeses

    # 
    # 	 * Takes in a Legal Proposition and returns the appropriate corresponding Move
    # 	 * @param p
    # 	 * @return a PropNetMove
    # 	 
    @classmethod
    def getMoveFromProposition(cls, p):
        """ generated source for method getMoveFromProposition """
        return Move(p.__name__.get(1))

    # 
    # 	 * Helper method for parsing the value of a goal proposition
    # 	 * @param goalProposition
    # 	 * @return the integer value of the goal proposition
    # 	 
    def getGoalValue(self, goalProposition):
        """ generated source for method getGoalValue """
        relation = goalProposition.__name__
        constant = relation.get(1)
        return Integer.parseInt(constant.__str__())

    # 
    # 	 * A Naive implementation that computes a PropNetMachineState
    # 	 * from the true BasePropositions.  This is correct but slower than more advanced implementations
    # 	 * You need not use this method!
    # 	 * @return PropNetMachineState
    # 	 
    def getStateFromBase(self):
        """ generated source for method getStateFromBase """
        contents = HashSet()
        for p in propNet.getBasePropositions().values():
            p.setValue(p.getSingleInput().getValue())
            if p.getValue():
                contents.add(p.__name__)
        return MachineState(contents)

