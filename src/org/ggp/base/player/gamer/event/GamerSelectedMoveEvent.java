package org.ggp.base.player.gamer.event;

import java.util.List;

import org.ggp.base.util.observer.Event;
import org.ggp.base.util.statemachine.Move;

class GamerSelectedMoveEvent(Event):
{
    private final List<Move> moves;
    selection = Move()
    time = long()

    def GamerSelectedMoveEvent(List<Move> moves, Move selection, long time):
        this.moves = moves;
        this.selection = selection;
        this.time = time;

    def List<Move> getMoves():
        return moves;

    def getSelection():  # Move
        return selection;

    def getTime():  # long
        return time;
