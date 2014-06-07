#!/usr/bin/env python
""" generated source for module GameRepository """
# package: org.ggp.base.util.game
import java.util.HashMap

import java.util.Map

import java.util.Set

# 
#  * Game repositories contain games, and provide two main services: you can
#  * query a repository to get a list of available games (by key), and given
#  * a key, you can look up the associated Game object.
#  *
#  * All queries to a game repository are cached, and the caching is handled
#  * in this abstract base class. Concrete subclasses will implement the actual
#  * behavior required for fetching games from the underlying repositories.
#  *
#  * @author Sam
#  
class GameRepository(object):
    """ generated source for class GameRepository """
    @classmethod
    def getDefaultRepository(cls):
        """ generated source for method getDefaultRepository """
        return CloudGameRepository("games.ggp.org/base")

    def getGame(self, theKey):
        """ generated source for method getGame """
        if not theGames.containsKey(theKey):
            if theGame != None:
                theGames.put(theKey, theGame)
        return theGames.get(theKey)

    def getGameKeys(self):
        """ generated source for method getGameKeys """
        if theGameKeys == None:
            theGameKeys = getUncachedGameKeys()
        return theGameKeys

    #  Abstract methods, for implementation classes.
    def getUncachedGame(self, theKey):
        """ generated source for method getUncachedGame """

    def getUncachedGameKeys(self):
        """ generated source for method getUncachedGameKeys """

    #  Cached values, lazily filled.
    theGameKeys = Set()
    theGames = HashMap()

