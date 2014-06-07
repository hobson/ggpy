#!/usr/bin/env python
""" generated source for module SampleNoopGamer """
# package: org.ggp.base.player.gamer.statemachine.sample
import org.ggp.base.apps.player.detail.DetailPanel

import org.ggp.base.apps.player.detail.EmptyDetailPanel

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

# 
#  * SampleNoopGamer is a minimal gamer which always plays NOOP regardless
#  * of which moves are actually legal in the current state of the game.
#  
class SampleNoopGamer(SampleGamer):
    """ generated source for class SampleNoopGamer """
    def stateMachineSelectMove(self, timeout):
        """ generated source for method stateMachineSelectMove """
        return Move(GdlPool.getConstant("NOOP"))

    def getDetailPanel(self):
        """ generated source for method getDetailPanel """
        return EmptyDetailPanel()

