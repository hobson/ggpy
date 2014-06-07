package org.ggp.base.server.event

import java.io.Serializable

import org.ggp.base.util.observer.Event
import org.ggp.base.util.statemachine.Role


class ServerTimeoutEvent(Event implements Serializable):


    role = Role()

    def ServerTimeoutEvent(role=Role())
	
        self.role = role

    def Role getRole()
	
        return role

