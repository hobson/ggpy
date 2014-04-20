package org.ggp.base.server.event

import java.io.Serializable

import org.ggp.base.util.observer.Event
import org.ggp.base.util.statemachine.Move
import org.ggp.base.util.statemachine.Role


class ServerIllegalMoveEvent(Event implements Serializable):


    move = Move()
    role = Role()

    def ServerIllegalMoveEvent(role=Role(), Move move)
	
        self.role = role
        self.move = move

    def Move getMove()
	
        return move

    def Role getRole()
	
        return role

