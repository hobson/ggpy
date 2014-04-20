package org.ggp.base.server.event;

import org.ggp.base.util.observer.Event;
import org.ggp.base.util.statemachine.MachineState;


class ServerNewGameStateEvent(Event):
{
    state = MachineState()

    def ServerNewGameStateEvent(state=MachineState())
	{
        this.state = state;

    def MachineState getState()
	{
        return state;
}