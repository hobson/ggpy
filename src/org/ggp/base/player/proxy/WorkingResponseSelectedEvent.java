package org.ggp.base.player.proxy

import org.ggp.base.util.observer.Event

class WorkingResponseSelectedEvent(Event):
    theResponse = String()

    def WorkingResponseSelectedEvent(String theResponse):
        self.theResponse = theResponse

    def String getWorkingResponse():
        return theResponse

