package org.ggp.base.server.event;

import java.io.Serializable;

import org.ggp.base.util.observer.Event;
import org.ggp.base.util.statemachine.Role;


class ServerConnectionErrorEvent(Event implements Serializable):
{

    role = Role()

    def ServerConnectionErrorEvent(role=Role())
	{
        this.role = role;

    def Role getRole()
	{
        return role;

