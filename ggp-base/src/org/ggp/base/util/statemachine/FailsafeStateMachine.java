package org.ggp.base.util.statemachine

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


/**
 * The FailsafeStateMachine is a wrapper around a particular state machine.
 * It will catch errors/exceptions being thrown from that state machine, and
 * fall back to a regular prover if the state machine fails. It's not totally
 * clear that this is helpful, but it's an additional layer of bullet-proofing
 * in case anything goes wrong.
 *
 * @author Sam Schreiber
 */
class FailsafeStateMachine(StateMachine):

    private StateMachine theBackingMachine = null
    gameDescription = List<Gdl>()

    def FailsafeStateMachine (StateMachine theInitialMachine):
        theBackingMachine = theInitialMachine

    def String getName():
        if(theBackingMachine != null):
            return "Failsafe(" + theBackingMachine.getName() + ")"

        return "Failsafe(null)"

    def synchronized void initialize(List<Gdl> description):
        self.gameDescription = description

        if(attemptLoadingInitialMachine())
            return

        GamerLogger.logError("StateMachine", "Failsafe Machine: failed to load initial state machine. Falling back...")
        if(attemptLoadingProverMachine())
            return

        GamerLogger.logError("StateMachine", "Failsafe Machine: catastrophic failure to load *any* state machine. Cannot recover.")
        GamerLogger.logError("StateMachine", "Failsafe Machine: cannot recover from current state. Shutting down.")
        theBackingMachine = null

    private void failGracefully(Exception e1, Error e2):
        if(e1 != null) GamerLogger.logStackTrace("StateMachine", e1)
        if(e2 != null) GamerLogger.logStackTrace("StateMachine", e2)
        GamerLogger.logError("StateMachine", "Failsafe Machine: graceful failure mode kicking in.")

        if(theBackingMachine.getClass() != ProverStateMachine.class):
            GamerLogger.logError("StateMachine", "Failsafe Machine: online failure for " + theBackingMachine.getClass() + ". Attempting to restart with a standard prover.")
            if(attemptLoadingProverMachine())
                return

        theBackingMachine = null
        GamerLogger.logError("StateMachine", "Failsafe Machine: online failure for regular prover. Cannot recover.")

    private bool attemptLoadingInitialMachine():
        try 
            theBackingMachine.initialize(gameDescription)
            GamerLogger.log("StateMachine", "Failsafe Machine: successfully activated initial state machine for use!")
            return true
        } catch(Exception e1):
        } catch(ThreadDeath d):
            throw d
        } catch(Error e2):

        return false

    private bool attemptLoadingProverMachine():
        try 
            StateMachine theStateMachine = new ProverStateMachine()
            theStateMachine.initialize(gameDescription)
            theBackingMachine = theStateMachine
            GamerLogger.log("StateMachine", "Failsafe Machine: successfully loaded traditional prover.")
            return true
        } catch(Exception e1):
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e2):

        return false

    def int getGoal(MachineState state, Role role) throws GoalDefinitionException 
        if(theBackingMachine == null)
            return 0

        try 
            return theBackingMachine.getGoal(state, role)
        } catch(GoalDefinitionException ge):
            throw ge
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return getGoal(state, role)

    def MachineState getInitialState():
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getInitialState()
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return getInitialState()

    def List<Move> getLegalMoves(MachineState state, Role role) throws MoveDefinitionException 
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getLegalMoves(state, role)
        } catch(MoveDefinitionException me):
            throw me
        } catch(Exception e):
            failGracefully(e, null)
        } catch(OutOfMemoryError e):
            throw e
        } catch(ThreadDeath d):
            throw d
        } catch(Error e):
            failGracefully(null, e)

        return getLegalMoves(state, role)

    def Move getRandomMove(MachineState state, Role role) throws MoveDefinitionException 
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getRandomMove(state, role)
        } catch(MoveDefinitionException me):
            throw me
        } catch(Exception e):
            failGracefully(e, null)
        } catch(OutOfMemoryError e):
            throw e
        } catch(ThreadDeath d):
            throw d
        } catch(Error e):
            failGracefully(null, e)

        return getRandomMove(state, role)

    def MachineState getMachineStateFromSentenceList(Set<GdlSentence> sentenceList):
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getMachineStateFromSentenceList(sentenceList)
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return getMachineStateFromSentenceList(sentenceList)

    def Move getMoveFromTerm(GdlTerm term):
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getMoveFromTerm(term)
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return getMoveFromTerm(term)

    def MachineState getNextState(MachineState state, List<Move> moves) throws TransitionDefinitionException 
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getNextState(state, moves)
        } catch(TransitionDefinitionException te):
            throw te
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return getNextState(state, moves)

    def MachineState getNextStateDestructively(MachineState state, List<Move> moves) throws TransitionDefinitionException 
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getNextStateDestructively(state, moves)
        } catch(TransitionDefinitionException te):
            throw te
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return getNextStateDestructively(state, moves)

    def Role getRoleFromConstant(GdlConstant constant):
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getRoleFromConstant(constant)
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return getRoleFromConstant(constant)

    def List<Role> getRoles():
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.getRoles()
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return getRoles()

    def bool isTerminal(MachineState state):
        if(theBackingMachine == null)
            return false

        try 
            return theBackingMachine.isTerminal(state)
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return isTerminal(state)

    def MachineState performDepthCharge(MachineState state, int[] theDepth) throws TransitionDefinitionException, MoveDefinitionException 
        if(theBackingMachine == null)
            return null

        try 
            return theBackingMachine.performDepthCharge(state, theDepth)
        except TransitionDefinitionException te):
        	throw te
        except MoveDefinitionException me):
        	throw me
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        return performDepthCharge(state, theDepth)

    def void getAverageDiscountedScoresFromRepeatedDepthCharges(MachineState state, float[] avgScores, float[] avgDepth, float discountFactor, int repetitions) throws TransitionDefinitionException, MoveDefinitionException, GoalDefinitionException 
        if(theBackingMachine == null)
            return

        try 
            theBackingMachine.getAverageDiscountedScoresFromRepeatedDepthCharges(state, avgScores, avgDepth, discountFactor, repetitions)
            return
        except TransitionDefinitionException te):
        	throw te
        except MoveDefinitionException me):
        	throw me
        except GoalDefinitionException ge):
        	throw ge
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        getAverageDiscountedScoresFromRepeatedDepthCharges(state, avgScores, avgDepth, discountFactor, repetitions)

    def void updateRoot(MachineState theState):
        if(theBackingMachine == null)
            return

        try 
            theBackingMachine.updateRoot(theState)
            return
        } catch(Exception e):
            failGracefully(e, null)
        } catch(ThreadDeath d):
            throw d
        } catch(OutOfMemoryError e):
            throw e
        } catch(Error e):
            failGracefully(null, e)

        updateRoot(theState)

    def StateMachine getBackingMachine():
        return theBackingMachine

