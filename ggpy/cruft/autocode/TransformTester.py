#!/usr/bin/env python
""" generated source for module TransformTester """
# package: org.ggp.base.util.gdl.transforms
import java.util.List

import org.ggp.base.util.game.GameRepository

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine

import org.ggp.base.util.statemachine.verifier.StateMachineVerifier

# 
#  *
#  * @author Sam Schreiber
#  *
#  
class TransformTester(object):
    """ generated source for class TransformTester """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        showDiffs = False
        theReference = ProverStateMachine()
        theMachine = ProverStateMachine()
        theRepository = GameRepository.getDefaultRepository()
        for gameKey in theRepository.getGameKeys():
            if gameKey.contains("laikLee"):
                continue 
            #  Choose the transformation(s) to test here
            description = DeORer.run(description)
            newDescription = VariableConstrainer.replaceFunctionValuedVariables(description)
            if description.hashCode() != newDescription.hashCode():
                theReference.initialize(description)
                theMachine.initialize(newDescription)
                print "Detected activation in game " + gameKey + ". Checking consistency: "
                StateMachineVerifier.checkMachineConsistency(theReference, theMachine, 10000)
                if showDiffs:
                    for x in newDescription:
                        if not description.contains(x):
                            print "NEW: " + x
                    for x in description:
                        if not newDescription.contains(x):
                            print "OLD: " + x


if __name__ == '__main__':
    import sys
    TransformTester.main(sys.argv)

