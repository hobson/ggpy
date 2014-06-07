#!/usr/bin/env python
""" generated source for module SampleMonteCarloGamer """
# package: org.ggp.base.player.gamer.statemachine.sample
import java.util.List

import org.ggp.base.player.gamer.event.GamerSelectedMoveEvent

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.StateMachine

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

# 
#  * SampleMonteCarloGamer is a simple state-machine-based Gamer. It will use a
#  * pure Monte Carlo approach towards picking moves, doing simulations and then
#  * choosing the move that has the highest expected score. It should be slightly
#  * more challenging than the RandomGamer, while still playing reasonably fast.
#  *
#  * However, right now it isn't challenging at all. It's extremely mediocre, and
#  * doesn't even block obvious one-move wins. This is partially due to the speed
#  * of the default state machine (which is slow) and mostly due to the algorithm
#  * assuming that the opponent plays completely randomly, which is inaccurate.
#  *
#  * @author Sam Schreiber
#  
class SampleMonteCarloGamer(SampleGamer):
    """ generated source for class SampleMonteCarloGamer """
    # 
    # 	 * Employs a simple sample "Monte Carlo" algorithm.
    # 	 
    def stateMachineSelectMove(self, timeout):
        """ generated source for method stateMachineSelectMove """
        theMachine = getStateMachine()
        start = System.currentTimeMillis()
        finishBy = timeout - 1000
        moves = theMachine.getLegalMoves(getCurrentState(), getRole())
        selection = moves.get(0)
        if len(moves) > 1:
            #  Perform depth charges for each candidate move, and keep track
            #  of the total score and total attempts accumulated for each move.
            while True:
                if System.currentTimeMillis() > finishBy:
                    break
                moveTotalPoints[i] += theScore
                moveTotalAttempts[i] += 1
                i = (i + 1) % len(moves)
            #  Compute the expected score for each move.
            while i < len(moves):
                moveExpectedPoints[i] = float(moveTotalPoints[i]) / moveTotalAttempts[i]
                i += 1
            #  Find the move with the best expected score.
            while i < len(moves):
                if moveExpectedPoints[i] > bestMoveScore:
                    bestMoveScore = moveExpectedPoints[i]
                    bestMove = i
                i += 1
            selection = moves.get(bestMove)
        stop = System.currentTimeMillis()
        notifyObservers(GamerSelectedMoveEvent(moves, selection, stop - start))
        return selection

    depth = [None]*1

    def performDepthChargeFromMove(self, theState, myMove):
        """ generated source for method performDepthChargeFromMove """
        theMachine = getStateMachine()
        try:
            return theMachine.getGoal(finalState, getRole())
        except Exception as e:
            e.printStackTrace()
            return 0

