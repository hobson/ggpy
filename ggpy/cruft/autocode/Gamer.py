#!/usr/bin/env python
""" generated source for module Gamer """
# package: org.ggp.base.player.gamer
import java.util.ArrayList

import java.util.List

import org.ggp.base.apps.player.config.ConfigPanel

import org.ggp.base.apps.player.config.EmptyConfigPanel

import org.ggp.base.apps.player.detail.DetailPanel

import org.ggp.base.apps.player.detail.EmptyDetailPanel

import org.ggp.base.player.gamer.exception.AbortingException

import org.ggp.base.player.gamer.exception.GamePreviewException

import org.ggp.base.player.gamer.exception.MetaGamingException

import org.ggp.base.player.gamer.exception.MoveSelectionException

import org.ggp.base.player.gamer.exception.StoppingException

import org.ggp.base.util.game.Game

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.match.Match

import org.ggp.base.util.observer.Event

import org.ggp.base.util.observer.Observer

import org.ggp.base.util.observer.Subject

# 
#  * The Gamer class defines methods for both meta-gaming and move selection in a
#  * pre-specified amount of time. The Gamer class is based on the <i>algorithm</i>
#  * design pattern.
#  
class Gamer(Subject):
    """ generated source for class Gamer """
    match = Match()
    roleName = GdlConstant()

    def __init__(self):
        """ generated source for method __init__ """
        super(Gamer, self).__init__()
        observers = ArrayList()
        #  When not playing a match, the variables 'match'
        #  and 'roleName' should be NULL. This indicates that
        #  the player is available for starting a new match.
        self.match = None
        self.roleName = None

    #  The following values are recommendations to the implementations
    # 	 * for the minimum length of time to leave between the stated timeout
    # 	 * and when you actually return from metaGame and selectMove. They are
    # 	 * stored here so they can be shared amongst all Gamers. 
    PREFERRED_METAGAME_BUFFER = 3900
    PREFERRED_PLAY_BUFFER = 1900

    #  ==== The Gaming Algorithms ====
    def metaGame(self, timeout):
        """ generated source for method metaGame """

    def selectMove(self, timeout):
        """ generated source for method selectMove """

    #  Note that the match's goal values will not necessarily be known when
    # 	 * stop() is called, as we only know the final set of moves and haven't
    # 	 * interpreted them yet. To get the final goal values, process the final
    # 	 * moves of the game.
    # 	 
    def stop(self):
        """ generated source for method stop """

    #  Cleanly stop playing the match
    def abort(self):
        """ generated source for method abort """

    #  Abruptly stop playing the match
    def preview(self, g, timeout):
        """ generated source for method preview """

    #  Preview a game
    #  ==== Gamer Profile and Configuration ====
    def getName(self):
        """ generated source for method getName """

    def getSpecies(self):
        """ generated source for method getSpecies """
        return None

    def isComputerPlayer(self):
        """ generated source for method isComputerPlayer """
        return True

    def getConfigPanel(self):
        """ generated source for method getConfigPanel """
        return EmptyConfigPanel()

    def getDetailPanel(self):
        """ generated source for method getDetailPanel """
        return EmptyDetailPanel()

    #  ==== Accessors ====
    def getMatch(self):
        """ generated source for method getMatch """
        return self.match

    def setMatch(self, match):
        """ generated source for method setMatch """
        self.match = match

    def getRoleName(self):
        """ generated source for method getRoleName """
        return self.roleName

    def setRoleName(self, roleName):
        """ generated source for method setRoleName """
        self.roleName = roleName

    #  ==== Observer Stuff ====
    observers = List()

    def addObserver(self, observer):
        """ generated source for method addObserver """
        self.observers.add(observer)

    def notifyObservers(self, event):
        """ generated source for method notifyObservers """
        for observer in observers:
            observer.observe(event)

