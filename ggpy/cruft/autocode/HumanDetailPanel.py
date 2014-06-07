#!/usr/bin/env python
""" generated source for module HumanDetailPanel """
# package: org.ggp.base.player.gamer.statemachine.human.gui
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

@SuppressWarnings("serial")
class HumanDetailPanel(DetailPanel):
    """ generated source for class HumanDetailPanel """
    moveTable = JZebraTable()
    moveTextField = JTextField()
    selectButton = JButton()
    selection = Move()
    timerBar = JTimerBar()

    def __init__(self):
        """ generated source for method __init__ """
        super(HumanDetailPanel, self).__init__(GridBagLayout())
        model = DefaultTableModel()
        model.addColumn("Legal Moves")
        self.moveTable = JZebraTable(model)
        self.selectButton = JButton(selectButtonMethod())
        self.moveTextField = JTextField()
        self.timerBar = JTimerBar()
        self.selection = None
        self.moveTable.setShowHorizontalLines(True)
        self.moveTable.setShowVerticalLines(True)
        self.moveTextField.setEditable(False)
        self.add(JScrollPane(self.moveTable, ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS, ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED), GridBagConstraints(0, 0, 2, 1, 1.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, Insets(5, 5, 5, 5), 5, 5))
        self.add(self.selectButton, GridBagConstraints(0, 1, 1, 1, 0.0, 0.0, GridBagConstraints.CENTER, GridBagConstraints.HORIZONTAL, Insets(5, 5, 5, 5), 0, 0))
        self.add(self.moveTextField, GridBagConstraints(1, 1, 1, 1, 1.0, 0.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, Insets(5, 5, 5, 5), 5, 5))
        self.add(self.timerBar, GridBagConstraints(0, 2, 2, 1, 1.0, 0.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, Insets(5, 5, 5, 5), 5, 5))

    @overloaded
    def observe(self, event):
        """ generated source for method observe """
        if isinstance(event, (HumanNewMovesEvent, )):
            self.observe(event)
        elif isinstance(event, (HumanTimeoutEvent, )):
            self.observe(event)
        elif isinstance(event, (PlayerTimeEvent, )):
            self.observe(event)

    @observe.register(object, HumanNewMovesEvent)
    def observe_0(self, event):
        """ generated source for method observe_0 """
        model = self.moveTable.getModel()
        model.setRowCount(0)
        for move in event.getMoves():
            model.addRow([None]*)
        self.selection = event.getSelection()
        self.moveTextField.setText(self.selection.__str__())

    @observe.register(object, HumanTimeoutEvent)
    def observe_1(self, event):
        """ generated source for method observe_1 """
        event.getHumanPlayer().setMove(self.selection)

    @observe.register(object, PlayerTimeEvent)
    def observe_2(self, event):
        """ generated source for method observe_2 """
        self.timerBar.time(event.getTime(), 500)

    def selectButtonMethod(self):
        """ generated source for method selectButtonMethod """
        return AbstractAction("Select")

