#!/usr/bin/env python
""" generated source for module ConsolePanel """
# package: org.ggp.base.util.ui
import java.awt.BorderLayout

import java.awt.Color

import java.io.IOException

import java.io.OutputStream

import java.io.PrintStream

import javax.swing.JPanel

import javax.swing.JScrollPane

import javax.swing.JTextArea

import javax.swing.SwingUtilities

import javax.swing.border.TitledBorder

# 
#  * ConsolePanel implements a light-weight panel that shows all of the
#  * messages being send to stdout and stderr. This can be useful in a graphical
#  * application that also needs to alert the user about warnings that occur in
#  * lower-level components, like the network communication stack.
#  
@SuppressWarnings("serial")
class ConsolePanel(JPanel):
    """ generated source for class ConsolePanel """
    def __init__(self):
        """ generated source for method __init__ """
        super(ConsolePanel, self).__init__(BorderLayout())
        #  Create an output console.
        outputConsole = JTextArea()
        outputConsole.setEditable(False)
        outputConsole.setForeground(Color(125, 0, 0))
        outputConsole.setText("(Console output will be displayed here.)\n\n")
        outputConsolePane = JScrollPane(outputConsole)
        setBorder(TitledBorder("Java Console:"))
        add(outputConsolePane, BorderLayout.CENTER)
        validate()
        #  Send the standard out and standard error streams
        #  to this panel, instead.
        out = OutputStream()
        System.setOut(PrintStream(out, True))
        System.setErr(PrintStream(out, True))

    outputConsole = JTextArea()

    def updateTextArea(self, text):
        """ generated source for method updateTextArea """
        SwingUtilities.invokeLater(Runnable())

