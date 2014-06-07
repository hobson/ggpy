#!/usr/bin/env python
""" generated source for module ConfigurableConfigPanel """
# package: org.ggp.base.player.gamer.statemachine.configurable
import java.awt.GridBagConstraints

import java.awt.GridBagLayout

import java.awt.Insets

import java.awt.event.ActionEvent

import java.awt.event.ActionListener

import java.io.BufferedReader

import java.io.BufferedWriter

import java.io.File

import java.io.FileInputStream

import java.io.FileWriter

import java.io.IOException

import java.io.InputStreamReader

import java.nio.charset.Charset

import java.util.Random

import javax.swing.AbstractAction

import javax.swing.JButton

import javax.swing.JCheckBox

import javax.swing.JComboBox

import javax.swing.JFileChooser

import javax.swing.JLabel

import javax.swing.JPanel

import javax.swing.JSpinner

import javax.swing.JTextField

import javax.swing.SpinnerNumberModel

import javax.swing.border.TitledBorder

import javax.swing.event.ChangeEvent

import javax.swing.event.ChangeListener

import javax.swing.event.DocumentEvent

import javax.swing.event.DocumentListener

import javax.swing.filechooser.FileFilter

import org.ggp.base.apps.player.config.ConfigPanel

import external.JSON.JSONException

import external.JSON.JSONObject

class ConfigurableConfigPanel(ConfigPanel, ActionListener, DocumentListener, ChangeListener):
    """ generated source for class ConfigurableConfigPanel """
    serialVersionUID = 1L
    associatedFile = File()
    associatedFileField = JTextField()
    params = JSONObject()
    savedParams = str()
    loadButton = JButton()
    saveAsButton = JButton()
    saveButton = JButton()
    name = JTextField()
    strategy = JComboBox()
    metagameStrategy = JComboBox()
    stateMachine = JComboBox()
    cacheStateMachine = JCheckBox()
    maxPlys = JSpinner()
    heuristicFocus = JSpinner()
    heuristicMobility = JSpinner()
    heuristicOpponentFocus = JSpinner()
    heuristicOpponentMobility = JSpinner()
    mcDecayRate = JSpinner()
    rightPanel = JPanel()

    def __init__(self):
        """ generated source for method __init__ """
        super(ConfigurableConfigPanel, self).__init__(GridBagLayout())
        leftPanel = JPanel(GridBagLayout())
        leftPanel.setBorder(TitledBorder("Major Parameters"))
        self.rightPanel = JPanel(GridBagLayout())
        self.rightPanel.setBorder(TitledBorder("Minor Parameters"))
        self.strategy = JComboBox([None]*)
        self.metagameStrategy = JComboBox([None]*)
        self.stateMachine = JComboBox([None]*)
        self.cacheStateMachine = JCheckBox()
        self.maxPlys = JSpinner(SpinnerNumberModel(1, 1, 100, 1))
        self.heuristicFocus = JSpinner(SpinnerNumberModel(1, 0, 10, 1))
        self.heuristicMobility = JSpinner(SpinnerNumberModel(1, 0, 10, 1))
        self.heuristicOpponentFocus = JSpinner(SpinnerNumberModel(1, 0, 10, 1))
        self.heuristicOpponentMobility = JSpinner(SpinnerNumberModel(1, 0, 10, 1))
        self.mcDecayRate = JSpinner(SpinnerNumberModel(0, 0, 99, 1))
        self.name = JTextField()
        self.name.setColumns(20)
        self.name.setText("Player #" + Random().nextInt(100000))
        self.loadButton = JButton(loadButtonMethod())
        self.saveButton = JButton(saveButtonMethod())
        self.saveAsButton = JButton(saveAsButtonMethod())
        self.associatedFileField = JTextField()
        self.associatedFileField.setEnabled(False)
        buttons = JPanel()
        buttons.add(self.loadButton)
        buttons.add(self.saveButton)
        buttons.add(self.saveAsButton)
        nRow = 0
        leftPanel.add(JLabel("Name"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        __nRow_0 = nRow
        nRow += 1
        leftPanel.add(self.name, GridBagConstraints(1, __nRow_0, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.HORIZONTAL, Insets(5, 5, 5, 5), 5, 5))
        leftPanel.add(JLabel("Gaming Strategy"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        __nRow_1 = nRow
        nRow += 1
        leftPanel.add(self.strategy, GridBagConstraints(1, __nRow_1, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.HORIZONTAL, Insets(5, 5, 5, 5), 5, 5))
        leftPanel.add(JLabel("Metagame Strategy"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        __nRow_2 = nRow
        nRow += 1
        leftPanel.add(self.metagameStrategy, GridBagConstraints(1, __nRow_2, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.HORIZONTAL, Insets(5, 5, 5, 5), 5, 5))
        leftPanel.add(JLabel("State Machine"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        __nRow_3 = nRow
        nRow += 1
        leftPanel.add(self.stateMachine, GridBagConstraints(1, __nRow_3, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.HORIZONTAL, Insets(5, 5, 5, 5), 5, 5))
        __nRow_4 = nRow
        nRow += 1
        leftPanel.add(buttons, GridBagConstraints(1, __nRow_4, 2, 1, 1.0, 1.0, GridBagConstraints.SOUTHEAST, GridBagConstraints.NONE, Insets(5, 5, 0, 5), 0, 0))
        leftPanel.add(self.associatedFileField, GridBagConstraints(0, nRow, 2, 1, 1.0, 0.0, GridBagConstraints.SOUTHEAST, GridBagConstraints.HORIZONTAL, Insets(0, 5, 5, 5), 0, 0))
        layoutRightPanel()
        add(leftPanel, GridBagConstraints(0, 0, 1, 1, 0.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, Insets(5, 5, 5, 5), 5, 5))
        add(self.rightPanel, GridBagConstraints(1, 0, 1, 1, 1.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, Insets(5, 5, 5, 5), 5, 5))
        self.params = JSONObject()
        syncJSONtoUI()
        self.strategy.addActionListener(self)
        self.metagameStrategy.addActionListener(self)
        self.stateMachine.addActionListener(self)
        self.cacheStateMachine.addActionListener(self)
        self.maxPlys.addChangeListener(self)
        self.heuristicFocus.addChangeListener(self)
        self.heuristicMobility.addChangeListener(self)
        self.heuristicOpponentFocus.addChangeListener(self)
        self.heuristicOpponentMobility.addChangeListener(self)
        self.mcDecayRate.addChangeListener(self)
        self.name.getDocument().addDocumentListener(self)

    def layoutRightPanel(self):
        """ generated source for method layoutRightPanel """
        nRow = 0
        self.rightPanel.removeAll()
        self.rightPanel.add(JLabel("State machine cache?"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        __nRow_5 = nRow
        nRow += 1
        self.rightPanel.add(self.cacheStateMachine, GridBagConstraints(1, __nRow_5, 1, 1, 1.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        if self.strategy.getSelectedItem().__str__() == "Heuristic":
        __nRow_6 = nRow
        nRow += 1
        __nRow_7 = nRow
        nRow += 1
        __nRow_8 = nRow
        nRow += 1
        __nRow_9 = nRow
        nRow += 1
        __nRow_10 = nRow
        nRow += 1
            self.rightPanel.add(JLabel("Max plys?"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(self.maxPlys, GridBagConstraints(1, __nRow_6, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(JLabel("Focus Heuristic Weight"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(self.heuristicFocus, GridBagConstraints(1, __nRow_7, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(JLabel("Mobility Heuristic Weight"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(self.heuristicMobility, GridBagConstraints(1, __nRow_8, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(JLabel("Opponent Focus Heuristic Weight"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(self.heuristicOpponentFocus, GridBagConstraints(1, __nRow_9, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(JLabel("Opponent Mobility Heuristic Weight"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(self.heuristicOpponentMobility, GridBagConstraints(1, __nRow_10, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        if self.strategy.getSelectedItem().__str__() == "Monte Carlo":
        __nRow_11 = nRow
        nRow += 1
            self.rightPanel.add(JLabel("Goal Decay Rate"), GridBagConstraints(0, nRow, 1, 1, 0.0, 0.0, GridBagConstraints.EAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
            self.rightPanel.add(self.mcDecayRate, GridBagConstraints(1, __nRow_11, 1, 1, 0.0, 0.0, GridBagConstraints.WEST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        __nRow_12 = nRow
        nRow += 1
        self.rightPanel.add(JLabel(), GridBagConstraints(2, __nRow_12, 1, 1, 1.0, 1.0, GridBagConstraints.SOUTHEAST, GridBagConstraints.NONE, Insets(5, 5, 5, 5), 5, 5))
        self.rightPanel.repaint()

    @SuppressWarnings("unchecked")
    def getParameter(self, name, defaultValue):
        """ generated source for method getParameter """
        try:
            if self.params.has(name):
                return self.params.get(name)
            else:
                return defaultValue
        except JSONException as je:
            return defaultValue

    def actionPerformed(self, arg0):
        """ generated source for method actionPerformed """
        if arg0.getSource() == self.strategy:
            self.layoutRightPanel()
        syncJSONtoUI()

    def changedUpdate(self, e):
        """ generated source for method changedUpdate """
        syncJSONtoUI()

    def insertUpdate(self, e):
        """ generated source for method insertUpdate """
        syncJSONtoUI()

    def removeUpdate(self, e):
        """ generated source for method removeUpdate """
        syncJSONtoUI()

    def stateChanged(self, arg0):
        """ generated source for method stateChanged """
        syncJSONtoUI()

    def syncJSONtoUI(self):
        """ generated source for method syncJSONtoUI """
        if settingUI:
            return
        self.params = getJSONfromUI()
        self.saveButton.setEnabled(self.savedParams == None or not self.params.__str__() == self.savedParams)

    def getJSONfromUI(self):
        """ generated source for method getJSONfromUI """
        newParams = JSONObject()
        try:
            if not self.name.getText().isEmpty():
                newParams.put("name", self.name.getText())
            newParams.put("strategy", self.strategy.getSelectedItem().__str__())
            newParams.put("metagameStrategy", self.metagameStrategy.getSelectedItem().__str__())
            newParams.put("stateMachine", self.stateMachine.getSelectedItem().__str__())
            newParams.put("cacheStateMachine", self.cacheStateMachine.isSelected())
            newParams.put("maxPlys", self.maxPlys.getModel().getValue())
            newParams.put("heuristicFocus", self.heuristicFocus.getModel().getValue())
            newParams.put("heuristicMobility", self.heuristicMobility.getModel().getValue())
            newParams.put("heuristicOpponentFocus", self.heuristicOpponentFocus.getModel().getValue())
            newParams.put("heuristicOpponentMobility", self.heuristicOpponentMobility.getModel().getValue())
            newParams.put("mcDecayRate", self.mcDecayRate.getModel().getValue())
        except JSONException as je:
            je.printStackTrace()
        return newParams

    settingUI = False

    def setUIfromJSON(self):
        """ generated source for method setUIfromJSON """
        self.settingUI = True
        try:
            if self.params.has("name"):
                self.name.setText(self.params.getString("name"))
            if self.params.has("strategy"):
                self.strategy.setSelectedItem(self.params.getString("strategy"))
            if self.params.has("metagameStrategy"):
                self.metagameStrategy.setSelectedItem(self.params.getString("metagameStrategy"))
            if self.params.has("stateMachine"):
                self.stateMachine.setSelectedItem(self.params.getString("stateMachine"))
            if self.params.has("cacheStateMachine"):
                self.cacheStateMachine.setSelected(self.params.getBoolean("cacheStateMachine"))
            if self.params.has("maxPlys"):
                self.maxPlys.getModel().setValue(self.params.getInt("maxPlys"))
            if self.params.has("heuristicFocus"):
                self.heuristicFocus.getModel().setValue(self.params.getInt("heuristicFocus"))
            if self.params.has("heuristicMobility"):
                self.heuristicMobility.getModel().setValue(self.params.getInt("heuristicMobility"))
            if self.params.has("heuristicOpponentFocus"):
                self.heuristicOpponentFocus.getModel().setValue(self.params.getInt("heuristicOpponentFocus"))
            if self.params.has("heuristicOpponentMobility"):
                self.heuristicOpponentMobility.getModel().setValue(self.params.getInt("heuristicOpponentMobility"))
            if self.params.has("mcDecayRate"):
                self.mcDecayRate.getModel().setValue(self.params.getInt("mcDecayRate"))
        except JSONException as je:
            je.printStackTrace()
        finally:
            self.settingUI = False

    def loadParamsJSON(self, fromFile):
        """ generated source for method loadParamsJSON """
        if not fromFile.exists():
            return
        self.associatedFile = fromFile
        self.associatedFileField.setText(self.associatedFile.getPath())
        self.params = JSONObject()
        try:
            try:
                while (line = br.readLine()) != None:
                    pdata.append(line)
            finally:
                br.close()
            self.params = JSONObject(pdata.__str__())
            self.savedParams = self.params.__str__()
            self.setUIfromJSON()
            self.syncJSONtoUI()
        except Exception as e:
            e.printStackTrace()

    def saveParamsJSON(self, saveAs):
        """ generated source for method saveParamsJSON """
        try:
            if saveAs or self.associatedFile == None:
                fc.setFileFilter(PlayerFilter())
                if returnVal == JFileChooser.APPROVE_OPTION and fc.getSelectedFile() != None:
                    if toFile.__name__.contains("."):
                        self.associatedFile = File(toFile.getParentFile(), toFile.__name__.substring(0, toFile.__name__.lastIndexOf(".")) + ".player")
                    else:
                        self.associatedFile = File(toFile.getParentFile(), toFile.__name__ + ".player")
                    self.associatedFileField.setText(self.associatedFile.getPath())
                else:
                    return
            bw.write(self.params.__str__())
            bw.close()
            self.savedParams = self.params.__str__()
            self.syncJSONtoUI()
        except IOException as ie:
            ie.printStackTrace()

    def saveButtonMethod(self):
        """ generated source for method saveButtonMethod """
        return AbstractAction("Save")

    def saveAsButtonMethod(self):
        """ generated source for method saveAsButtonMethod """
        return AbstractAction("Save As")

    def loadButtonMethod(self):
        """ generated source for method loadButtonMethod """
        return AbstractAction("Load")

    class PlayerFilter(FileFilter):
        """ generated source for class PlayerFilter """
        def accept(self, f):
            """ generated source for method accept """
            if f.isDirectory():
                return True
            return f.__name__.endsWith(".player")

        def getDescription(self):
            """ generated source for method getDescription """
            return "GGP Players (*.player)"

