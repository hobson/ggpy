#!/usr/bin/env python
""" generated source for module GamerUnrecognizedMatchEvent """
# package: org.ggp.base.player.gamer.event
import org.ggp.base.util.observer.Event

class GamerUnrecognizedMatchEvent(Event):
    """ generated source for class GamerUnrecognizedMatchEvent """
    matchId = str()

    def __init__(self, matchId):
        """ generated source for method __init__ """
        super(GamerUnrecognizedMatchEvent, self).__init__()
        self.matchId = matchId

    def getMatchId(self):
        """ generated source for method getMatchId """
        return self.matchId

