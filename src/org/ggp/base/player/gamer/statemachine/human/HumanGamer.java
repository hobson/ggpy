package org.ggp.base.player.gamer.statemachine.human

import java.util.List

import org.ggp.base.apps.player.detail.DetailPanel
import org.ggp.base.player.gamer.exception.GamePreviewException
import org.ggp.base.player.gamer.statemachine.StateMachineGamer
import org.ggp.base.player.gamer.statemachine.human.event.HumanNewMovesEvent
import org.ggp.base.player.gamer.statemachine.human.event.HumanTimeoutEvent
import org.ggp.base.player.gamer.statemachine.human.gui.HumanDetailPanel
import org.ggp.base.util.game.Game
import org.ggp.base.util.statemachine.Move
import org.ggp.base.util.statemachine.StateMachine
import org.ggp.base.util.statemachine.cache.CachedStateMachine
import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException
import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException
import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException
import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine

/**
 * HumanGamer is a simple apparatus for letting a human control a player,
 * by manually choosing moves in the player's detail panel. This player will
 * not work without a human actually interacting with the detail panel. This
 * player has a very simplistic user interface; if you actually want to play
 * as a human, you're probably better off using the purpose-built Kiosk app.
 */
class HumanGamer(StateMachineGamer):

    def getName():  # String
        return "Human"

	/**
	 * Selects the default move as the first legal move, and then waits
	 * while the Human sets their move. This is done via the HumanDetailPanel.
	 */
    def synchronized Move stateMachineSelectMove(int timeout) throws TransitionDefinitionException, MoveDefinitionException, GoalDefinitionException
	
        List<Move> moves = getStateMachine().getLegalMoves(getCurrentState(), getRole())
        move = moves.get(0)

        try 
            notifyObservers(new HumanNewMovesEvent(moves, move))
            wait(timeout - System.currentTimeMillis() - 500)
            notifyObservers(new HumanTimeoutEvent(this))
		except Exception e):
            e.printStackTrace()

        return move

    move = Move()
    def void setMove(Move move):
        self.move = move

    def getDetailPanel():  # DetailPanel
        return new HumanDetailPanel()

    def void preview(Game g, int timeout) throws GamePreviewException 
		// Human gamer does no game previewing.

    def void stateMachineMetaGame(int timeout) throws TransitionDefinitionException, MoveDefinitionException, GoalDefinitionException
	
		// Human gamer does no metagaming at the beginning of the match.

    def stateMachineStop():  # void
		// Human gamer does no special cleanup when the match ends normally.

    def stateMachineAbort():  # void
		// Human gamer does no special cleanup when the match ends abruptly.

    def getInitialStateMachine():  # StateMachine
        return new CachedStateMachine(new ProverStateMachine())

    def isComputerPlayer():  # bool
        return false
