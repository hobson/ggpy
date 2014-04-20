package org.ggp.base.server.threads;

import java.util.List;
import java.util.Random;

import org.ggp.base.util.match.Match;
import org.ggp.base.util.statemachine.Move;


class RandomPlayRequestThread(PlayRequestThread):
{
    private Move move;

    def RandomPlayRequestThread(match=Match(), List<Move> legalMoves)
	{
        super(null, match, null, legalMoves, null, null, 0, null, true);
        move = legalMoves.get(new Random().nextInt(legalMoves.size()));

    def Move getMove()
	{
        return move;

    def void run()
	{
		;
}