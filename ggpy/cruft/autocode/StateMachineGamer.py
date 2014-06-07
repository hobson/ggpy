#!/usr/bin/env python
""" generated source for module StateMachineGamer """
# package: org.ggp.base.player.gamer.statemachine
import java.util.ArrayList

import java.util.List

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.exception.AbortingException

import org.ggp.base.player.gamer.exception.MetaGamingException

import org.ggp.base.player.gamer.exception.MoveSelectionException

import org.ggp.base.player.gamer.exception.StoppingException

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

import org.ggp.base.util.statemachine.StateMachine

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

# 
#  * The base class for Gamers that rely on representing games as state machines.
#  * Almost every player should subclass this class, since it provides the common
#  * methods for interpreting the match history as transitions in a state machine,
#  * and for keeping an up-to-date view of the current state of the game.
#  *
#  * See @SimpleSearchLightGamer, @HumanGamer, and @RandomGamer for examples.
#  *
#  * @author evancox
#  * @author Sam
#  
class StateMachineGamer(Gamer):
    """ generated source for class StateMachineGamer """
    #  =====================================================================
    #  First, the abstract methods which need to be overriden by subclasses.
    #  These determine what state machine is used, what the gamer does during
    #  metagaming, and how the gamer selects moves.
    # 
    #      * Defines which state machine this gamer will use.
    #      * @return
    #      
    def getInitialStateMachine(self):
        """ generated source for method getInitialStateMachine """

    # 
    #      * Defines the metagaming action taken by a player during the START_CLOCK
    #      * @param timeout time in milliseconds since the era when this function must return
    #      * @throws TransitionDefinitionException
    #      * @throws MoveDefinitionException
    #      * @throws GoalDefinitionException
    #      
    def stateMachineMetaGame(self, timeout):
        """ generated source for method stateMachineMetaGame """

    # 
    #      * Defines the algorithm that the player uses to select their move.
    #      * @param timeout time in milliseconds since the era when this function must return
    #      * @return Move - the move selected by the player
    #      * @throws TransitionDefinitionException
    #      * @throws MoveDefinitionException
    #      * @throws GoalDefinitionException
    #      
    def stateMachineSelectMove(self, timeout):
        """ generated source for method stateMachineSelectMove """

    # 
    #      * Defines any actions that the player takes upon the game cleanly ending.
    #      
    def stateMachineStop(self):
        """ generated source for method stateMachineStop """

    # 
    #      * Defines any actions that the player takes upon the game abruptly ending.
    #      
    def stateMachineAbort(self):
        """ generated source for method stateMachineAbort """

    #  =====================================================================
    #  Next, methods which can be used by subclasses to get information about
    #  the current state of the game, and tweak the state machine on the fly.
    # 
    # 	 * Returns the current state of the game.
    # 	 
    def getCurrentState(self):
        """ generated source for method getCurrentState """
        return currentState

    # 
    # 	 * Returns the role that this gamer is playing as in the game.
    # 	 
    def getRole(self):
        """ generated source for method getRole """
        return role

    # 
    # 	 * Returns the state machine.  This is used for calculating the next state and other operations, such as computing
    # 	 * the legal moves for all players, whether states are terminal, and the goal values of terminal states.
    # 	 
    def getStateMachine(self):
        """ generated source for method getStateMachine """
        return stateMachine

    # 
    #      * Cleans up the role, currentState and stateMachine. This should only be
    #      * used when a match is over, and even then only when you really need to
    #      * free up resources that the state machine has tied up. Currently, it is
    #      * only used in the Proxy, for players designed to run 24/7.
    #      
    def cleanupAfterMatch(self):
        """ generated source for method cleanupAfterMatch """
        role = None
        currentState = None
        stateMachine = None
        setMatch(None)
        setRoleName(None)

    # 
    #      * Switches stateMachine to newStateMachine, playing through the match
    #      * history to the current state so that currentState is expressed using
    #      * a MachineState generated by the new state machine.
    #      *
    #      * This is not done in a thread-safe fashion with respect to the rest of
    #      * the gamer, so be careful when using this method.
    #      *
    #      * @param newStateMachine the new state machine
    #      
    def switchStateMachine(self, newStateMachine):
        """ generated source for method switchStateMachine """
        try:
            #  Attempt to run through the game history in the new machine
            for nextMove in theMoveHistory:
                for theSentence in nextMove:
                    theJointMove.add(newStateMachine.getMoveFromTerm(theSentence))
                newCurrentState = newStateMachine.getNextStateDestructively(newCurrentState, theJointMove)
            #  Finally, switch over if everything went well.
            role = newRole
            currentState = newCurrentState
            stateMachine = newStateMachine
        except Exception as e:
            GamerLogger.log("GamePlayer", "Caught an exception while switching state machine!")
            GamerLogger.logStackTrace("GamePlayer", e)

    #  =====================================================================
    #  Finally, methods which are overridden with proper state-machine-based
    #  semantics. These basically wrap a state-machine-based view of the world
    #  around the ordinary metaGame() and selectMove() functions, calling the
    #  new stateMachineMetaGame() and stateMachineSelectMove() functions after
    #  doing the state-machine-related book-keeping.
    # 
    # 	 * A wrapper function for stateMachineMetaGame. When the match begins, this
    # 	 * initializes the state machine and role using the match description, and
    # 	 * then calls stateMachineMetaGame.
    # 	 
    def metaGame(self, timeout):
        """ generated source for method metaGame """
        try:
            stateMachine = self.getInitialStateMachine()
            stateMachine.initialize(getMatch().getGame().getRules())
            currentState = stateMachine.getInitialState()
            role = stateMachine.getRoleFromConstant(getRoleName())
            getMatch().appendState(currentState.getContents())
            self.stateMachineMetaGame(timeout)
        except Exception as e:
            GamerLogger.logStackTrace("GamePlayer", e)
            raise MetaGamingException(e)

    def selectMove(self, timeout):
        """ generated source for method selectMove """
        try:
            stateMachine.doPerMoveWork()
            if lastMoves != None:
                for sentence in lastMoves:
                    moves.add(stateMachine.getMoveFromTerm(sentence))
                currentState = stateMachine.getNextState(currentState, moves)
                getMatch().appendState(currentState.getContents())
            return self.stateMachineSelectMove(timeout).getContents()
        except Exception as e:
            GamerLogger.logStackTrace("GamePlayer", e)
            raise MoveSelectionException(e)

    def stop(self):
        """ generated source for method stop """
        try:
            stateMachine.doPerMoveWork()
            if lastMoves != None:
                for sentence in lastMoves:
                    moves.add(stateMachine.getMoveFromTerm(sentence))
                currentState = stateMachine.getNextState(currentState, moves)
                getMatch().appendState(currentState.getContents())
                getMatch().markCompleted(stateMachine.getGoals(currentState))
            self.stateMachineStop()
        except Exception as e:
            GamerLogger.logStackTrace("GamePlayer", e)
            raise StoppingException(e)

    def abort(self):
        """ generated source for method abort """
        try:
            self.stateMachineAbort()
        except Exception as e:
            GamerLogger.logStackTrace("GamePlayer", e)
            raise AbortingException(e)

    role = Role()
    currentState = MachineState()
    stateMachine = StateMachine()

