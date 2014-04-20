package org.ggp.base.player.gamer.statemachine.sample;

import org.ggp.base.apps.player.detail.DetailPanel;
import org.ggp.base.apps.player.detail.SimpleDetailPanel;
import org.ggp.base.player.gamer.exception.GamePreviewException;
import org.ggp.base.player.gamer.statemachine.StateMachineGamer;
import org.ggp.base.util.game.Game;
import org.ggp.base.util.statemachine.StateMachine;
import org.ggp.base.util.statemachine.cache.CachedStateMachine;
import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException;
import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException;
import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException;
import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine;

/**
 * SampleGamer is a simplified version of the StateMachineGamer, dropping some
 * advanced functionality so the example gamers can be presented concisely.
 * This class implements 7 of the 8 core functions that need to be implemented
 * for any gamer.
 *
 * If you want to quickly create a gamer of your own, extend this class and
 * add the last core function : def Move stateMachineSelectMove(int timeout)
 */

def abstract class SampleGamer(StateMachineGamer):
{
    def void stateMachineMetaGame(int timeout) throws TransitionDefinitionException, MoveDefinitionException, GoalDefinitionException
	{
		// Sample gamers do no metagaming at the beginning of the match.



	/** This will currently return "SampleGamer"
	 * If you are working on : def abstract class MyGamer(SampleGamer):
	 * Then this function would return "MyGamer"
	 */
    def getName():  # String
        return getClass().getSimpleName();

	// This is the default State Machine
    def getInitialStateMachine():  # StateMachine
        return new CachedStateMachine(new ProverStateMachine());

	// This is the defaul Sample Panel
    def getDetailPanel():  # DetailPanel
        return new SimpleDetailPanel();



    def stateMachineStop():  # void
		// Sample gamers do no special cleanup when the match ends normally.

    def stateMachineAbort():  # void
		// Sample gamers do no special cleanup when the match ends abruptly.

    def void preview(Game g, int timeout) throws GamePreviewException {
		// Sample gamers do no game previewing.
}