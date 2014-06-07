#!/usr/bin/env python
""" generated source for module GameSelector """
# package: org.ggp.base.util.ui
import java.awt.event.ActionEvent

import java.awt.event.ActionListener

import java.util.ArrayList

import java.util.Collections

import java.util.HashMap

import java.util.List

import java.util.Map

import javax.swing.JComboBox

import org.ggp.base.util.game.CloudGameRepository

import org.ggp.base.util.game.Game

import org.ggp.base.util.game.GameRepository

import org.ggp.base.util.game.LocalGameRepository

# 
#  * GameSelector is a pair of widgets for selecting a game repository
#  * and then choosing a game from that game repository. Currently this
#  * is a little rough, and could use some polish, but it provides all
#  * of the important functionality: you can load games both from local
#  * storage and from game repositories on the web.
#  *
#  * @author Sam Schreiber
#  
class GameSelector(ActionListener):
    """ generated source for class GameSelector """
    theGameList = JComboBox()
    theRepositoryList = JComboBox()
    theSelectedRepository = GameRepository()
    theCachedRepositories = Map()

    class NamedItem(object):
        """ generated source for class NamedItem """
        theKey = str()
        theName = str()

        def __init__(self, theKey, theName):
            """ generated source for method __init__ """
            self.theKey = theKey
            self.theName = theName

        def __str__(self):
            """ generated source for method toString """
            return self.theName

    def __init__(self):
        """ generated source for method __init__ """
        super(GameSelector, self).__init__()
        self.theGameList = JComboBox()
        self.theGameList.addActionListener(self)
        self.theRepositoryList = JComboBox()
        self.theRepositoryList.addActionListener(self)
        self.theCachedRepositories = HashMap()
        self.theRepositoryList.addItem("games.ggp.org/base")
        self.theRepositoryList.addItem("games.ggp.org/dresden")
        self.theRepositoryList.addItem("games.ggp.org/stanford")
        self.theRepositoryList.addItem("Local Game Repository")

    def actionPerformed(self, e):
        """ generated source for method actionPerformed """
        if e.getSource() == self.theRepositoryList:
            if self.theCachedRepositories.containsKey(theRepositoryName):
                self.theSelectedRepository = self.theCachedRepositories.get(theRepositoryName)
            else:
                if theRepositoryName == "Local Game Repository":
                    self.theSelectedRepository = LocalGameRepository()
                else:
                    self.theSelectedRepository = CloudGameRepository(theRepositoryName)
                self.theCachedRepositories.put(theRepositoryName, self.theSelectedRepository)
            repopulateGameList()

    def getSelectedGameRepository(self):
        """ generated source for method getSelectedGameRepository """
        return self.theSelectedRepository

    def repopulateGameList(self):
        """ generated source for method repopulateGameList """
        theRepository = self.getSelectedGameRepository()
        theKeyList = ArrayList(theRepository.getGameKeys())
        Collections.sort(theKeyList)
        self.theGameList.removeAllItems()
        for theKey in theKeyList:
            if theGame == None:
                continue 
            if theName == None:
                theName = theKey
            if 24 > len(theName):
                theName = theName.substring(0, 24) + "..."
            self.theGameList.addItem(self.NamedItem(theKey, theName))

    def getRepositoryList(self):
        """ generated source for method getRepositoryList """
        return self.theRepositoryList

    def getGameList(self):
        """ generated source for method getGameList """
        return self.theGameList

    def getSelectedGame(self):
        """ generated source for method getSelectedGame """
        try:
            return self.getSelectedGameRepository().getGame((self.theGameList.getSelectedItem()).theKey)
        except Exception as e:
            return None

