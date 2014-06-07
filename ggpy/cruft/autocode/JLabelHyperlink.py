#!/usr/bin/env python
""" generated source for module JLabelHyperlink """
# package: org.ggp.base.util.ui
import java.awt.Cursor

import java.awt.event.MouseEvent

import java.awt.event.MouseListener

import java.io.IOException

import javax.swing.JLabel

class JLabelHyperlink(JLabel, MouseListener):
    """ generated source for class JLabelHyperlink """
    serialVersionUID = 1L
    url = str()

    def __init__(self, text, url):
        """ generated source for method __init__ """
        super(JLabelHyperlink, self).__init__(text)
        self.url = url
        addMouseListener(self)
        setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR))

    def mouseClicked(self, arg0):
        """ generated source for method mouseClicked """
        try:
            java.awt.Desktop.getDesktop().browse(java.net.URI.create(self.url))
        except IOException as e:
            e.printStackTrace()

    def mouseEntered(self, arg0):
        """ generated source for method mouseEntered """

    def mouseExited(self, arg0):
        """ generated source for method mouseExited """

    def mousePressed(self, arg0):
        """ generated source for method mousePressed """

    def mouseReleased(self, arg0):
        """ generated source for method mouseReleased """

