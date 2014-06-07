#!/usr/bin/env python
""" generated source for module TransitionDefinitionException """
# package: org.ggp.base.util.statemachine.exceptions
import java.util.List

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

@SuppressWarnings("serial")
class TransitionDefinitionException(Exception):
    """ generated source for class TransitionDefinitionException """
    moves = List()
    state = MachineState()

    def __init__(self, state, moves):
        """ generated source for method __init__ """
        super(TransitionDefinitionException, self).__init__()
        self.state = state
        self.moves = moves

    def getMoves(self):
        """ generated source for method getMoves """
        return self.moves

    def getState(self):
        """ generated source for method getState """
        return self.state

    def __str__(self):
        """ generated source for method toString """
        return "Transition is poorly defined for " + self.moves + " in " + self.state

