package org.ggp.base.player.gamer.statemachine.human.event

import java.util.Collections
import java.util.Comparator
import java.util.List

import org.ggp.base.util.observer.Event
import org.ggp.base.util.statemachine.Move


class HumanNewMovesEvent(Event):


    private final List<Move> moves
    selection = Move()

    def HumanNewMovesEvent(List<Move> moves, Move selection)
	
	    Collections.sort(moves, new Comparator<Move>()@Override
	    def int compare(Move o1, Move o2) return o1.toString().compareTo(o2.toString());}})
        self.moves = moves
        self.selection = selection

    def List<Move> getMoves()
	
        return moves

    def Move getSelection()
	
        return selection

