#!/usr/bin/env python
""" generated source for module GameFlowTester """
# package: org.ggp.base.util.gdl.model
import org.ggp.base.util.game.Game

import org.ggp.base.util.game.GameRepository

class GameFlowTester(object):
    """ generated source for class GameFlowTester """
    # This doesn't really "test" the game flow so much as let us
    # examine it to evaluate it.
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        gameName = "tictactoe"
        theGame = GameRepository.getDefaultRepository().getGame(gameName)
        flow = GameFlow(theGame.getRules())
        print "Size of flow: " + flow.getNumTurns()
        print "Sentence forms in flow: " + flow.getSentenceForms()
        i = 0
        while i < flow.getNumTurns():
            print "On turn " + i + ": " + flow.getSentencesTrueOnTurn(i)
            i += 1
        print "Turn after last: " + flow.getTurnAfterLast()


if __name__ == '__main__':
    import sys
    GameFlowTester.main(sys.argv)

