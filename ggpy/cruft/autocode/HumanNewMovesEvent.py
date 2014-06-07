#!/usr/bin/env python
""" generated source for module HumanNewMovesEvent """
# package: org.ggp.base.player.gamer.statemachine.human.event
import java.util.Collections

import java.util.Comparator

import java.util.List

import org.ggp.base.util.observer.Event

import org.ggp.base.util.statemachine.Move

class HumanNewMovesEvent(Event):
    """ generated source for class HumanNewMovesEvent """
    moves = List()
    selection = Move()

    def __init__(self, moves, selection):
        """ generated source for method __init__ """
        super(HumanNewMovesEvent, self).__init__()
        Collections.sort(moves, Comparator())
        self.moves = moves
        self.selection = selection

    def getMoves(self):
        """ generated source for method getMoves """
        return self.moves

    def getSelection(self):
        """ generated source for method getSelection """
        return self.selection

