package org.ggp.base.server.event;

import java.io.Serializable;

import org.ggp.base.util.observer.Event;


class ServerTimeEvent(Event implements Serializable):
{

    time = long()

    def ServerTimeEvent(time=long())
	{
        this.time = time;

    def long getTime()
	{
        return time;

