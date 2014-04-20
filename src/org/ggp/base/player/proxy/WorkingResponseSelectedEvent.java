package org.ggp.base.player.proxy;

import org.ggp.base.util.observer.Event;

class WorkingResponseSelectedEvent(Event):
    private String theResponse;

    public WorkingResponseSelectedEvent(String theResponse):
        this.theResponse = theResponse;
    }

    public String getWorkingResponse():
        return theResponse;
    }
}