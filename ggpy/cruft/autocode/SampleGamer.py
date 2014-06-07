#!/usr/bin/env python
""" generated source for module SampleGamer """
# package: org.ggp.base.player.gamer.statemachine.sample
import org.ggp.base.apps.player.detail.DetailPanel

import org.ggp.base.apps.player.detail.SimpleDetailPanel

import org.ggp.base.player.gamer.exception.GamePreviewException

import org.ggp.base.player.gamer.statemachine.StateMachineGamer

import org.ggp.base.util.game.Game

import org.ggp.base.util.statemachine.StateMachine

import org.ggp.base.util.statemachine.cache.CachedStateMachine

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine

# 
#  * SampleGamer is a simplified version of the StateMachineGamer, dropping some
#  * advanced functionality so the example gamers can be presented concisely.
#  * This class implements 7 of the 8 core functions that need to be implemented
#  * for any gamer.
#  *
#  * If you want to quickly create a gamer of your own, extend this class and
#  * add the last core function : public Move stateMachineSelectMove(long timeout)
#  
class SampleGamer(StateMachineGamer):
    """ generated source for class SampleGamer """
    def stateMachineMetaGame(self, timeout):
        """ generated source for method stateMachineMetaGame """
        #  Sample gamers do no metagaming at the beginning of the match.

    #  This will currently return "SampleGamer"
    # 	 * If you are working on : public abstract class MyGamer extends SampleGamer
    # 	 * Then this function would return "MyGamer"
    # 	 
    def getName(self):
        """ generated source for method getName """
        return getClass().getSimpleName()

    #  This is the default State Machine
    def getInitialStateMachine(self):
        """ generated source for method getInitialStateMachine """
        return CachedStateMachine(ProverStateMachine())

    #  This is the defaul Sample Panel
    def getDetailPanel(self):
        """ generated source for method getDetailPanel """
        return SimpleDetailPanel()

    def stateMachineStop(self):
        """ generated source for method stateMachineStop """
        #  Sample gamers do no special cleanup when the match ends normally.

    def stateMachineAbort(self):
        """ generated source for method stateMachineAbort """
        #  Sample gamers do no special cleanup when the match ends abruptly.

    def preview(self, g, timeout):
        """ generated source for method preview """
        #  Sample gamers do no game previewing.

