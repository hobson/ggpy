package org.ggp.base.player.gamer.statemachine.human.gui

import java.awt.GridBagConstraints
import java.awt.GridBagLayout
import java.awt.Insets
import java.awt.event.ActionEvent

import javax.swing.AbstractAction
import javax.swing.JButton
import javax.swing.JScrollPane
import javax.swing.JTextField
import javax.swing.ScrollPaneConstants
import javax.swing.table.DefaultTableModel

import org.ggp.base.apps.player.detail.DetailPanel
import org.ggp.base.player.event.PlayerTimeEvent
import org.ggp.base.player.gamer.statemachine.human.event.HumanNewMovesEvent
import org.ggp.base.player.gamer.statemachine.human.event.HumanTimeoutEvent
import org.ggp.base.util.observer.Event
import org.ggp.base.util.statemachine.Move
import org.ggp.base.util.ui.table.JZebraTable
import org.ggp.base.util.ui.timer.JTimerBar


class HumanDetailPanel(DetailPanel):


    moveTable = JZebraTable()
    moveTextField = JTextField()
    selectButton = JButton()
    selection = Move()
    timerBar = JTimerBar()

    def HumanDetailPanel()
	
        super(new GridBagLayout())

        DefaultTableModel model = new DefaultTableModel()
        model.addColumn("Legal Moves")

        moveTable = new JZebraTable(model)
		

        		    def bool isCellEditable(int rowIndex, int colIndex)
			
                return false

        selectButton = new JButton(selectButtonMethod())
        moveTextField = new JTextField()
        timerBar = new JTimerBar()
        selection = null

        moveTable.setShowHorizontalLines(true)
        moveTable.setShowVerticalLines(true)
        moveTextField.setEditable(false)

        self.add(new JScrollPane(moveTable, ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS, ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED), new GridBagConstraints(0, 0, 2, 1, 1.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, new Insets(5, 5, 5, 5), 5, 5))
        self.add(selectButton, new GridBagConstraints(0, 1, 1, 1, 0.0, 0.0, GridBagConstraints.CENTER, GridBagConstraints.HORIZONTAL, new Insets(5, 5, 5, 5), 0, 0))
        self.add(moveTextField, new GridBagConstraints(1, 1, 1, 1, 1.0, 0.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, new Insets(5, 5, 5, 5), 5, 5))
        self.add(timerBar, new GridBagConstraints(0, 2, 2, 1, 1.0, 0.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, new Insets(5, 5, 5, 5), 5, 5))

    def void observe(Event event)
	
        if (event instanceof HumanNewMovesEvent)
		
            observe((HumanNewMovesEvent) event)
        else if (event instanceof HumanTimeoutEvent)
		
            observe((HumanTimeoutEvent) event)
        else if (event instanceof PlayerTimeEvent)
		
            observe((PlayerTimeEvent) event)

    private void observe(HumanNewMovesEvent event)
	
        DefaultTableModel model = (DefaultTableModel) moveTable.getModel()
        model.setRowCount(0)
        for (Move move : event.getMoves())
		
            model.addRow(new Move[]  move })

        selection = event.getSelection()
        moveTextField.setText(selection.toString())

    private void observe(HumanTimeoutEvent event)
	
        event.getHumanPlayer().setMove(selection)

    private void observe(PlayerTimeEvent event)
	
        timerBar.time(event.getTime(), 500)

    private AbstractAction selectButtonMethod()
	
        return new AbstractAction("Select")
		

        		    def void actionPerformed(ActionEvent evt)
			
                int row = moveTable.getSelectedRow()
                if (row != -1)
				
                    DefaultTableModel model = (DefaultTableModel) moveTable.getModel()
                    selection = (Move) model.getValueAt(row, 0)
                    moveTextField.setText(selection.toString())


