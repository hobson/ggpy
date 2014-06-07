package org.ggp.base.server.event

import java.io.Serializable

import org.ggp.base.util.observer.Event


class ServerTimeEvent(Event implements Serializable):


    time = int()

    def ServerTimeEvent(time=int())
	
        self.time = time

    def int getTime()
	
        return time

