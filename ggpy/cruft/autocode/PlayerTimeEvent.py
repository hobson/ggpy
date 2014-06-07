#!/usr/bin/env python
""" generated source for module PlayerTimeEvent """
# package: org.ggp.base.player.event
import org.ggp.base.util.observer.Event

class PlayerTimeEvent(Event):
    """ generated source for class PlayerTimeEvent """
    time = long()

    def __init__(self, time):
        """ generated source for method __init__ """
        super(PlayerTimeEvent, self).__init__()
        self.time = time

    def getTime(self):
        """ generated source for method getTime """
        return self.time

