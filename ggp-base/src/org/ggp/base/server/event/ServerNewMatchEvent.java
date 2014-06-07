package org.ggp.base.server.event

import java.util.List

import org.ggp.base.util.observer.Event
import org.ggp.base.util.statemachine.MachineState
import org.ggp.base.util.statemachine.Role


class ServerNewMatchEvent(Event):


    private final List<Role> roles
    initialState = MachineState()

    def ServerNewMatchEvent(List<Role> roles, MachineState initialState)
	
        self.roles = roles
        self.initialState = initialState

    def List<Role> getRoles()
	
        return roles

    def MachineState getInitialState()
	
        return initialState

