package org.ggp.base.apps.kiosk

import java.awt.BorderLayout
import java.awt.Color
import java.awt.FlowLayout
import java.awt.Font
import java.awt.event.ActionEvent
import java.awt.event.ActionListener
import java.util.HashSet
import java.util.Set

import javax.swing.JButton
import javax.swing.JLabel
import javax.swing.JPanel

import org.ggp.base.util.observer.Event
import org.ggp.base.util.observer.Observer
import org.ggp.base.util.observer.Subject
import org.ggp.base.util.statemachine.MachineState
import org.ggp.base.util.statemachine.Move
import org.ggp.base.util.statemachine.Role

class GameGUI(JPanel implements Subject, Observer, ActionListener):
    serialVersionUID = 0x1  # int 

    theCanvas = GameCanvas()
    workingMove = Move()

    workingMoveLabel = JLabel()
    submitMoveButton = JButton()
    clearSelectionButton = JButton()

    private bool gameOver = false

    private bool moveBeingSubmitted = false
    private bool stillMetagaming = true

    def GameGUI(GameCanvas theCanvas):
        super(new BorderLayout())

        self.theCanvas = theCanvas

        JLabel theTitleLabel = new JLabel(theCanvas.getGameName())
        theTitleLabel.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 36))

        JPanel northPanel = new JPanel(new FlowLayout())
        northPanel.add(theTitleLabel)

        submitMoveButton = new JButton("Submit Move")
        submitMoveButton.addActionListener(this)

        clearSelectionButton = new JButton("Clear Selection")
        clearSelectionButton.addActionListener(this)

        workingMoveLabel = new JLabel()

        JPanel southCenterPanel = new JPanel(new FlowLayout())
        JPanel southEastPanel = new JPanel(new FlowLayout())
        JPanel southPanel = new JPanel(new BorderLayout())
        southEastPanel.add(new JLabel("Time Remaining     "))
        southEastPanel.add(clearSelectionButton)
        southEastPanel.add(submitMoveButton)
        southPanel.add("West", workingMoveLabel)
        southPanel.add("Center", southCenterPanel)
        southPanel.add("East", southEastPanel)

        add("North", northPanel)
        add("Center", theCanvas)
        add("South", southPanel)

        northPanel.setBackground(theCanvas.getBackground())
        southPanel.setBackground(theCanvas.getBackground())
        southEastPanel.setBackground(theCanvas.getBackground())
        southCenterPanel.setBackground(theCanvas.getBackground())

        theCanvas.addObserver(this)
        updateControls()

    def void beginPlay():
    	stillMetagaming = false
    	updateControls()

    def void updateGameState(MachineState gameState):
    	moveBeingSubmitted = false
        theCanvas.updateGameState(gameState)
        updateControls()

    def void setRole(Role r):
        theCanvas.setRole(r)

    def void observe(Event event):
        if(event instanceof MoveSelectedEvent):
            workingMove = ((MoveSelectedEvent)event).getMove()
            if(((MoveSelectedEvent)event).isFinal()):
            	moveBeingSubmitted = true
            	updateControls()
            	notifyObservers(new MoveSelectedEvent(workingMove))

            updateControls()


    private void updateControls():
        submitMoveButton.setEnabled(!gameOver && !moveBeingSubmitted && !stillMetagaming)
        clearSelectionButton.setEnabled(!gameOver && !moveBeingSubmitted && !stillMetagaming)
        theCanvas.setEnabled(!gameOver && !moveBeingSubmitted && !stillMetagaming)

        if(gameOver) return
        if(workingMove == null):
            workingMoveLabel.setText("  Working Move: <none>")
            submitMoveButton.setEnabled(false)
            clearSelectionButton.setEnabled(false)
        else:
            workingMoveLabel.setText("  Working Move: " + workingMove)


    def void showFinalMessage(String theMessage):
        workingMoveLabel.setText(theMessage)
        workingMoveLabel.setForeground(Color.RED)
        gameOver = true
        updateControls()

        validate()
        repaint()

    def void actionPerformed(ActionEvent e):
        if(gameOver) return

        if(e.getSource() == clearSelectionButton):
            theCanvas.clearMoveSelection()
        elif(e.getSource() == submitMoveButton):
            if(workingMove != null):
                moveBeingSubmitted = true
                updateControls()
                notifyObservers(new MoveSelectedEvent(workingMove))



    // Subject boilerplate
    private Set<Observer> theObservers = new HashSet<Observer>()

    def void addObserver(Observer observer):
        theObservers.add(observer)

    def void notifyObservers(Event event):
        for(Observer theObserver : theObservers)
            theObserver.observe(event)

