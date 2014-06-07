#!/usr/bin/env python
""" generated source for module PlayerReceivedMessageEvent """
# package: org.ggp.base.player.event
import org.ggp.base.util.observer.Event

class PlayerReceivedMessageEvent(Event):
    """ generated source for class PlayerReceivedMessageEvent """
    message = str()

    def __init__(self, message):
        """ generated source for method __init__ """
        super(PlayerReceivedMessageEvent, self).__init__()
        self.message = message

    def getMessage(self):
        """ generated source for method getMessage """
        return self.message

