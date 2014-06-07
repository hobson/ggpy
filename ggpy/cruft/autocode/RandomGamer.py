#!/usr/bin/env python
""" generated source for module RandomGamer """
# package: org.ggp.base.player.gamer.statemachine.random
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

# 
#  * RandomGamer is a very simple state-machine-based Gamer that will always
#  * pick randomly from the legal moves it finds at any state in the game.
#  
class RandomGamer(StateMachineGamer):
    """ generated source for class RandomGamer """
    def getName(self):
        """ generated source for method getName """
        return "Random"

    def stateMachineSelectMove(self, timeout):
        """ generated source for method stateMachineSelectMove """
        start = System.currentTimeMillis()
        moves = getStateMachine().getLegalMoves(getCurrentState(), getRole())
        selection = (moves.get(Random().nextInt(len(moves))))
        stop = System.currentTimeMillis()
        notifyObservers(GamerSelectedMoveEvent(moves, selection, stop - start))
        return selection

    def getInitialStateMachine(self):
        """ generated source for method getInitialStateMachine """
        return CachedStateMachine(ProverStateMachine())

    def preview(self, g, timeout):
        """ generated source for method preview """
        #  Random gamer does no game previewing.

    def stateMachineMetaGame(self, timeout):
        """ generated source for method stateMachineMetaGame """
        #  Random gamer does no metagaming at the beginning of the match.

    def stateMachineStop(self):
        """ generated source for method stateMachineStop """
        #  Random gamer does no special cleanup when the match ends normally.

    def stateMachineAbort(self):
        """ generated source for method stateMachineAbort """
        #  Random gamer does no special cleanup when the match ends abruptly.

    def getDetailPanel(self):
        """ generated source for method getDetailPanel """
        return SimpleDetailPanel()

