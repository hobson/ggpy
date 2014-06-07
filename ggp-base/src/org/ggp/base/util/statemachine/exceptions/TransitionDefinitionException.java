package org.ggp.base.util.statemachine.exceptions

import java.util.List

import org.ggp.base.util.statemachine.MachineState
import org.ggp.base.util.statemachine.Move


class TransitionDefinitionException(Exception):


    private final List<Move> moves
    state = MachineState()

    def TransitionDefinitionException(state=MachineState(), List<Move> moves)
	
        self.state = state
        self.moves = moves

    def List<Move> getMoves()
	
        return moves

    def MachineState getState()
	
        return state

    def String toString()
	
        return "Transition is poorly defined for " + moves + " in " + state

