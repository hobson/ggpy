#!/usr/bin/env python
""" generated source for module HumanGamer """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.player.gamer.statemachine.human
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

# 
#  * HumanGamer is a simple apparatus for letting a human control a player,
#  * by manually choosing moves in the player's detail panel. This player will
#  * not work without a human actually interacting with the detail panel. This
#  * player has a very simplistic user interface; if you actually want to play
#  * as a human, you're probably better off using the purpose-built Kiosk app.
#  
class HumanGamer(StateMachineGamer):
    """ generated source for class HumanGamer """
    def getName(self):
        """ generated source for method getName """
        return "Human"

    # 
    # 	 * Selects the default move as the first legal move, and then waits
    # 	 * while the Human sets their move. This is done via the HumanDetailPanel.
    # 	 
    @synchronized
    def stateMachineSelectMove(self, timeout):
        """ generated source for method stateMachineSelectMove """
        moves = getStateMachine().getLegalMoves(getCurrentState(), getRole())
        move = moves.get(0)
        try:
            notifyObservers(HumanNewMovesEvent(moves, move))
            wait(timeout - System.currentTimeMillis() - 500)
            notifyObservers(HumanTimeoutEvent(self))
        except Exception as e:
            e.printStackTrace()
        return move

    move = Move()

    def setMove(self, move):
        """ generated source for method setMove """
        self.move = move

    def getDetailPanel(self):
        """ generated source for method getDetailPanel """
        return HumanDetailPanel()

    def preview(self, g, timeout):
        """ generated source for method preview """
        #  Human gamer does no game previewing.

    def stateMachineMetaGame(self, timeout):
        """ generated source for method stateMachineMetaGame """
        #  Human gamer does no metagaming at the beginning of the match.

    def stateMachineStop(self):
        """ generated source for method stateMachineStop """
        #  Human gamer does no special cleanup when the match ends normally.

    def stateMachineAbort(self):
        """ generated source for method stateMachineAbort """
        #  Human gamer does no special cleanup when the match ends abruptly.

    def getInitialStateMachine(self):
        """ generated source for method getInitialStateMachine """
        return CachedStateMachine(ProverStateMachine())

    def isComputerPlayer(self):
        """ generated source for method isComputerPlayer """
        return False

