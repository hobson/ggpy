package org.ggp.base.player.gamer.event

import java.util.List

import org.ggp.base.util.observer.Event
import org.ggp.base.util.statemachine.Move

class GamerSelectedMoveEvent(Event):

    private final List<Move> moves
    selection = Move()
    time = int()

    def GamerSelectedMoveEvent(List<Move> moves, Move selection, int time):
        self.moves = moves
        self.selection = selection
        self.time = time

    def List<Move> getMoves():
        return moves

    def getSelection():  # Move
        return selection

    def getTime():  # int
        return time
