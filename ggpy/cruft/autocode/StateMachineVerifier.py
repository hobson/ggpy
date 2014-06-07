#!/usr/bin/env python
""" generated source for module StateMachineVerifier """
# package: org.ggp.base.util.statemachine.verifier
import java.util.ArrayList

import java.util.List

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

import org.ggp.base.util.statemachine.StateMachine

class StateMachineVerifier(object):
    """ generated source for class StateMachineVerifier """
    @classmethod
    def checkMachineConsistency(cls, theReference, theSubject, timeToSpend):
        """ generated source for method checkMachineConsistency """
        startTime = System.currentTimeMillis()
        GamerLogger.log("StateMachine", "Performing automatic consistency testing on " + theSubject.__class__.__name__ + " using " + theReference.__class__.__name__ + " as a reference.")
        theMachines = ArrayList()
        theMachines.add(theReference)
        theMachines.add(theSubject)
        GamerLogger.emitToConsole("Consistency checking: [")
        nRound = 0
        while True:
            nRound += 1
            GamerLogger.emitToConsole(".")
            while i < len(theMachines):
                try:
                    theCurrentStates[i] = theMachines.get(i).getInitialState()
                except Exception as e:
                    GamerLogger.log("StateMachine", "Machine #" + i + " failed to generate an initial state!")
                    return False
                i += 1
            while not theMachines.get(0).isTerminal(theCurrentStates[0]):
                if System.currentTimeMillis() > startTime + timeToSpend:
                    break
                #  Do per-state consistency checks
                while i < len(theMachines):
                    for theRole in theMachines.get(0).getRoles():
                        try:
                            if not (theMachines.get(i).getLegalMoves(theCurrentStates[i], theRole).size() == theMachines.get(0).getLegalMoves(theCurrentStates[0], theRole).size()):
                                GamerLogger.log("StateMachine", "Inconsistency between machine #" + i + " and ProverStateMachine over state " + theCurrentStates[0] + " vs " + theCurrentStates[i].getContents())
                                GamerLogger.log("StateMachine", "Machine #" + 0 + " has move count = " + theMachines.get(0).getLegalMoves(theCurrentStates[0], theRole).size() + " for player " + theRole)
                                GamerLogger.log("StateMachine", "Machine #" + i + " has move count = " + theMachines.get(i).getLegalMoves(theCurrentStates[i], theRole).size() + " for player " + theRole)
                                return False
                        except Exception as e:
                            GamerLogger.logStackTrace("StateMachine", e)
                    i += 1
                try:
                    while i < len(theMachines):
                        try:
                            theCurrentStates[i] = theMachines.get(i).getNextState(theCurrentStates[i], theJointMove)
                        except Exception as e:
                            GamerLogger.logStackTrace("StateMachine", e)
                        i += 1
                except Exception as e:
                    GamerLogger.logStackTrace("StateMachine", e)
            if System.currentTimeMillis() > startTime + timeToSpend:
                break
            while i < len(theMachines):
                if not theMachines.get(i).isTerminal(theCurrentStates[i]):
                    GamerLogger.log("StateMachine", "Inconsistency between machine #" + i + " and ProverStateMachine over terminal-ness of state " + theCurrentStates[0] + " vs " + theCurrentStates[i])
                    return False
                for theRole in theMachines.get(0).getRoles():
                    try:
                        theMachines.get(0).getGoal(theCurrentStates[0], theRole)
                    except Exception as e:
                        continue 
                    try:
                        if theMachines.get(i).getGoal(theCurrentStates[i], theRole) != theMachines.get(0).getGoal(theCurrentStates[0], theRole):
                            GamerLogger.log("StateMachine", "Inconsistency between machine #" + i + " and ProverStateMachine over goal value for " + theRole + " of state " + theCurrentStates[0] + ": " + theMachines.get(i).getGoal(theCurrentStates[i], theRole) + " vs " + theMachines.get(0).getGoal(theCurrentStates[0], theRole))
                            return False
                    except Exception as e:
                        GamerLogger.log("StateMachine", "Inconsistency between machine #" + i + " and ProverStateMachine over goal-ness of state " + theCurrentStates[0] + " vs " + theCurrentStates[i])
                        return False
                i += 1
        GamerLogger.emitToConsole("]\n")
        GamerLogger.log("StateMachine", "Completed automatic consistency testing on " + theSubject.__class__.__name__ + ", w/ " + nRound + " rounds: all tests pass!")
        return True

