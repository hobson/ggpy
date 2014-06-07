package org.ggp.base.apps.kiosk

import java.awt.BorderLayout
import java.util.List
import java.util.concurrent.ArrayBlockingQueue
import java.util.concurrent.BlockingQueue

import javax.swing.JPanel

import org.ggp.base.player.gamer.exception.GamePreviewException
import org.ggp.base.player.gamer.statemachine.StateMachineGamer
import org.ggp.base.server.event.ServerCompletedMatchEvent
import org.ggp.base.server.event.ServerNewGameStateEvent
import org.ggp.base.util.game.Game
import org.ggp.base.util.gdl.grammar.GdlPool
import org.ggp.base.util.observer.Event
import org.ggp.base.util.observer.Observer
import org.ggp.base.util.statemachine.MachineState
import org.ggp.base.util.statemachine.Move
import org.ggp.base.util.statemachine.Role
import org.ggp.base.util.statemachine.StateMachine
import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException
import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException
import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException
import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine


class KioskGamer(StateMachineGamer implements Observer):
    private BlockingQueue<Move> theQueue = new ArrayBlockingQueue<Move>(25)

    theGUI = GameGUI()
    theGUIPanel = JPanel()
    def KioskGamer(JPanel theGUIPanel):
        self.theGUIPanel = theGUIPanel
        theGUIPanel.setLayout(new BorderLayout())

    private GameCanvas theCanvas = null
    def void setCanvas(GameCanvas theCanvas):
        self.theCanvas = theCanvas

    def void stateMachineMetaGame(int timeout)
            throws TransitionDefinitionException, MoveDefinitionException,
            GoalDefinitionException 
        if(theCanvas == null)
            throw new IllegalStateException("KioskGamer did not receive a canvas.")
        theCanvas.setStateMachine(getStateMachine())

        theGUI = new GameGUI(theCanvas)
        theGUI.setRole(getRole())
        theGUI.setBackground(theGUIPanel.getBackground())
        theGUI.updateGameState(getStateMachine().getInitialState())
        theGUI.addObserver(this)

        theGUIPanel.removeAll()
        theGUIPanel.add("Center", theGUI)
        theGUIPanel.repaint()

        theGUIPanel.setVisible(false)
        theGUIPanel.setVisible(true)
        theGUIPanel.validate()
        theGUIPanel.repaint()

    def Move stateMachineSelectMove(int timeout)
            throws TransitionDefinitionException, MoveDefinitionException,
            GoalDefinitionException 
    	theGUI.beginPlay()
        theQueue.clear()
        theGUI.updateGameState(getCurrentState())
        try 
            return theQueue.take()
        } catch(Exception e):
            e.printStackTrace()
            return null


    def StateMachine getInitialStateMachine():
        return new ProverStateMachine()

    def String getName():
        return "GraphicalHumanGamer"

    stateFromServer = MachineState()

    def void observe(Event event):
        if(event instanceof MoveSelectedEvent):
            Move theMove = ((MoveSelectedEvent)event).getMove()
            if(theQueue.size() < 2):
                theQueue.add(theMove)

        elif(event instanceof ServerNewGameStateEvent):
            stateFromServer = ((ServerNewGameStateEvent)event).getState()
        elif(event instanceof ServerCompletedMatchEvent):
            theGUI.updateGameState(stateFromServer)

            List<Role> theRoles = getStateMachine().getRoles()
            List<Integer> theGoals = ((ServerCompletedMatchEvent)event).getGoals()

            StringBuilder finalMessage = new StringBuilder()
            finalMessage.append("Goals: ")
            for(int i = 0; i < theRoles.size(); i++):
                finalMessage.append(theRoles.get(i))
                finalMessage.append(" = ")
                finalMessage.append(theGoals.get(i))
                if(i < theRoles.size()-1):
                    finalMessage.append(", ")


            theGUI.showFinalMessage(finalMessage.toString())


    def stateMachineStop():  # void
		// Do nothing

    def stateMachineAbort():  # void
		// Add an "ABORT" move to the queue so that we don't wait indefinitely
		// for a human to submit a move for the aborted match; instead we should
		// finish it up as quickly as possible so we can display the next match
		// when it arrives.
        theQueue.add(new Move(GdlPool.getConstant("ABORT")))
        theGUI.showFinalMessage("Aborted")

    def isComputerPlayer():  # bool
        return false

    def void preview(Game g, int timeout) throws GamePreviewException 
		
