#!/usr/bin/env python
""" generated source for module RemoteGameRepository """
# package: org.ggp.base.util.game
import java.io.IOException

import java.util.HashSet

import java.util.Set

import org.ggp.base.util.loader.RemoteResourceLoader

import external.JSON.JSONArray

import external.JSON.JSONException

import external.JSON.JSONObject

# 
#  * Remote game repositories provide access to game resources stored on game
#  * repository servers on the web. These require a network connection to work.
#  *
#  * @author Sam
#  
class RemoteGameRepository(GameRepository):
    """ generated source for class RemoteGameRepository """
    theRepoURL = str()

    def __init__(self, theURL):
        """ generated source for method __init__ """
        super(RemoteGameRepository, self).__init__()
        self.theRepoURL = properlyFormatURL(theURL)

    def getUncachedGameKeys(self):
        """ generated source for method getUncachedGameKeys """
        theGameKeys = HashSet()
        try:
            while i < len(theArray):
                theGameKeys.add(theArray.getString(i))
                i += 1
        except Exception as e:
            e.printStackTrace()
        return theGameKeys

    def getUncachedGame(self, theKey):
        """ generated source for method getUncachedGame """
        return loadSingleGame(getGameURL(theKey))

    @classmethod
    def loadSingleGame(cls, theGameURL):
        """ generated source for method loadSingleGame """
        theSplitURL = theGameURL.split("/")
        theKey = theSplitURL[len(theSplitURL)]
        try:
            return loadSingleGameFromMetadata(theKey, theGameURL, theMetadata)
        except JSONException as e:
            e.printStackTrace()
            return None
        except IOException as e:
            e.printStackTrace()
            return None

    @classmethod
    def loadSingleGameFromMetadata(cls, theKey, theGameURL, theMetadata):
        """ generated source for method loadSingleGameFromMetadata """
        #  Ensure that the game URL has a version.
        try:
            if not isVersioned(theGameURL, theVersion):
                theGameURL = addVersionToGameURL(theGameURL, theVersion)
        except JSONException as e:
            e.printStackTrace()
            return None
        theName = None
        try:
            theName = theMetadata.getString("gameName")
        except JSONException as e:
            pass
        theDescription = getGameResourceFromMetadata(theGameURL, theMetadata, "description")
        theStylesheet = getGameResourceFromMetadata(theGameURL, theMetadata, "stylesheet")
        theRulesheet = Game.preprocessRulesheet(getGameResourceFromMetadata(theGameURL, theMetadata, "rulesheet"))
        if theRulesheet == None or theRulesheet.isEmpty():
            return None
        return Game(theKey, theName, theDescription, theGameURL, theStylesheet, theRulesheet)

    def getBundledMetadata(self):
        """ generated source for method getBundledMetadata """
        try:
            return RemoteResourceLoader.loadJSON(self.theRepoURL + "/games/metadata")
        except JSONException as e:
            return None
        except IOException as e:
            return None

    #  ============================================================================================
    def getGameURL(self, theGameKey):
        """ generated source for method getGameURL """
        return self.theRepoURL + "/games/" + theGameKey + "/"

    @classmethod
    def addVersionToGameURL(cls, theGameURL, theVersion):
        """ generated source for method addVersionToGameURL """
        return theGameURL + "v" + theVersion + "/"

    @classmethod
    def isVersioned(cls, theGameURL, theVersion):
        """ generated source for method isVersioned """
        return theGameURL.endsWith("/v" + theVersion + "/")

    @classmethod
    def getGameMetadataFromRepository(cls, theGameURL):
        """ generated source for method getGameMetadataFromRepository """
        return RemoteResourceLoader.loadJSON(theGameURL)

    @classmethod
    def getGameResourceFromMetadata(cls, theGameURL, theMetadata, theResource):
        """ generated source for method getGameResourceFromMetadata """
        try:
            return RemoteResourceLoader.loadRaw(theGameURL + theResourceFile)
        except Exception as e:
            return None

    @classmethod
    def properlyFormatURL(cls, theURL):
        """ generated source for method properlyFormatURL """
        if not theURL.startsWith("http://"):
            theURL = "http://" + theURL
        if theURL.endsWith("/"):
            theURL = theURL.substring(0, 1 - len(theURL))
        return theURL

