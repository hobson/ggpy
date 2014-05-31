#!/usr/bin/env python
""" generated source for module BasesInputsValidator """
# package: org.ggp.base.validator
import java.util.ArrayList

import java.util.Collections

import java.util.HashSet

import java.util.List

import java.util.Set

import org.ggp.base.util.game.CloudGameRepository

import org.ggp.base.util.game.Game

import org.ggp.base.util.game.GameRepository

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.prover.aima.AimaProver

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

import org.ggp.base.util.statemachine.StateMachine

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine

import com.google.common.collect.ImmutableList

class BasesInputsValidator(GameValidator):
    """ generated source for class BasesInputsValidator """
    BASE = GdlPool.getConstant("base")
    INPUT = GdlPool.getConstant("input")
    TRUE = GdlPool.getConstant("true")
    LEGAL = GdlPool.getConstant("legal")
    X = GdlPool.getVariable("?x")
    Y = GdlPool.getVariable("?y")
    millisecondsToTest = int()

    def __init__(self, millisecondsToTest):
        """ generated source for method __init__ """
        super(BasesInputsValidator, self).__init__()
        self.millisecondsToTest = millisecondsToTest

    def checkValidity(self, theGame):
        """ generated source for method checkValidity """
        try:
            sm.initialize(theGame.getRules())
            if len(bases) == 0:
                raise ValidatorException("Could not find base propositions.")
            elif len(inputs) == 0:
                raise ValidatorException("Could not find input propositions.")
            for base in bases:
                truesFromBases.add(GdlPool.getRelation(self.TRUE, base.getBody()))
            for input in inputs:
                legalsFromInputs.add(GdlPool.getRelation(self.LEGAL, input.getBody()))
            if truesFromBases.isEmpty() and legalsFromInputs.isEmpty():
                return ImmutableList.of()
            while System.currentTimeMillis() < startTime + self.millisecondsToTest:
                # Check state against bases, inputs
                if not truesFromBases.isEmpty():
                    if not truesFromBases.containsAll(state.getContents()):
                        missingBases.addAll(state.getContents())
                        missingBases.removeAll(truesFromBases)
                        raise ValidatorException("Found missing bases: " + missingBases)
                if not legalsFromInputs.isEmpty():
                    for role in sm.getRoles():
                        for move in legalMoves:
                            legalSentences.add(GdlPool.getRelation(self.LEGAL, [None]*))
                    if not legalsFromInputs.containsAll(legalSentences):
                        missingInputs.addAll(legalSentences)
                        missingInputs.removeAll(legalsFromInputs)
                        raise ValidatorException("Found missing inputs: " + missingInputs)
                state = sm.getRandomNextState(state)
                if sm.isTerminal(state):
                    state = initialState
        except MoveDefinitionException as mde:
            raise ValidatorException("Could not find legal moves while simulating: " + mde)
        except TransitionDefinitionException as tde:
            raise ValidatorException("Could not find transition definition while simulating: " + tde)
        except RuntimeException as e:
            raise ValidatorException("Ran into a runtime exception while simulating: " + e)
        except StackOverflowError as e:
            raise ValidatorException("Ran into a stack overflow while simulating: " + e)
        except OutOfMemoryError as e:
            raise ValidatorException("Ran out of memory while simulating: " + e)
        return ImmutableList.of()

    # 
    # 	 * @param args
    # 	 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        gameRepo = CloudGameRepository("http://games.ggp.org/stanford/")
        for gameKey in gameRepo.getGameKeys():
            if not gameKey == "amazons" and not gameKey == "alexChess":
                try:
                    BasesInputsValidator(20000).checkValidity(gameRepo.getGame(gameKey))
                    print "Game " + gameKey + " has valid base/input propositions."
                except ValidatorException as ve:
                    print "Game " + gameKey + " is invalid: " + ve.getMessage()


if __name__ == '__main__':
    import sys
    BasesInputsValidator.main(sys.argv)

