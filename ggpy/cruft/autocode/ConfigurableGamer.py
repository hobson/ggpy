#!/usr/bin/env python
""" generated source for module ConfigurableGamer """
# package: org.ggp.base.player.gamer.statemachine.configurable
import java.util.Arrays

import java.util.List

import java.util.Random

import org.ggp.base.apps.player.config.ConfigPanel

import org.ggp.base.apps.player.detail.DetailPanel

import org.ggp.base.player.gamer.event.GamerSelectedMoveEvent

import org.ggp.base.player.gamer.exception.GameAnalysisException

import org.ggp.base.player.gamer.statemachine.StateMachineGamer

import org.ggp.base.util.game.Game

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.statemachine.MachineState

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.StateMachine

import org.ggp.base.util.statemachine.cache.CachedStateMachine

import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException

import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException

import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException

import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine

# 
#  * ConfigurablePlayer is a player that's designed to be configured via a set of
#  * parameters that can be adjusted without any code modifications. It presents
#  * a nice user interface for setting these parameters, and stores them as JSON
#  * when the user clicks "save" (and loads them automatically when new players
#  * are created).
#  * 
#  * @author Sam Schreiber
#  
class ConfigurableGamer(StateMachineGamer):
    """ generated source for class ConfigurableGamer """
    configPanel = ConfigurableConfigPanel()
    detailPanel = ConfigurableDetailPanel()
    theRandom = Random()
    statesExpanded = ConfigurableDetailPanel.AggregatingCounter()
    simulationsDone = ConfigurableDetailPanel.AggregatingCounter()
    expectedScore = ConfigurableDetailPanel.FixedCounter()

    def __init__(self):
        """ generated source for method __init__ """
        super(ConfigurableGamer, self).__init__()
        self.configPanel = ConfigurableConfigPanel()
        self.detailPanel = ConfigurableDetailPanel()
        self.statesExpanded = self.detailPanel.AggregatingCounter("States Expanded", False)
        self.simulationsDone = self.detailPanel.AggregatingCounter("Simulations Done", False)
        self.expectedScore = self.detailPanel.FixedCounter("Expected Score", True)

    def getName(self):
        """ generated source for method getName """
        return self.configPanel.getParameter("name", "Player #1")

    # 
    # 	 * Employs a configurable, parametrized algorithm that can be adjusted
    # 	 * with knobs and parameters that can be tweaked without detailed knowledge
    # 	 * of the code for the player.
    # 	 
    def stateMachineSelectMove(self, timeout):
        """ generated source for method stateMachineSelectMove """
        self.detailPanel.beginAddingDataPoints()
        theMachine = getStateMachine()
        start = System.currentTimeMillis()
        finishBy = timeout - 2500
        finishSelectionForcedBy = finishBy - 1000
        finishSelectionBy = finishSelectionForcedBy - 1000
        selectMoveThread = SelectMoveThread(finishSelectionBy)
        selectMoveThread.start()
        try:
            selectMoveThread.join(finishSelectionForcedBy - System.currentTimeMillis())
        except InterruptedException as e:
        selectMoveThread.interrupt()
        moves = theMachine.getLegalMoves(getCurrentState(), getRole())
        selection = selectMoveThread.getSelectedMove()
        ranOutOfTime = False
        if selection == None:
            ranOutOfTime = True
            selection = moves.get(0)
        stop = System.currentTimeMillis()
        self.detailPanel.addObservation(getMatch().getMoveHistory().size(), selection, stop - start, ranOutOfTime)
        notifyObservers(GamerSelectedMoveEvent(moves, selection, stop - start))
        return selection

    def analyze(self, g, timeout):
        """ generated source for method analyze """

    def stateMachineMetaGame(self, timeout):
        """ generated source for method stateMachineMetaGame """
        metagameStrategy = self.configPanel.getParameter("metagameStrategy", "None")
        if metagameStrategy == "Random Exploration":
            while finishBy > System.currentTimeMillis():
                getStateMachine().performDepthCharge(getStateMachine().getInitialState(), depth)
                self.statesExpanded.increment(depth[0])

    def stateMachineStop(self):
        """ generated source for method stateMachineStop """

    def stateMachineAbort(self):
        """ generated source for method stateMachineAbort """

    def getInitialStateMachine(self):
        """ generated source for method getInitialStateMachine """
        theMachine = StateMachine()
        stateMachine = self.configPanel.getParameter("stateMachine", "Prover")
        if stateMachine == "Prover":
            theMachine = ProverStateMachine()
        else:
            theMachine = ProverStateMachine()
        if self.configPanel.getParameter("cacheStateMachine", False):
            theMachine = CachedStateMachine(theMachine)
        return theMachine

    def getConfigPanel(self):
        """ generated source for method getConfigPanel """
        return self.configPanel

    def getDetailPanel(self):
        """ generated source for method getDetailPanel """
        return self.detailPanel

    class SelectMoveThread(Thread):
        """ generated source for class SelectMoveThread """
        strategy = str()
        selection = Move()
        finishBy = long()

        def __init__(self, finishBy):
            """ generated source for method __init__ """
            super(SelectMoveThread, self).__init__()
            self.strategy = self.configPanel.getParameter("strategy", "Noop")
            self.finishBy = finishBy
            self.selection = None

        def run(self):
            """ generated source for method run """
            try:
                if self.strategy == "Noop":
                    self.selection = Move(GdlPool.getConstant("Noop"))
                elif self.strategy == "Legal":
                    self.selection = moves.get(0)
                elif self.strategy == "Random":
                    self.selection = moves.get(self.theRandom.nextInt(len(moves)))
                elif self.strategy == "Puzzle":
                    self.selection = selectPuzzleMove(self.finishBy)
                elif self.strategy == "Minimax":
                    self.selection = selectMinimaxMove(self.finishBy)
                elif self.strategy == "Heuristic":
                    self.selection = selectHeuristicMove(self.finishBy)
                elif self.strategy == "Monte Carlo":
                    self.selection = selectMonteCarloMove(self.finishBy)
            except MoveDefinitionException as e:
                raise RuntimeException(e)
            except TransitionDefinitionException as e:
                raise RuntimeException(e)
            except GoalDefinitionException as e:
                raise RuntimeException(e)

        def getSelectedMove(self):
            """ generated source for method getSelectedMove """
            return self.selection

    def selectPuzzleMove(self, finishBy):
        """ generated source for method selectPuzzleMove """
        if getStateMachine().getRoles().size() > 1:
            return Move(GdlPool.getConstant("OOPS"))
        moves = getStateMachine().getLegalMoves(getCurrentState(), getRole())
        bestScoreSoFar = -1
        bestMoveSoFar = None
        for move in moves:
            self.statesExpanded.increment(1)
            if bestScoreAfterMove > bestScoreSoFar:
                bestScoreSoFar = bestScoreAfterMove
                bestMoveSoFar = move
                if bestScoreSoFar == 100:
                    break
        self.expectedScore.set(bestScoreSoFar)
        return bestMoveSoFar

    def getPuzzleBestScore(self, state):
        """ generated source for method getPuzzleBestScore """
        if getStateMachine().isTerminal(state):
            return getStateMachine().getGoal(state, getRole())
        bestScoreSoFar = -1
        moves = getStateMachine().getLegalMoves(state, getRole())
        for move in moves:
            self.statesExpanded.increment(1)
            bestScoreSoFar = Math.max(bestScoreSoFar, bestScoreAfterMove)
            if bestScoreSoFar == 100:
                break
        return bestScoreSoFar

    def selectMinimaxMove(self, finishBy):
        """ generated source for method selectMinimaxMove """
        moves = getStateMachine().getLegalMoves(getCurrentState(), getRole())
        bestScoreSoFar = -1
        bestMoveSoFar = None
        for move in moves:
            if bestScoreAfterMove > bestScoreSoFar:
                bestScoreSoFar = bestScoreAfterMove
                bestMoveSoFar = move
                if bestScoreSoFar == 100:
                    break
        self.expectedScore.set(bestScoreSoFar)
        return bestMoveSoFar

    def minimaxScoreForMove(self, state, myMove):
        """ generated source for method minimaxScoreForMove """
        worstScoreSoFar = 100
        for jointMove in getStateMachine().getLegalJointMoves(state, getRole(), myMove):
            self.statesExpanded.increment(1)
            if getStateMachine().isTerminal(stateAfterMove):
                bestScoreSoFar = getStateMachine().getGoal(stateAfterMove, getRole())
            else:
                for myNextMove in moves:
                    bestScoreSoFar = Math.max(bestScoreSoFar, bestScoreAfterMove)
                    if bestScoreSoFar == 100:
                        break
            worstScoreSoFar = Math.min(worstScoreSoFar, bestScoreSoFar)
            if worstScoreSoFar == 0:
                break
        return worstScoreSoFar

    def selectHeuristicMove(self, finishBy):
        """ generated source for method selectHeuristicMove """
        moves = getStateMachine().getLegalMoves(getCurrentState(), getRole())
        bestScoreSoFar = -1
        bestMoveSoFar = None
        for move in moves:
            if bestScoreAfterMove > bestScoreSoFar:
                bestScoreSoFar = bestScoreAfterMove
                bestMoveSoFar = move
                if bestScoreSoFar == 100:
                    break
        self.expectedScore.set(bestScoreSoFar)
        return bestMoveSoFar

    def heuristicScoreForMove(self, state, myMove, depth):
        """ generated source for method heuristicScoreForMove """
        worstScoreSoFar = 100
        for jointMove in getStateMachine().getLegalJointMoves(state, getRole(), myMove):
            self.statesExpanded.increment(1)
            if getStateMachine().isTerminal(stateAfterMove):
                bestScoreSoFar = getStateMachine().getGoal(stateAfterMove, getRole())
            elif depth == 0:
                bestScoreSoFar = MixtureHeuristic().evaluate(stateAfterMove)
            else:
                for myNextMove in moves:
                    bestScoreSoFar = Math.max(bestScoreSoFar, bestScoreAfterMove)
                    if bestScoreSoFar == 100:
                        break
            worstScoreSoFar = Math.min(worstScoreSoFar, bestScoreSoFar)
            if worstScoreSoFar == 0:
                break
        return worstScoreSoFar

    class Heuristic(object):
        """ generated source for interface Heuristic """
        __metaclass__ = ABCMeta
        @abstractmethod
        def evaluate(self, state):
            """ generated source for method evaluate """

    class MixtureHeuristic(Heuristic):
        """ generated source for class MixtureHeuristic """
        def evaluate(self, state):
            """ generated source for method evaluate """
            focusWeight = self.configPanel.getParameter("heuristicFocus", 1)
            mobilityWeight = self.configPanel.getParameter("heuristicMobility", 1)
            opponentFocusWeight = self.configPanel.getParameter("heuristicOpponentFocus", 1)
            opponentMobilityWeight = self.configPanel.getParameter("heuristicOpponentMobility", 1)
            totalWeight = focusWeight + mobilityWeight + opponentFocusWeight + opponentMobilityWeight
            return int(((focusWeight * FocusHeuristic().evaluate(state) + mobilityWeight * MobilityHeuristic().evaluate(state) + opponentFocusWeight * OpponentFocusHeuristic().evaluate(state) + opponentMobilityWeight * OpponentMobilityHeuristic().evaluate(state)) / totalWeight))

    class MoveBasedHeuristic(object):
        """ generated source for class MoveBasedHeuristic """
        def myMoveCount(self, state):
            """ generated source for method myMoveCount """
            return getStateMachine().getLegalMoves(state, getRole()).size()

        def theirMoveCount(self, state):
            """ generated source for method theirMoveCount """
            return getStateMachine().getLegalJointMoves(state).size() / getStateMachine().getLegalMoves(state, getRole()).size()

        def getDescendingScore(self, forCount):
            """ generated source for method getDescendingScore """
            return int((100 * Math.exp((1 - forCount) / 5.0)))

        def getAscendingScore(self, forCount):
            """ generated source for method getAscendingScore """
            return int((100 * Math.exp(-1 / forCount)))

    class FocusHeuristic(MoveBasedHeuristic, Heuristic):
        """ generated source for class FocusHeuristic """
        def evaluate(self, state):
            """ generated source for method evaluate """
            return getDescendingScore(myMoveCount(state))

    class MobilityHeuristic(MoveBasedHeuristic, Heuristic):
        """ generated source for class MobilityHeuristic """
        def evaluate(self, state):
            """ generated source for method evaluate """
            return getAscendingScore(myMoveCount(state))

    class OpponentFocusHeuristic(MoveBasedHeuristic, Heuristic):
        """ generated source for class OpponentFocusHeuristic """
        def evaluate(self, state):
            """ generated source for method evaluate """
            return getDescendingScore(theirMoveCount(state))

    class OpponentMobilityHeuristic(MoveBasedHeuristic, Heuristic):
        """ generated source for class OpponentMobilityHeuristic """
        def evaluate(self, state):
            """ generated source for method evaluate """
            return getAscendingScore(theirMoveCount(state))

    def selectMonteCarloMove(self, finishBy):
        """ generated source for method selectMonteCarloMove """
        theMachine = getStateMachine()
        timeToExpect = System.currentTimeMillis() + 1000
        moves = theMachine.getLegalMoves(getCurrentState(), getRole())
        selection = moves.get(0)
        if len(moves) > 1:
            while True:
                if System.currentTimeMillis() > finishBy:
                    break
                moveTotalPoints[i] += theScore
                moveTotalAttempts[i] += 1
                self.simulationsDone.increment(1)
                if System.currentTimeMillis() > timeToExpect:
                    while j < len(moves):
                        bestChildValueSoFar = Math.max(bestChildValueSoFar, float(moveTotalPoints[i]) / moveTotalAttempts[i])
                        j += 1
                    self.expectedScore.set(bestChildValueSoFar)
                    timeToExpect = System.currentTimeMillis() + 1000
                i = (i + 1) % len(moves)
            while i < len(moves):
                moveExpectedPoints[i] = float(moveTotalPoints[i]) / moveTotalAttempts[i]
                i += 1
            while i < len(moves):
                if moveExpectedPoints[i] > bestMoveScore:
                    bestMoveScore = moveExpectedPoints[i]
                    bestMove = i
                i += 1
            selection = moves.get(bestMove)
        return selection

    depth = [None]*1

    def performMonteCarloDepthChargeFromMove(self, theState, myMove):
        """ generated source for method performMonteCarloDepthChargeFromMove """
        theMachine = getStateMachine()
        try:
            self.statesExpanded.increment(self.depth[0])
            return theMachine.getGoal(finalState, getRole()) * Math.pow(1 - (self.configPanel.getParameter("mcDecayRate", 0) / 100.0), self.depth[0])
        except Exception as e:
            e.printStackTrace()
            return 0

