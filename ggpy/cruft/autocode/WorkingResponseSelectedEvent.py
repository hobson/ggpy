#!/usr/bin/env python
""" generated source for module WorkingResponseSelectedEvent """
# package: org.ggp.base.player.proxy
import org.ggp.base.util.observer.Event

class WorkingResponseSelectedEvent(Event):
    """ generated source for class WorkingResponseSelectedEvent """
    theResponse = str()

    def __init__(self, theResponse):
        """ generated source for method __init__ """
        super(WorkingResponseSelectedEvent, self).__init__()
        self.theResponse = theResponse

    def getWorkingResponse(self):
        """ generated source for method getWorkingResponse """
        return self.theResponse

