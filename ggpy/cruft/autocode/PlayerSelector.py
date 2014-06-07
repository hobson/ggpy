#!/usr/bin/env python
""" generated source for module PlayerSelector """
# package: org.ggp.base.util.ui
import java.awt.Color

import java.awt.Component

import java.awt.Graphics

import java.awt.image.BufferedImage

import javax.swing.ImageIcon

import javax.swing.JComboBox

import javax.swing.JLabel

import javax.swing.JList

import javax.swing.ListCellRenderer

import javax.swing.ListSelectionModel

import org.ggp.base.util.observer.Event

import org.ggp.base.util.observer.Observer

import org.ggp.base.util.presence.PlayerPresence

import org.ggp.base.util.presence.PlayerPresenceManager

import org.ggp.base.util.presence.PlayerPresenceManager.InvalidHostportException

class PlayerSelector(object):
    """ generated source for class PlayerSelector """
    thePresenceManager = PlayerPresenceManager()

    def __init__(self):
        """ generated source for method __init__ """
        self.thePresenceManager = PlayerPresenceManager()

    class PlayerPresenceLabel(JLabel, ListCellRenderer, str):
        """ generated source for class PlayerPresenceLabel """
        serialVersionUID = 1L
        maxLabelLength = int()

        def __init__(self, maxLabelLength):
            """ generated source for method __init__ """
            super(PlayerPresenceLabel, self).__init__()
            setOpaque(True)
            setHorizontalAlignment(CENTER)
            setVerticalAlignment(CENTER)
            self.maxLabelLength = maxLabelLength

        def getListCellRendererComponent(self, list_, value, index, isSelected, cellHasFocus):
            """ generated source for method getListCellRendererComponent """
            setHorizontalAlignment(JLabel.LEFT)
            if isSelected:
                setBackground(list_.getSelectionBackground())
                setForeground(list_.getSelectionForeground())
            else:
                setBackground(list_.getBackground())
                setForeground(list_.getForeground())
            if value == None:
                return self
            presence = self.thePresenceManager.getPresence(value.__str__())
            status = presence.getStatus()
            if status != None:
                status = status.lower()
            iconSize = 20
            img = BufferedImage(iconSize, iconSize, BufferedImage.TYPE_INT_RGB)
            g = img.getGraphics()
            g.setColor(getBackground())
            g.fillRect(0, 0, iconSize, iconSize)
            if status == None:
                g.setColor(Color.GRAY)
            elif status == "available":
                g.setColor(Color.GREEN)
            elif status == "busy":
                g.setColor(Color.ORANGE)
            elif status == "error":
                g.setColor(Color.BLACK)
            else:
                g.setColor(Color.MAGENTA)
            g.fillOval(3, 3, iconSize - 6, iconSize - 6)
            textLabel = presence.getHost() + ":" + presence.getPort()
            if presence.__name__ != None:
                textLabel = presence.__name__ + " (" + textLabel + ")"
            if self.maxLabelLength > len(textLabel):
                textLabel = textLabel.substring(0, self.maxLabelLength - 3) + "..."
            setIcon(ImageIcon(img))
            setText(textLabel)
            setFont(list_.getFont())
            return self

    class PlayerSelectorBox(JComboBox, str, Observer):
        """ generated source for class PlayerSelectorBox """
        serialVersionUID = 1L

        def __init__(self):
            """ generated source for method __init__ """
            super(PlayerSelectorBox, self).__init__()
            self.thePresenceManager.addObserver(self)
            setRenderer(self.PlayerPresenceLabel(20))
            addAllPlayerItems()

        def addAllPlayerItems(self):
            """ generated source for method addAllPlayerItems """
            for name in thePresenceManager.getSortedPlayerNames():
                addItem(name)

        def observe(self, event):
            """ generated source for method observe """
            if isinstance(event, (PlayerPresenceChanged, )):
                repaint()
                revalidate()
            elif isinstance(event, (PlayerPresenceAdded, )) or isinstance(event, (PlayerPresenceRemoved, )):
                removeAllItems()
                self.addAllPlayerItems()
                setSelectedItem(currentlySelected)
                repaint()
                revalidate()

    class PlayerSelectorList(JList, str, Observer):
        """ generated source for class PlayerSelectorList """
        serialVersionUID = 1L

        def __init__(self):
            """ generated source for method __init__ """
            super(PlayerSelectorList, self).__init__()
            self.thePresenceManager.addObserver(self)
            setCellRenderer(self.PlayerPresenceLabel(40))
            setSelectionMode(ListSelectionModel.SINGLE_SELECTION)
            setAllPlayerItems()

        def setAllPlayerItems(self):
            """ generated source for method setAllPlayerItems """
            setListData(self.thePresenceManager.getSortedPlayerNames().toArray([None]*0))

        def observe(self, event):
            """ generated source for method observe """
            if isinstance(event, (PlayerPresenceChanged, )):
                repaint()
                revalidate()
            elif isinstance(event, (PlayerPresenceAdded, )) or isinstance(event, (PlayerPresenceRemoved, )):
                self.setAllPlayerItems()
                setSelectedValue(currentlySelected, True)
                repaint()
                revalidate()

    def addPlayer(self, hostport):
        """ generated source for method addPlayer """
        self.thePresenceManager.addPlayer(hostport)

    def removePlayer(self, hostport):
        """ generated source for method removePlayer """
        self.thePresenceManager.removePlayer(hostport)

    def getPlayerPresence(self, name):
        """ generated source for method getPlayerPresence """
        return self.thePresenceManager.getPresence(name)

    def getPlayerSelectorBox(self):
        """ generated source for method getPlayerSelectorBox """
        return self.PlayerSelectorBox()

    def getPlayerSelectorList(self):
        """ generated source for method getPlayerSelectorList """
        return self.PlayerSelectorList()

