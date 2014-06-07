#!/usr/bin/env python
""" generated source for module Match """
# package: org.ggp.base.util.match
import java.util.ArrayList

import java.util.Date

import java.util.HashSet

import java.util.List

import java.util.Random

import java.util.Set

import org.ggp.base.util.crypto.BaseCryptography.EncodedKeyPair

import org.ggp.base.util.crypto.SignableJSON

import org.ggp.base.util.game.Game

import org.ggp.base.util.game.RemoteGameRepository

import org.ggp.base.util.gdl.factory.GdlFactory

import org.ggp.base.util.gdl.factory.exceptions.GdlFormatException

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.scrambler.GdlScrambler

import org.ggp.base.util.gdl.scrambler.MappingGdlScrambler

import org.ggp.base.util.gdl.scrambler.NoOpGdlScrambler

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.statemachine.Role

import org.ggp.base.util.symbol.factory.SymbolFactory

import org.ggp.base.util.symbol.factory.exceptions.SymbolFormatException

import org.ggp.base.util.symbol.grammar.SymbolList

import external.JSON.JSONArray

import external.JSON.JSONException

import external.JSON.JSONObject

# 
#  * Match encapsulates all of the information relating to a single match.
#  * A match is a single play through a game, with a complete history that
#  * lists what move each player made at each step through the match. This
#  * also includes other relevant metadata about the match, including some
#  * unique identifiers, configuration information, and so on.
#  *
#  * NOTE: Match objects created by a player, representing state read from
#  * a server, are not completely filled out. For example, they only get an
#  * ephemeral Game object, which has a rulesheet but no key or metadata.
#  * Gamers which do not derive from StateMachineGamer also do not keep any
#  * information on what states have been observed, because (somehow) they
#  * are representing games without using state machines. In general, these
#  * player-created Match objects shouldn't be sent out into the ecosystem.
#  *
#  * @author Sam
#  
class Match(object):
    """ generated source for class Match """
    matchId = str()
    randomToken = str()
    spectatorAuthToken = str()
    playClock = int()
    startClock = int()
    previewClock = int()
    startTime = Date()
    theGame = Game()
    moveHistory = List()
    stateHistory = List()
    errorHistory = List()
    stateTimeHistory = List()
    isCompleted = bool()
    isAborted = bool()
    goalValues = List()
    numRoles = int()
    theCryptographicKeys = EncodedKeyPair()
    thePlayerNamesFromHost = List()
    isPlayerHuman = List()
    theGdlScrambler = NoOpGdlScrambler()

    @overloaded
    def __init__(self, matchId, previewClock, startClock, playClock, theGame):
        """ generated source for method __init__ """
        self.matchId = matchId
        self.previewClock = previewClock
        self.startClock = startClock
        self.playClock = playClock
        self.theGame = theGame
        self.startTime = Date()
        self.randomToken = getRandomString(32)
        self.spectatorAuthToken = getRandomString(12)
        self.isCompleted = False
        self.isAborted = False
        self.numRoles = Role.computeRoles(theGame.getRules()).size()
        self.moveHistory = ArrayList()
        self.stateHistory = ArrayList()
        self.stateTimeHistory = ArrayList()
        self.errorHistory = ArrayList()
        self.goalValues = ArrayList()

    @__init__.register(object, str, Game, str)
    def __init___0(self, theJSON, theGame, authToken):
        """ generated source for method __init___0 """
        theMatchObject = JSONObject(theJSON)
        self.matchId = theMatchObject.getString("matchId")
        self.startClock = theMatchObject.getInt("startClock")
        self.playClock = theMatchObject.getInt("playClock")
        if theGame == None:
            self.theGame = RemoteGameRepository.loadSingleGame(theMatchObject.getString("gameMetaURL"))
            if self.theGame == None:
                raise RuntimeException("Could not find metadata for game referenced in Match object: " + theMatchObject.getString("gameMetaURL"))
        else:
            self.theGame = theGame
        if theMatchObject.has("previewClock"):
            self.previewClock = theMatchObject.getInt("previewClock")
        else:
            self.previewClock = -1
        self.startTime = Date(theMatchObject.getLong("startTime"))
        self.randomToken = theMatchObject.getString("randomToken")
        self.spectatorAuthToken = authToken
        self.isCompleted = theMatchObject.getBoolean("isCompleted")
        if theMatchObject.has("isAborted"):
            self.isAborted = theMatchObject.getBoolean("isAborted")
        else:
            self.isAborted = False
        self.numRoles = Role.computeRoles(self.theGame.getRules()).size()
        self.moveHistory = ArrayList()
        self.stateHistory = ArrayList()
        self.stateTimeHistory = ArrayList()
        self.errorHistory = ArrayList()
        theMoves = theMatchObject.getJSONArray("moves")
        i = 0
        while i < len(theMoves):
            while j < len(moveElements):
                theMove.add(GdlFactory.createTerm(moveElements.getString(j)))
                j += 1
            self.moveHistory.add(theMove)
            i += 1
        theStates = theMatchObject.getJSONArray("states")
        i = 0
        while i < len(theStates):
            while j < len(stateElements):
                theState.add(GdlFactory.create("( true " + stateElements.get(j).__str__() + " )"))
                j += 1
            self.stateHistory.add(theState)
            i += 1
        theStateTimes = theMatchObject.getJSONArray("stateTimes")
        i = 0
        while i < len(theStateTimes):
            self.stateTimeHistory.add(Date(theStateTimes.getLong(i)))
            i += 1
        if theMatchObject.has("errors"):
            while i < len(theErrors):
                while j < len(errorElements):
                    theMoveErrors.add(errorElements.getString(j))
                    j += 1
                self.errorHistory.add(theMoveErrors)
                i += 1
        self.goalValues = ArrayList()
        try:
            while i < len(theGoalValues):
                self.goalValues.add(theGoalValues.getInt(i))
                i += 1
        except JSONException as e:
            pass
        #  TODO: Add a way to recover cryptographic public keys and signatures.
        #  Or, perhaps loading a match into memory for editing should strip those?
        if theMatchObject.has("playerNamesFromHost"):
            self.thePlayerNamesFromHost = ArrayList()
            while i < len(thePlayerNames):
                self.thePlayerNamesFromHost.add(thePlayerNames.getString(i))
                i += 1
        if theMatchObject.has("isPlayerHuman"):
            self.isPlayerHuman = ArrayList()
            while i < len(isPlayerHumanArray):
                self.isPlayerHuman.add(isPlayerHumanArray.getBoolean(i))
                i += 1

    #  Mutators 
    def setCryptographicKeys(self, k):
        """ generated source for method setCryptographicKeys """
        self.theCryptographicKeys = k

    def enableScrambling(self):
        """ generated source for method enableScrambling """
        self.theGdlScrambler = MappingGdlScrambler(Random(self.startTime.getTime()))
        for rule in theGame.getRules():
            self.theGdlScrambler.scramble(rule)

    def setPlayerNamesFromHost(self, thePlayerNames):
        """ generated source for method setPlayerNamesFromHost """
        self.thePlayerNamesFromHost = thePlayerNames

    def getPlayerNamesFromHost(self):
        """ generated source for method getPlayerNamesFromHost """
        return self.thePlayerNamesFromHost

    def setWhichPlayersAreHuman(self, isPlayerHuman):
        """ generated source for method setWhichPlayersAreHuman """
        self.isPlayerHuman = isPlayerHuman

    def appendMoves(self, moves):
        """ generated source for method appendMoves """
        self.moveHistory.add(moves)

    def appendMoves2(self, moves):
        """ generated source for method appendMoves2 """
        #  NOTE: This is appendMoves2 because it Java can't handle two
        #  appendMove methods that both take List objects with different
        #  templatized parameters.
        theMoves = ArrayList()
        for m in moves:
            theMoves.add(m.getContents())
        self.appendMoves(theMoves)

    def appendState(self, state):
        """ generated source for method appendState """
        self.stateHistory.add(state)
        self.stateTimeHistory.add(Date())

    def appendErrors(self, errors):
        """ generated source for method appendErrors """
        self.errorHistory.add(errors)

    def appendNoErrors(self):
        """ generated source for method appendNoErrors """
        theNoErrors = ArrayList()
        i = 0
        while i < self.numRoles:
            theNoErrors.add("")
            i += 1
        self.errorHistory.add(theNoErrors)

    def markCompleted(self, theGoalValues):
        """ generated source for method markCompleted """
        self.isCompleted = True
        if theGoalValues != None:
            self.goalValues.addAll(theGoalValues)

    def markAborted(self):
        """ generated source for method markAborted """
        self.isAborted = True

    #  Complex accessors 
    def toJSON(self):
        """ generated source for method toJSON """
        theJSON = JSONObject()
        try:
            theJSON.put("matchId", self.matchId)
            theJSON.put("randomToken", self.randomToken)
            theJSON.put("startTime", self.startTime.getTime())
            theJSON.put("gameMetaURL", getGameRepositoryURL())
            theJSON.put("isCompleted", self.isCompleted)
            theJSON.put("isAborted", self.isAborted)
            theJSON.put("states", JSONArray(renderArrayAsJSON(renderStateHistory(self.stateHistory), True)))
            theJSON.put("moves", JSONArray(renderArrayAsJSON(renderMoveHistory(self.moveHistory), False)))
            theJSON.put("stateTimes", JSONArray(renderArrayAsJSON(self.stateTimeHistory, False)))
            if len(self.errorHistory) > 0:
                theJSON.put("errors", JSONArray(renderArrayAsJSON(renderErrorHistory(self.errorHistory), False)))
            if len(self.goalValues) > 0:
                theJSON.put("goalValues", self.goalValues)
            theJSON.put("previewClock", self.previewClock)
            theJSON.put("startClock", self.startClock)
            theJSON.put("playClock", self.playClock)
            if self.thePlayerNamesFromHost != None:
                theJSON.put("playerNamesFromHost", self.thePlayerNamesFromHost)
            if self.isPlayerHuman != None:
                theJSON.put("isPlayerHuman", self.isPlayerHuman)
            theJSON.put("scrambled", self.theGdlScrambler.scrambles() if self.theGdlScrambler != None else False)
        except JSONException as e:
            return None
        if self.theCryptographicKeys != None:
            try:
                SignableJSON.signJSON(theJSON, self.theCryptographicKeys.thePublicKey, self.theCryptographicKeys.thePrivateKey)
                if not SignableJSON.isSignedJSON(theJSON):
                    raise Exception("Could not recognize signed match: " + theJSON)
                if not SignableJSON.verifySignedJSON(theJSON):
                    raise Exception("Could not verify signed match: " + theJSON)
            except Exception as e:
                System.err.println(e)
                theJSON.remove("matchHostPK")
                theJSON.remove("matchHostSignature")
        return theJSON.__str__()

    def toXML(self):
        """ generated source for method toXML """
        try:
            theXML.append("<match>")
            for key in JSONObject.getNames(theJSON):
                if isinstance(value, (JSONObject, )):
                    raise RuntimeException("Unexpected embedded JSONObject in match JSON with tag " + key + "; could not convert to XML.")
                elif not (isinstance(value, (JSONArray, ))):
                    theXML.append(renderLeafXML(key, theJSON.get(key)))
                elif key == "states":
                    theXML.append(renderStateHistoryXML(self.stateHistory))
                elif key == "moves":
                    theXML.append(renderMoveHistoryXML(self.moveHistory))
                elif key == "errors":
                    theXML.append(renderErrorHistoryXML(self.errorHistory))
                else:
                    theXML.append(renderArrayXML(key, value))
            theXML.append("</match>")
            return theXML.__str__()
        except JSONException as je:
            return None

    def getMostRecentMoves(self):
        """ generated source for method getMostRecentMoves """
        if len(self.moveHistory) == 0:
            return None
        return self.moveHistory.get(len(self.moveHistory) - 1)

    def getMostRecentState(self):
        """ generated source for method getMostRecentState """
        if len(self.stateHistory) == 0:
            return None
        return self.stateHistory.get(len(self.stateHistory) - 1)

    def getGameRepositoryURL(self):
        """ generated source for method getGameRepositoryURL """
        return getGame().getRepositoryURL()

    def __str__(self):
        """ generated source for method toString """
        return self.toJSON()

    #  Simple accessors 
    def getMatchId(self):
        """ generated source for method getMatchId """
        return self.matchId

    def getRandomToken(self):
        """ generated source for method getRandomToken """
        return self.randomToken

    def getSpectatorAuthToken(self):
        """ generated source for method getSpectatorAuthToken """
        return self.spectatorAuthToken

    def getGame(self):
        """ generated source for method getGame """
        return self.theGame

    def getMoveHistory(self):
        """ generated source for method getMoveHistory """
        return self.moveHistory

    def getStateHistory(self):
        """ generated source for method getStateHistory """
        return self.stateHistory

    def getStateTimeHistory(self):
        """ generated source for method getStateTimeHistory """
        return self.stateTimeHistory

    def getErrorHistory(self):
        """ generated source for method getErrorHistory """
        return self.errorHistory

    def getPreviewClock(self):
        """ generated source for method getPreviewClock """
        return self.previewClock

    def getPlayClock(self):
        """ generated source for method getPlayClock """
        return self.playClock

    def getStartClock(self):
        """ generated source for method getStartClock """
        return self.startClock

    def getStartTime(self):
        """ generated source for method getStartTime """
        return self.startTime

    def isCompleted(self):
        """ generated source for method isCompleted """
        return self.isCompleted

    def isAborted(self):
        """ generated source for method isAborted """
        return self.isAborted

    def getGoalValues(self):
        """ generated source for method getGoalValues """
        return self.goalValues

    def getGdlScrambler(self):
        """ generated source for method getGdlScrambler """
        return self.theGdlScrambler

    #  Static methods 
    @classmethod
    def getRandomString(cls, nLength):
        """ generated source for method getRandomString """
        theGenerator = Random()
        theString = ""
        i = 0
        while i < nLength:
            if nVal < 26:
                theString += str(('a' + nVal))
            elif nVal < 52:
                theString += str(('A' + (nVal - 26)))
            elif nVal < 62:
                theString += str(('0' + (nVal - 52)))
            i += 1
        return theString

    #  JSON rendering methods 
    @classmethod
    def renderArrayAsJSON(cls, theList, useQuotes):
        """ generated source for method renderArrayAsJSON """
        s = "["
        i = 0
        while i < len(theList):
            #  AppEngine-specific, not needed yet: if (o instanceof Text) o = ((Text)o).getValue();
            if isinstance(o, (Date, )):
                o = (o).getTime()
            if useQuotes:
                s += "\""
            s += o.__str__()
            if useQuotes:
                s += "\""
            if i < len(theList) - 1:
                s += ", "
            i += 1
        return s + "]"

    @classmethod
    def renderStateHistory(cls, stateHistory):
        """ generated source for method renderStateHistory """
        renderedStates = ArrayList()
        for aState in stateHistory:
            renderedStates.add(renderStateAsSymbolList(aState))
        return renderedStates

    @classmethod
    def renderMoveHistory(cls, moveHistory):
        """ generated source for method renderMoveHistory """
        renderedMoves = ArrayList()
        for aMove in moveHistory:
            renderedMoves.add(cls.renderArrayAsJSON(aMove, True))
        return renderedMoves

    @classmethod
    def renderErrorHistory(cls, errorHistory):
        """ generated source for method renderErrorHistory """
        renderedErrors = ArrayList()
        for anError in errorHistory:
            renderedErrors.add(cls.renderArrayAsJSON(anError, True))
        return renderedErrors

    @classmethod
    def renderStateAsSymbolList(cls, theState):
        """ generated source for method renderStateAsSymbolList """
        #  Strip out the TRUE proposition, since those are implied for states.
        s = "( "
        for sent in theState:
            s += sentString.substring(6, 2 - len(sentString)).trim() + " "
        return s + ")"

    #  XML Rendering methods -- these are horribly inefficient and are included only for legacy/standards compatibility 
    @classmethod
    def renderLeafXML(cls, tagName, value):
        """ generated source for method renderLeafXML """
        return "<" + tagName + ">" + value.__str__() + "</" + tagName + ">"

    @classmethod
    def renderMoveHistoryXML(cls, moveHistory):
        """ generated source for method renderMoveHistoryXML """
        theXML = StringBuilder()
        theXML.append("<history>")
        for move in moveHistory:
            theXML.append("<move>")
            for action in move:
                theXML.append(cls.renderLeafXML("action", renderGdlToXML(action)))
            theXML.append("</move>")
        theXML.append("</history>")
        return theXML.__str__()

    @classmethod
    def renderErrorHistoryXML(cls, errorHistory):
        """ generated source for method renderErrorHistoryXML """
        theXML = StringBuilder()
        theXML.append("<errorHistory>")
        for errors in errorHistory:
            theXML.append("<errors>")
            for error in errors:
                theXML.append(cls.renderLeafXML("error", error))
            theXML.append("</errors>")
        theXML.append("</errorHistory>")
        return theXML.__str__()

    @classmethod
    def renderStateHistoryXML(cls, stateHistory):
        """ generated source for method renderStateHistoryXML """
        theXML = StringBuilder()
        theXML.append("<herstory>")
        for state in stateHistory:
            theXML.append(renderStateXML(state))
        theXML.append("</herstory>")
        return theXML.__str__()

    @classmethod
    def renderStateXML(cls, state):
        """ generated source for method renderStateXML """
        theXML = StringBuilder()
        theXML.append("<state>")
        for sentence in state:
            theXML.append(renderGdlToXML(sentence))
        theXML.append("</state>")
        return theXML.__str__()

    @classmethod
    def renderArrayXML(cls, tag, arr):
        """ generated source for method renderArrayXML """
        theXML = StringBuilder()
        i = 0
        while i < len(arr):
            theXML.append(cls.renderLeafXML(tag, arr.get(i)))
            i += 1
        return theXML.__str__()

    @classmethod
    def renderGdlToXML(cls, gdl):
        """ generated source for method renderGdlToXML """
        rval = ""
        if isinstance(gdl, (GdlConstant, )):
            return c.getValue()
        elif isinstance(gdl, (GdlFunction, )):
            if f.__name__.__str__() == "true":
                return "<fact>" + cls.renderGdlToXML(f.get(0)) + "</fact>"
            else:
                rval += "<relation>" + f.__name__ + "</relation>"
                while i < f.arity():
                    pass
                    i += 1
                return rval
        elif isinstance(gdl, (GdlRelation, )):
            if relation.__name__.__str__() == "true":
                while i < relation.arity():
                    pass
                    i += 1
                return rval
            else:
                rval += "<relation>" + relation.__name__ + "</relation>"
                while i < relation.arity():
                    pass
                    i += 1
                return rval
        else:
            System.err.println("gdlToXML Error: could not handle " + gdl.__str__())
            return None

