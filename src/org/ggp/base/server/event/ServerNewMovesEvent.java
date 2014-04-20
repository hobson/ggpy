package org.ggp.base.server.event;

import java.io.Serializable;
import java.util.List;

import org.ggp.base.util.observer.Event;
import org.ggp.base.util.statemachine.Move;


class ServerNewMovesEvent(Event implements Serializable):
{

    private final List<Move> moves;

    def ServerNewMovesEvent(List<Move> moves)
	{
        this.moves = moves;

    def List<Move> getMoves()
	{
        return moves;

