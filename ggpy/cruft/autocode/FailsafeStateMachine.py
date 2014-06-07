#!/usr/bin/env python
""" generated source for module FailsafeStateMachine """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.statemachine
import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine

# 
#  * The FailsafeStateMachine is a wrapper around a particular state machine.
#  * It will catch errors/exceptions being thrown from that state machine, and
#  * fall back to a regular prover if the state machine fails. It's not totally
#  * clear that this is helpful, but it's an additional layer of bullet-proofing
#  * in case anything goes wrong.
#  *
#  * @author Sam Schreiber
#  
class FailsafeStateMachine(StateMachine):
    """ generated source for class FailsafeStateMachine """
    theBackingMachine = None
    gameDescription = List()

    def __init__(self, theInitialMachine):
        """ generated source for method __init__ """
        super(FailsafeStateMachine, self).__init__()
        self.theBackingMachine = theInitialMachine

    def getName(self):
        """ generated source for method getName """
        if self.theBackingMachine != None:
            return "Failsafe(" + self.theBackingMachine.__name__ + ")"
        return "Failsafe(null)"

    @synchronized
    def initialize(self, description):
        """ generated source for method initialize """
        self.gameDescription = description
        if attemptLoadingInitialMachine():
            return
        GamerLogger.logError("StateMachine", "Failsafe Machine: failed to load initial state machine. Falling back...")
        if attemptLoadingProverMachine():
            return
        GamerLogger.logError("StateMachine", "Failsafe Machine: catastrophic failure to load *any* state machine. Cannot recover.")
        GamerLogger.logError("StateMachine", "Failsafe Machine: cannot recover from current state. Shutting down.")
        self.theBackingMachine = None

    def failGracefully(self, e1, e2):
        """ generated source for method failGracefully """
        if e1 != None:
            GamerLogger.logStackTrace("StateMachine", e1)
        if e2 != None:
            GamerLogger.logStackTrace("StateMachine", e2)
        GamerLogger.logError("StateMachine", "Failsafe Machine: graceful failure mode kicking in.")
        if self.theBackingMachine.__class__ != ProverStateMachine.__class__:
            GamerLogger.logError("StateMachine", "Failsafe Machine: online failure for " + self.theBackingMachine.__class__ + ". Attempting to restart with a standard prover.")
            if attemptLoadingProverMachine():
                return
        self.theBackingMachine = None
        GamerLogger.logError("StateMachine", "Failsafe Machine: online failure for regular prover. Cannot recover.")

    def attemptLoadingInitialMachine(self):
        """ generated source for method attemptLoadingInitialMachine """
        try:
            self.theBackingMachine.initialize(self.gameDescription)
            GamerLogger.log("StateMachine", "Failsafe Machine: successfully activated initial state machine for use!")
            return True
        except Exception as e1:
            pass
        except ThreadDeath as d:
            raise d
        except Error as e2:
            pass
        return False

    def attemptLoadingProverMachine(self):
        """ generated source for method attemptLoadingProverMachine """
        try:
            theStateMachine.initialize(self.gameDescription)
            self.theBackingMachine = theStateMachine
            GamerLogger.log("StateMachine", "Failsafe Machine: successfully loaded traditional prover.")
            return True
        except Exception as e1:
            pass
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e2:
            pass
        return False

    def getGoal(self, state, role):
        """ generated source for method getGoal """
        if self.theBackingMachine == None:
            return 0
        try:
            return self.theBackingMachine.getGoal(state, role)
        except GoalDefinitionException as ge:
            raise ge
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.getGoal(state, role)

    def getInitialState(self):
        """ generated source for method getInitialState """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getInitialState()
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.getInitialState()

    def getLegalMoves(self, state, role):
        """ generated source for method getLegalMoves """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getLegalMoves(state, role)
        except MoveDefinitionException as me:
            raise me
        except Exception as e:
            self.failGracefully(e, None)
        except OutOfMemoryError as e:
            raise e
        except ThreadDeath as d:
            raise d
        except Error as e:
            self.failGracefully(None, e)
        return self.getLegalMoves(state, role)

    def getRandomMove(self, state, role):
        """ generated source for method getRandomMove """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getRandomMove(state, role)
        except MoveDefinitionException as me:
            raise me
        except Exception as e:
            self.failGracefully(e, None)
        except OutOfMemoryError as e:
            raise e
        except ThreadDeath as d:
            raise d
        except Error as e:
            self.failGracefully(None, e)
        return self.getRandomMove(state, role)

    def getMachineStateFromSentenceList(self, sentenceList):
        """ generated source for method getMachineStateFromSentenceList """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getMachineStateFromSentenceList(sentenceList)
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.getMachineStateFromSentenceList(sentenceList)

    def getMoveFromTerm(self, term):
        """ generated source for method getMoveFromTerm """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getMoveFromTerm(term)
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.getMoveFromTerm(term)

    def getNextState(self, state, moves):
        """ generated source for method getNextState """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getNextState(state, moves)
        except TransitionDefinitionException as te:
            raise te
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.getNextState(state, moves)

    def getNextStateDestructively(self, state, moves):
        """ generated source for method getNextStateDestructively """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getNextStateDestructively(state, moves)
        except TransitionDefinitionException as te:
            raise te
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.getNextStateDestructively(state, moves)

    def getRoleFromConstant(self, constant):
        """ generated source for method getRoleFromConstant """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getRoleFromConstant(constant)
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.getRoleFromConstant(constant)

    def getRoles(self):
        """ generated source for method getRoles """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.getRoles()
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.getRoles()

    def isTerminal(self, state):
        """ generated source for method isTerminal """
        if self.theBackingMachine == None:
            return False
        try:
            return self.theBackingMachine.isTerminal(state)
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.isTerminal(state)

    def performDepthCharge(self, state, theDepth):
        """ generated source for method performDepthCharge """
        if self.theBackingMachine == None:
            return None
        try:
            return self.theBackingMachine.performDepthCharge(state, theDepth)
        except TransitionDefinitionException as te:
            raise te
        except MoveDefinitionException as me:
            raise me
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        return self.performDepthCharge(state, theDepth)

    def getAverageDiscountedScoresFromRepeatedDepthCharges(self, state, avgScores, avgDepth, discountFactor, repetitions):
        """ generated source for method getAverageDiscountedScoresFromRepeatedDepthCharges """
        if self.theBackingMachine == None:
            return
        try:
            self.theBackingMachine.getAverageDiscountedScoresFromRepeatedDepthCharges(state, avgScores, avgDepth, discountFactor, repetitions)
            return
        except TransitionDefinitionException as te:
            raise te
        except MoveDefinitionException as me:
            raise me
        except GoalDefinitionException as ge:
            raise ge
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        self.getAverageDiscountedScoresFromRepeatedDepthCharges(state, avgScores, avgDepth, discountFactor, repetitions)

    def updateRoot(self, theState):
        """ generated source for method updateRoot """
        if self.theBackingMachine == None:
            return
        try:
            self.theBackingMachine.updateRoot(theState)
            return
        except Exception as e:
            self.failGracefully(e, None)
        except ThreadDeath as d:
            raise d
        except OutOfMemoryError as e:
            raise e
        except Error as e:
            self.failGracefully(None, e)
        self.updateRoot(theState)

    def getBackingMachine(self):
        """ generated source for method getBackingMachine """
        return self.theBackingMachine

