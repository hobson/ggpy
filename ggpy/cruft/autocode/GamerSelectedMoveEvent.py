#!/usr/bin/env python
""" generated source for module GamerSelectedMoveEvent """
# package: org.ggp.base.player.gamer.event
import java.util.List

import org.ggp.base.util.observer.Event

import org.ggp.base.util.statemachine.Move

class GamerSelectedMoveEvent(Event):
    """ generated source for class GamerSelectedMoveEvent """
    moves = List()
    selection = Move()
    time = long()

    def __init__(self, moves, selection, time):
        """ generated source for method __init__ """
        super(GamerSelectedMoveEvent, self).__init__()
        self.moves = moves
        self.selection = selection
        self.time = time

    def getMoves(self):
        """ generated source for method getMoves """
        return self.moves

    def getSelection(self):
        """ generated source for method getSelection """
        return self.selection

    def getTime(self):
        """ generated source for method getTime """
        return self.time

