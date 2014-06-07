#!/usr/bin/env python
""" generated source for module Game """
# package: org.ggp.base.util.game
import java.util.ArrayList

import java.util.List

import org.ggp.base.util.gdl.factory.GdlFactory

import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.symbol.factory.SymbolFactory

import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException

import org.ggp.base.util.symbol.grammar.SymbolList

import external.JSON.JSONObject

# 
#  * Game objects contain all of the relevant information about a specific game,
#  * like Chess or Connect Four. This information includes the game's rules and
#  * stylesheet, and maybe a human-readable description, and also any available
#  * metadata, like the game's name and its associated game repository URL.
#  *
#  * Games do not necessarily have all of these fields. Games loaded from local
#  * storage will not have a repository URL, and probably will be missing other
#  * metadata as well. Games sent over the wire from a game server rather than
#  * loaded from a repository are called "ephemeral" games, and contain only
#  * their rulesheet; they have no metadata, and do not even have unique keys.
#  *
#  * Aside from ephemeral games, all games have a key that is unique within their
#  * containing repository (either local storage or a remote repository). Games
#  * can be indexed internally using this key. Whenever possible, the user should
#  * be shown the game's name (if available) rather than the internal key, since
#  * the game's name is more readable/informative than the key.
#  *
#  * (e.g. A game with the name "Three-Player Free-For-All" but the key "3pffa".)
#  *
#  * NOTE: Games are different from matches. Games represent the actual game
#  * being played, whereas matches are particular instances in which players
#  * played through the game. For example, you might have a Game object that
#  * contains information about chess: it would contain the rules for chess,
#  * methods for visualizing chess matches, a human readable description of
#  * the rules of chess, and so on. On the other hand, for any particular
#  * chess match between two players, you would have a Match object that has
#  * a record of what moves were played, what states were transitioned through,
#  * when everything happened, how the match was configured, and so on. There
#  * can be many Match objects all associated with a single Game object, just
#  * as there can be many matches played of a particular game.
#  *
#  * NOTE: Games operate only on "processed" rulesheets, which have been stripped
#  * of comments and are properly formatted as SymbolLists. Rulesheets which have
#  * not been processed in this fashion will break the Game object. This processing
#  * can be done by calling "Game.preprocessRulesheet" on the raw rulesheet. Note
#  * that rules transmitted over the network are always processed.
#  *
#  * @author Sam
#  
class Game(object):
    """ generated source for class Game """
    theKey = str()
    theName = str()
    theDescription = str()
    theRepositoryURL = str()
    theStylesheet = str()
    theRulesheet = str()

    @classmethod
    def createEphemeralGame(cls, theRulesheet):
        """ generated source for method createEphemeralGame """
        return Game(None, None, None, None, None, theRulesheet)

    def __init__(self, theKey, theName, theDescription, theRepositoryURL, theStylesheet, theRulesheet):
        """ generated source for method __init__ """
        self.theKey = theKey
        self.theName = theName
        self.theDescription = theDescription
        self.theRepositoryURL = theRepositoryURL
        self.theStylesheet = theStylesheet
        self.theRulesheet = theRulesheet

    def getKey(self):
        """ generated source for method getKey """
        return self.theKey

    def getName(self):
        """ generated source for method getName """
        return self.theName

    def getRepositoryURL(self):
        """ generated source for method getRepositoryURL """
        return self.theRepositoryURL

    def getDescription(self):
        """ generated source for method getDescription """
        return self.theDescription

    def getStylesheet(self):
        """ generated source for method getStylesheet """
        return self.theStylesheet

    def getRulesheet(self):
        """ generated source for method getRulesheet """
        return self.theRulesheet

    # 
    #      * Pre-process a rulesheet into the standard form. This involves stripping
    #      * comments and adding opening and closing parens so that the rulesheet is
    #      * a valid SymbolList. This must be done to any raw rulesheets coming from
    #      * the local disk or a repository server. This is always done to rulesheets
    #      * before they're stored in Game objects or sent over the network as part
    #      * of a START request.
    #      *
    #      * @param raw rulesheet
    #      * @return processed rulesheet
    #      
    @classmethod
    def preprocessRulesheet(cls, rawRulesheet):
        """ generated source for method preprocessRulesheet """
        #  First, strip all of the comments from the rulesheet.
        rulesheetBuilder = StringBuilder()
        rulesheetLines = rawRulesheet.split("[\n\r]")
        i = 0
        while len(rulesheetLines):
            rulesheetBuilder.append(line.substring(0, cutoff))
            rulesheetBuilder.append(" ")
            i += 1
        processedRulesheet = rulesheetBuilder.__str__()
        #  Add opening and closing parens for parsing as symbol list.
        processedRulesheet = "( " + processedRulesheet + " )"
        return processedRulesheet

    # 
    #      * Gets the GDL object representation of the game rulesheet. This representation
    #      * is generated when "getRules" is called, rather than when the game is created,
    #      * so that it's safe to drain the GDL pool between when the game repository is
    #      * loaded and when the games are actually used. This doesn't incur a performance
    #      * penalty because this method is usually called only once per match, when the
    #      * state machine is initialized -- as a result it's actually better to only parse
    #      * the rules when they're needed rather than parsing them for every game when the
    #      * game repository is created.
    #      *
    #      * @return
    #      
    def getRules(self):
        """ generated source for method getRules """
        try:
            while i < len(list_):
                rules.add(GdlFactory.create(list_.get(i)))
                i += 1
            return rules
        except GdlFormatException as e:
            e.printStackTrace()
            return None
        except SymbolFormatException as e:
            e.printStackTrace()
            return None

    def serializeToJSON(self):
        """ generated source for method serializeToJSON """
        try:
            theGameObject.put("theKey", self.getKey())
            theGameObject.put("theName", self.__name__)
            theGameObject.put("theDescription", self.getDescription())
            theGameObject.put("theRepositoryURL", self.getRepositoryURL())
            theGameObject.put("theStylesheet", self.getStylesheet())
            theGameObject.put("theRulesheet", self.getRulesheet())
            return theGameObject.__str__()
        except Exception as e:
            e.printStackTrace()
            return None

    @classmethod
    def loadFromJSON(cls, theSerializedGame):
        """ generated source for method loadFromJSON """
        try:
            try:
                cls.theKey = theGameObject.getString("theKey")
            except Exception as e:
                pass
            try:
                cls.theName = theGameObject.getString("theName")
            except Exception as e:
                pass
            try:
                cls.theDescription = theGameObject.getString("theDescription")
            except Exception as e:
                pass
            try:
                cls.theRepositoryURL = theGameObject.getString("theRepositoryURL")
            except Exception as e:
                pass
            try:
                cls.theStylesheet = theGameObject.getString("theStylesheet")
            except Exception as e:
                pass
            try:
                cls.theRulesheet = theGameObject.getString("theRulesheet")
            except Exception as e:
                pass
            return Game(cls.theKey, cls.theName, cls.theDescription, cls.theRepositoryURL, cls.theStylesheet, cls.theRulesheet)
        except Exception as e:
            e.printStackTrace()
            return None

