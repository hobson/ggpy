#!/usr/bin/env python
""" generated source for module StateMachine """
# package: org.ggp.base.util.statemachine
import java.util.ArrayList

import java.util.HashMap

import java.util.LinkedList

import java.util.List

import java.util.Map

import java.util.Random

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

# 
#  * Provides the base class for all state machine implementations.
#  
class StateMachine(object):
    """ generated source for class StateMachine """
    #  ============================================
    #           Stubs for implementations
    #  ============================================
    #   The following methods are required for a valid
    #  state machine implementation.
    # 
    # 	 * Initializes the StateMachine to describe the given game rules.
    # 	 * <p>
    # 	 * This method should only be called once, and it should be called before any
    # 	 
    def initialize(self, description):
        """ generated source for method initialize """

    # 
    #      * Returns the goal value for the given role in the given state. Goal values
    #      * are always between 0 and 100.
    #      *
    #      * @throws GoalDefinitionException if there is no goal value or more than one
    #      * goal value for the given role in the given state. If this occurs when this
    #      * is called on a terminal state, this indicates an error in either the game
    #      * description or the StateMachine implementation.
    #      
    def getGoal(self, state, role):
        """ generated source for method getGoal """

    # 
    #      * Returns true if and only if the given state is a terminal state (i.e. the
    #      * game is over).
    #      
    def isTerminal(self, state):
        """ generated source for method isTerminal """

    # 
    #      * Returns a list of the roles in the game, in the same order as they
    #      * were defined in the game description.
    #      * <p>
    #      * The result will be the same as calling {@link Role#computeRoles(List)}
    #      * on the game rules used to initialize this state machine.
    #      
    def getRoles(self):
        """ generated source for method getRoles """

    # 
    #      * Returns the initial state of the game.
    #      
    def getInitialState(self):
        """ generated source for method getInitialState """

    # 
    #      * Returns a list containing every move that is legal for the given role in the
    #      * given state.
    #      *
    #      * @throws MoveDefinitionException if the role has no legal moves. This indicates
    #      * an error in either the game description or the StateMachine implementation.
    #      
    #  TODO: There are philosophical reasons for this to return Set<Move> rather than List<Move>.
    def getLegalMoves(self, state, role):
        """ generated source for method getLegalMoves """

    # 
    #      * Returns the next state of the game given the current state and a joint move
    #      * list containing one move per role.
    #      *
    #      * @param moves A list containing one move per role. The moves should be
    #      * listed in the same order as roles are listed by {@link #getRoles()}.
    #      * @throws TransitionDefinitionException indicates an error in either the
    #      * game description or the StateMachine implementation.
    #      
    def getNextState(self, state, moves):
        """ generated source for method getNextState """

    #  The following methods are included in the abstract StateMachine base so
    #  implementations which use alternative Role/Move/State representations
    #  can look up/compute what some Gdl corresponds to in their representation.
    #  They are implemented for convenience, using the default ways of generating
    #  these objects, but they can be overridden to support machine-specific objects.
    def getMachineStateFromSentenceList(self, sentenceList):
        """ generated source for method getMachineStateFromSentenceList """
        return MachineState(sentenceList)

    def getRoleFromConstant(self, constant):
        """ generated source for method getRoleFromConstant """
        return Role(constant)

    def getMoveFromTerm(self, term):
        """ generated source for method getMoveFromTerm """
        return Move(term)

    #  ============================================
    #           Stubs for advanced methods
    #  ============================================
    # 
    #    The following methods have functioning stubs,
    #  which can be overridden with full-fledged versions
    #  as needed by state machines. Clients should assume
    #  the contracts for these methods hold, regardless
    #  of the state machine implementation they pick.
    #  Override this to perform some extra work (like trimming a cache) once per move.
    #      * <p>
    #      * CONTRACT: Should be called once per move.
    #      
    def doPerMoveWork(self):
        """ generated source for method doPerMoveWork """

    #  Override this to provide memory-saving destructive-next-state functionality.
    #      * <p>
    #      * CONTRACT: After calling this method, "state" should not be accessed.
    #      
    def getNextStateDestructively(self, state, moves):
        """ generated source for method getNextStateDestructively """
        return self.getNextState(state, moves)

    #  Override this to allow the state machine to be conditioned on a particular current state.
    #      * This means that the state machine will only handle portions of the game tree at and below
    #      * the given state; it no longer needs to properly handle earlier portions of the game tree.
    #      * This constraint can be used to optimize certain state machine implementations.
    #      * <p>
    #      * CONTRACT: After calling this method, the state machine never deals with a state that
    #      *           is not "theState" or one of its descendants in the game tree.
    #      
    def updateRoot(self, theState):
        """ generated source for method updateRoot """

    #  ============================================
    #    Implementations of convenience methods
    #  ============================================
    def getName(self):
        """ generated source for method getName """
        return self.__class__.getSimpleName()

    @overloaded
    def getLegalJointMoves(self, state):
        """ generated source for method getLegalJointMoves """
        legals = ArrayList()
        for role in getRoles():
            legals.add(self.getLegalMoves(state, role))
        crossProduct = ArrayList()
        crossProductLegalMoves(legals, crossProduct, LinkedList())
        return crossProduct

    @getLegalJointMoves.register(object, MachineState, Role, Move)
    def getLegalJointMoves_0(self, state, role, move):
        """ generated source for method getLegalJointMoves_0 """
        legals = ArrayList()
        for r in getRoles():
            if r == role:
                m.add(move)
                legals.add(m)
            else:
                legals.add(self.getLegalMoves(state, r))
        crossProduct = ArrayList()
        crossProductLegalMoves(legals, crossProduct, LinkedList())
        return crossProduct

    @overloaded
    def getNextStates(self, state):
        """ generated source for method getNextStates """
        nextStates = ArrayList()
        for move in getLegalJointMoves(state):
            nextStates.add(self.getNextState(state, move))
        return nextStates

    @getNextStates.register(object, MachineState, Role)
    def getNextStates_0(self, state, role):
        """ generated source for method getNextStates_0 """
        nextStates = HashMap()
        roleIndices = getRoleIndices()
        for moves in getLegalJointMoves(state):
            if not nextStates.containsKey(move):
                nextStates.put(move, ArrayList())
            nextStates.get(move).add(self.getNextState(state, moves))
        return nextStates

    def crossProductLegalMoves(self, legals, crossProduct, partial):
        """ generated source for method crossProductLegalMoves """
        if len(partial) == len(legals):
            crossProduct.add(ArrayList(partial))
        else:
            for move in legals.get(len(partial)):
                partial.addLast(move)
                self.crossProductLegalMoves(legals, crossProduct, partial)
                partial.removeLast()

    roleIndices = None

    def getRoleIndices(self):
        """ generated source for method getRoleIndices """
        if self.roleIndices == None:
            self.roleIndices = HashMap()
            while i < len(roles):
                self.roleIndices.put(roles.get(i), i)
                i += 1
        return self.roleIndices

    def getGoals(self, state):
        """ generated source for method getGoals """
        theGoals = ArrayList()
        for r in getRoles():
            theGoals.add(self.getGoal(state, r))
        return theGoals

    @overloaded
    def getRandomJointMove(self, state):
        """ generated source for method getRandomJointMove """
        random = ArrayList()
        for role in getRoles():
            random.add(getRandomMove(state, role))
        return random

    @getRandomJointMove.register(object, MachineState, Role, Move)
    def getRandomJointMove_0(self, state, role, move):
        """ generated source for method getRandomJointMove_0 """
        random = ArrayList()
        for r in getRoles():
            if r == role:
                random.add(move)
            else:
                random.add(getRandomMove(state, r))
        return random

    def getRandomMove(self, state, role):
        """ generated source for method getRandomMove """
        legals = self.getLegalMoves(state, role)
        return legals.get(Random().nextInt(len(legals)))

    @overloaded
    def getRandomNextState(self, state):
        """ generated source for method getRandomNextState """
        random = self.getRandomJointMove(state)
        return self.getNextState(state, random)

    @getRandomNextState.register(object, MachineState, Role, Move)
    def getRandomNextState_0(self, state, role, move):
        """ generated source for method getRandomNextState_0 """
        random = self.getRandomJointMove(state, role, move)
        return self.getNextState(state, random)

    def performDepthCharge(self, state, theDepth):
        """ generated source for method performDepthCharge """
        nDepth = 0
        while not self.isTerminal(state):
            nDepth += 1
            state = self.getNextStateDestructively(state, self.getRandomJointMove(state))
        if theDepth != None:
            theDepth[0] = nDepth
        return state

    def getAverageDiscountedScoresFromRepeatedDepthCharges(self, state, avgScores, avgDepth, discountFactor, repetitions):
        """ generated source for method getAverageDiscountedScoresFromRepeatedDepthCharges """
        avgDepth[0] = 0
        j = 0
        while len(avgScores):
            avgScores[j] = 0
            j += 1
        depth = [None]*1
        i = 0
        while i < repetitions:
            stateForCharge = self.performDepthCharge(stateForCharge, depth)
            avgDepth[0] += depth[0]
            while len(avgScores):
                avgScores[j] += self.getGoal(stateForCharge, self.getRoles().get(j)) * accumulatedDiscountFactor
                j += 1
            i += 1
        avgDepth[0] /= repetitions
        j = 0
        while len(avgScores):
            avgScores[j] /= repetitions
            j += 1

StateMachine.# 	 * other methods on the StateMachine.

