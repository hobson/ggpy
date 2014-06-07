#!/usr/bin/env python
""" generated source for module GamerNewMatchEvent """
# package: org.ggp.base.player.gamer.event
import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.match.Match

import org.ggp.base.util.observer.Event

class GamerNewMatchEvent(Event):
    """ generated source for class GamerNewMatchEvent """
    match = Match()
    roleName = GdlConstant()

    def __init__(self, match, roleName):
        """ generated source for method __init__ """
        super(GamerNewMatchEvent, self).__init__()
        self.match = match
        self.roleName = roleName

    def getMatch(self):
        """ generated source for method getMatch """
        return self.match

    def getRoleName(self):
        """ generated source for method getRoleName """
        return self.roleName

