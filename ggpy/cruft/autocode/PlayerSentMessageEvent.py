#!/usr/bin/env python
""" generated source for module PlayerSentMessageEvent """
# package: org.ggp.base.player.event
import org.ggp.base.util.observer.Event

class PlayerSentMessageEvent(Event):
    """ generated source for class PlayerSentMessageEvent """
    message = str()

    def __init__(self, message):
        """ generated source for method __init__ """
        super(PlayerSentMessageEvent, self).__init__()
        self.message = message

    def getMessage(self):
        """ generated source for method getMessage """
        return self.message

