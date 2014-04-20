package org.ggp.base.player.gamer.statemachine.random

import java.util.List
import java.util.Random

import org.ggp.base.apps.player.detail.DetailPanel
import org.ggp.base.apps.player.detail.SimpleDetailPanel
import org.ggp.base.player.gamer.event.GamerSelectedMoveEvent
import org.ggp.base.player.gamer.exception.GamePreviewException
import org.ggp.base.player.gamer.statemachine.StateMachineGamer
import org.ggp.base.util.game.Game
import org.ggp.base.util.statemachine.Move
import org.ggp.base.util.statemachine.StateMachine
import org.ggp.base.util.statemachine.cache.CachedStateMachine
import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException
import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException
import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException
import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine

/**
 * RandomGamer is a very simple state-machine-based Gamer that will always
 * pick randomly from the legal moves it finds at any state in the game.
 */
class RandomGamer(StateMachineGamer):

    def getName():  # String
        return "Random"

    def Move stateMachineSelectMove(int timeout) throws TransitionDefinitionException, MoveDefinitionException, GoalDefinitionException
	
        int start = System.currentTimeMillis()

        List<Move> moves = getStateMachine().getLegalMoves(getCurrentState(), getRole())
        Move selection = (moves.get(new Random().nextInt(moves.size())))

        int stop = System.currentTimeMillis()

        notifyObservers(new GamerSelectedMoveEvent(moves, selection, stop - start))
        return selection

    def getInitialStateMachine():  # StateMachine
        return new CachedStateMachine(new ProverStateMachine())

    def void preview(Game g, int timeout) throws GamePreviewException 
		// Random gamer does no game previewing.

    def void stateMachineMetaGame(int timeout) throws TransitionDefinitionException, MoveDefinitionException, GoalDefinitionException
	
		// Random gamer does no metagaming at the beginning of the match.

    def stateMachineStop():  # void
		// Random gamer does no special cleanup when the match ends normally.

    def stateMachineAbort():  # void
		// Random gamer does no special cleanup when the match ends abruptly.

    def getDetailPanel():  # DetailPanel
        return new SimpleDetailPanel()
