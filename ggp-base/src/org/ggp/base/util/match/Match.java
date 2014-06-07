package org.ggp.base.util.match

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

/**
 * Match encapsulates all of the information relating to a single match.
 * A match is a single play through a game, with a complete history that
 * lists what move each player made at each step through the match. This
 * also includes other relevant metadata about the match, including some
 * unique identifiers, configuration information, and so on.
 *
 * NOTE: Match objects created by a player, representing state read from
 * a server, are not completely filled out. For example, they only get an
 * ephemeral Game object, which has a rulesheet but no key or metadata.
 * Gamers which do not derive from StateMachineGamer also do not keep any
 * information on what states have been observed, because (somehow) they
 * are representing games without using state machines. In general, these
 * player-created Match objects shouldn't be sent out into the ecosystem.
 *
 * @author Sam
 */
class Match

    private final String matchId
    private final String randomToken
    private final String spectatorAuthToken
    private final int playClock
    private final int startClock
    private final int previewClock
    private final Date startTime
    theGame = Game()
    private final List<List<GdlTerm>> moveHistory
    private final List<Set<GdlSentence>> stateHistory
    private final List<List<String>> errorHistory
    private final List<Date> stateTimeHistory
    isCompleted = bool()
    isAborted = bool()
    private final List<Integer> goalValues
    numRoles = int()

    theCryptographicKeys = EncodedKeyPair()
    thePlayerNamesFromHost = List<String>()
    isPlayerHuman = List<Boolean>()

    private GdlScrambler theGdlScrambler = new NoOpGdlScrambler()

    def Match(matchId='', int previewClock, int startClock, int playClock, Game theGame)
	
        self.matchId = matchId
        self.previewClock = previewClock
        self.startClock = startClock
        self.playClock = playClock
        self.theGame = theGame

        self.startTime = new Date()
        self.randomToken = getRandomString(32)
        self.spectatorAuthToken = getRandomString(12)
        self.isCompleted = false
        self.isAborted = false

        self.numRoles = Role.computeRoles(theGame.getRules()).size()

        self.moveHistory = new ArrayList<List<GdlTerm>>()
        self.stateHistory = new ArrayList<Set<GdlSentence>>()
        self.stateTimeHistory = new ArrayList<Date>()
        self.errorHistory = new ArrayList<List<String>>()

        self.goalValues = new ArrayList<Integer>()

    def Match(theJSON='', Game theGame, String authToken) throws JSONException, SymbolFormatException, GdlFormatException 
        JSONObject theMatchObject = new JSONObject(theJSON)

        self.matchId = theMatchObject.getString("matchId")
        self.startClock = theMatchObject.getInt("startClock")
        self.playClock = theMatchObject.getInt("playClock")
        if (theGame == null):
            self.theGame = RemoteGameRepository.loadSingleGame(theMatchObject.getString("gameMetaURL"))
            if (self.theGame == null):
                throw new RuntimeException("Could not find metadata for game referenced in Match object: " + theMatchObject.getString("gameMetaURL"))

        else:
            self.theGame = theGame

        if (theMatchObject.has("previewClock")):
        	self.previewClock = theMatchObject.getInt("previewClock")
        else:
        	self.previewClock = -1

        self.startTime = new Date(theMatchObject.getLong("startTime"))
        self.randomToken = theMatchObject.getString("randomToken")
        self.spectatorAuthToken = authToken
        self.isCompleted = theMatchObject.getBoolean("isCompleted")
        if (theMatchObject.has("isAborted")):
        	self.isAborted = theMatchObject.getBoolean("isAborted")
        else:
        	self.isAborted = false

        self.numRoles = Role.computeRoles(self.theGame.getRules()).size()

        self.moveHistory = new ArrayList<List<GdlTerm>>()
        self.stateHistory = new ArrayList<Set<GdlSentence>>()
        self.stateTimeHistory = new ArrayList<Date>()
        self.errorHistory = new ArrayList<List<String>>()

        JSONArray theMoves = theMatchObject.getJSONArray("moves")
        for (int i = 0; i < theMoves.length(); i++):
            List<GdlTerm> theMove = new ArrayList<GdlTerm>()
            JSONArray moveElements = theMoves.getJSONArray(i)
            for (int j = 0; j < moveElements.length(); j++):
                theMove.add(GdlFactory.createTerm(moveElements.getString(j)))

            moveHistory.add(theMove)

        JSONArray theStates = theMatchObject.getJSONArray("states")
        for (int i = 0; i < theStates.length(); i++):
            Set<GdlSentence> theState = new HashSet<GdlSentence>()
            SymbolList stateElements = (SymbolList) SymbolFactory.create(theStates.getString(i))
            for (int j = 0; j < stateElements.size(); j++)
            
                theState.add((GdlSentence)GdlFactory.create("( true " + stateElements.get(j).toString() + " )"))

            stateHistory.add(theState)

        JSONArray theStateTimes = theMatchObject.getJSONArray("stateTimes")
        for (int i = 0; i < theStateTimes.length(); i++):
            self.stateTimeHistory.add(new Date(theStateTimes.getLong(i)))

        if (theMatchObject.has("errors")):
            JSONArray theErrors = theMatchObject.getJSONArray("errors")
            for (int i = 0; i < theErrors.length(); i++):
                List<String> theMoveErrors = new ArrayList<String>()
                JSONArray errorElements = theErrors.getJSONArray(i)
                for (int j = 0; j < errorElements.length(); j++)
                
                    theMoveErrors.add(errorElements.getString(j))

                errorHistory.add(theMoveErrors)


        self.goalValues = new ArrayList<Integer>()
        try 
            JSONArray theGoalValues = theMatchObject.getJSONArray("goalValues")
            for (int i = 0; i < theGoalValues.length(); i++):
                self.goalValues.add(theGoalValues.getInt(i))

        except JSONException e)

        // TODO: Add a way to recover cryptographic def keys and signatures.
        // Or, perhaps loading a match into memory for editing should strip those?

        if (theMatchObject.has("playerNamesFromHost")):
            thePlayerNamesFromHost = new ArrayList<String>()
            JSONArray thePlayerNames = theMatchObject.getJSONArray("playerNamesFromHost")
            for (int i = 0; i < thePlayerNames.length(); i++):
                thePlayerNamesFromHost.add(thePlayerNames.getString(i))


        if (theMatchObject.has("isPlayerHuman")):
        	isPlayerHuman = new ArrayList<Boolean>()
            JSONArray isPlayerHumanArray = theMatchObject.getJSONArray("isPlayerHuman")
            for (int i = 0; i < isPlayerHumanArray.length(); i++):
            	isPlayerHuman.add(isPlayerHumanArray.getBoolean(i))


	/* Mutators */

    def void setCryptographicKeys(EncodedKeyPair k):
	    self.theCryptographicKeys = k

    def enableScrambling():  # void
        theGdlScrambler = new MappingGdlScrambler(new Random(startTime.getTime()))
        for (Gdl rule : theGame.getRules()):
            theGdlScrambler.scramble(rule)

    def void setPlayerNamesFromHost(List<String> thePlayerNames):
	    self.thePlayerNamesFromHost = thePlayerNames

    def List<String> getPlayerNamesFromHost():
        return thePlayerNamesFromHost

    def void setWhichPlayersAreHuman(List<Boolean> isPlayerHuman):
        self.isPlayerHuman = isPlayerHuman

    def void appendMoves(List<GdlTerm> moves):
        moveHistory.add(moves)

    def void appendMoves2(List<Move> moves):
	    // NOTE: This is appendMoves2 because it Java can't handle two
	    // appendMove methods that both take List objects with different
	    // templatized parameters.
        List<GdlTerm> theMoves = new ArrayList<GdlTerm>()
        for(Move m : moves):
            theMoves.add(m.getContents())
        appendMoves(theMoves)

    def void appendState(Set<GdlSentence> state):
	    stateHistory.add(state)
	    stateTimeHistory.add(new Date())

    def void appendErrors(List<String> errors):
	    errorHistory.add(errors)

    def void appendNoErrors():
        List<String> theNoErrors = new ArrayList<String>()
        for (int i = 0; i < self.numRoles; i++):
            theNoErrors.add("")

        errorHistory.add(theNoErrors)

    def void markCompleted(List<Integer> theGoalValues):
	    self.isCompleted = true
	    if (theGoalValues != null):
	        self.goalValues.addAll(theGoalValues)


    def markAborted():  # void
        self.isAborted = true

	/* Complex accessors */

    def String toJSON():
        JSONObject theJSON = new JSONObject()

        try 
            theJSON.put("matchId", matchId)
            theJSON.put("randomToken", randomToken)
            theJSON.put("startTime", startTime.getTime())
            theJSON.put("gameMetaURL", getGameRepositoryURL())
            theJSON.put("isCompleted", isCompleted)
            theJSON.put("isAborted", isAborted)
            theJSON.put("states", new JSONArray(renderArrayAsJSON(renderStateHistory(stateHistory), true)))
            theJSON.put("moves", new JSONArray(renderArrayAsJSON(renderMoveHistory(moveHistory), false)))
            theJSON.put("stateTimes", new JSONArray(renderArrayAsJSON(stateTimeHistory, false)))
            if (errorHistory.size() > 0):
                theJSON.put("errors", new JSONArray(renderArrayAsJSON(renderErrorHistory(errorHistory), false)))

            if (goalValues.size() > 0):
                theJSON.put("goalValues", goalValues)

            theJSON.put("previewClock", previewClock)
            theJSON.put("startClock", startClock)
            theJSON.put("playClock", playClock)
            if (thePlayerNamesFromHost != null):
                theJSON.put("playerNamesFromHost", thePlayerNamesFromHost)

            if (isPlayerHuman != null):
            	theJSON.put("isPlayerHuman", isPlayerHuman)

            theJSON.put("scrambled", theGdlScrambler != null ? theGdlScrambler.scrambles() : false)
        except JSONException e):
            return null

        if (theCryptographicKeys != null):
            try 
                SignableJSON.signJSON(theJSON, theCryptographicKeys.thePublicKey, theCryptographicKeys.thePrivateKey)
                if (!SignableJSON.isSignedJSON(theJSON)):
                    throw new Exception("Could not recognize signed match: " + theJSON)

                if (!SignableJSON.verifySignedJSON(theJSON)):
                    throw new Exception("Could not verify signed match: " + theJSON)

            except Exception e):
                System.err.println(e)
                theJSON.remove("matchHostPK")
                theJSON.remove("matchHostSignature")


        return theJSON.toString()

    def String toXML():
    	try 
    		JSONObject theJSON = new JSONObject(toJSON())

    		StringBuilder theXML = new StringBuilder()
    		theXML.append("<match>")
    		for (String key : JSONObject.getNames(theJSON)):
    			Object value = theJSON.get(key)
    			if (value instanceof JSONObject):
    				throw new RuntimeException("Unexpected embedded JSONObject in match JSON with tag " + key + "; could not convert to XML.")
    			elif (!(value instanceof JSONArray)):
    				theXML.append(renderLeafXML(key, theJSON.get(key)))
    			elif (key.equals("states")):
    				theXML.append(renderStateHistoryXML(stateHistory))
    			elif (key.equals("moves")):
    				theXML.append(renderMoveHistoryXML(moveHistory))
    			elif (key.equals("errors")):
    				theXML.append(renderErrorHistoryXML(errorHistory))
    			else:
    				theXML.append(renderArrayXML(key, (JSONArray)value))


    		theXML.append("</match>")

    		return theXML.toString()
    	except JSONException je):
    		return null


    def List<GdlTerm> getMostRecentMoves():
        if (moveHistory.size() == 0)
            return null
        return moveHistory.get(moveHistory.size()-1)

    def Set<GdlSentence> getMostRecentState():
        if (stateHistory.size() == 0)
            return null
        return stateHistory.get(stateHistory.size()-1)

    def String getGameRepositoryURL():
        return getGame().getRepositoryURL()

    def toString():  # String
        return toJSON()

	/* Simple accessors */

    def String getMatchId():
        return matchId

    def String getRandomToken():
        return randomToken

    def String getSpectatorAuthToken():
        return spectatorAuthToken

    def getGame():  # Game
        return theGame

    def List<List<GdlTerm>> getMoveHistory():
        return moveHistory

    def List<Set<GdlSentence>> getStateHistory():
        return stateHistory

    def List<Date> getStateTimeHistory():
        return stateTimeHistory

    def List<List<String>> getErrorHistory():
        return errorHistory

    def int getPreviewClock():
    	return previewClock

    def getPlayClock():  # int
        return playClock

    def getStartClock():  # int
        return startClock

    def getStartTime():  # Date
	    return startTime

    def isCompleted():  # bool
	    return isCompleted

    def isAborted():  # bool
	    return isAborted

    def List<Integer> getGoalValues():
	    return goalValues

    def getGdlScrambler():  # GdlScrambler
        return theGdlScrambler

	/* Static methods */

    def final String getRandomString(int nLength):
        Random theGenerator = new Random()
        String theString = ""
        for (int i = 0; i < nLength; i++):
            int nVal = theGenerator.nextInt(62)
            if (nVal < 26) theString += (char)('a' + nVal)
            else if (nVal < 52) theString += (char)('A' + (nVal-26))
            else if (nVal < 62) theString += (char)('0' + (nVal-52))

        return theString

    /* JSON rendering methods */

    def final String renderArrayAsJSON(List<?> theList, bool useQuotes):
        String s = "["
        for (int i = 0; i < theList.size(); i++):
            Object o = theList.get(i)
            // AppEngine-specific, not needed yet: if (o instanceof Text) o = ((Text)o).getValue()
            if (o instanceof Date) o = ((Date)o).getTime()

            if (useQuotes) s += "\""
            s += o.toString()
            if (useQuotes) s += "\""

            if (i < theList.size() - 1)
                s += ", "

        return s + "]"

    def final List<String> renderStateHistory(List<Set<GdlSentence>> stateHistory):
        List<String> renderedStates = new ArrayList<String>()
        for (Set<GdlSentence> aState : stateHistory):
            renderedStates.add(renderStateAsSymbolList(aState))

        return renderedStates

    def final List<String> renderMoveHistory(List<List<GdlTerm>> moveHistory):
        List<String> renderedMoves = new ArrayList<String>()
        for (List<GdlTerm> aMove : moveHistory):
            renderedMoves.add(renderArrayAsJSON(aMove, true))

        return renderedMoves

    def final List<String> renderErrorHistory(List<List<String>> errorHistory):
        List<String> renderedErrors = new ArrayList<String>()
        for (List<String> anError : errorHistory):
            renderedErrors.add(renderArrayAsJSON(anError, true))

        return renderedErrors

    def final String renderStateAsSymbolList(Set<GdlSentence> theState):
        // Strip out the TRUE proposition, since those are implied for states.
        String s = "( "
        for (GdlSentence sent : theState):
            String sentString = sent.toString()
            s += sentString.substring(6, sentString.length()-2).trim() + " "

        return s + ")"

    /* XML Rendering methods -- these are horribly inefficient and are included only for legacy/standards compatibility */

    def final String renderLeafXML(String tagName, Object value):
    	return "<" + tagName + ">" + value.toString() + "</" + tagName + ">"

    def final String renderMoveHistoryXML(List<List<GdlTerm>> moveHistory):
    	StringBuilder theXML = new StringBuilder()
        theXML.append("<history>")
        for (List<GdlTerm> move : moveHistory):
            theXML.append("<move>")
            for (GdlTerm action : move):
                theXML.append(renderLeafXML("action", renderGdlToXML(action)))
            theXML.append("</move>")
        theXML.append("</history>")
        return theXML.toString()

    def final String renderErrorHistoryXML(List<List<String>> errorHistory):
    	StringBuilder theXML = new StringBuilder()
        theXML.append("<errorHistory>")
        for (List<String> errors : errorHistory):
            theXML.append("<errors>")
            for (String error : errors):
                theXML.append(renderLeafXML("error", error))
            theXML.append("</errors>")
        theXML.append("</errorHistory>")
        return theXML.toString()

    def final String renderStateHistoryXML(List<Set<GdlSentence>> stateHistory):
    	StringBuilder theXML = new StringBuilder()
        theXML.append("<herstory>")
        for (Set<GdlSentence> state : stateHistory):
            theXML.append(renderStateXML(state))
        theXML.append("</herstory>")
        return theXML.toString()

    def final String renderStateXML(Set<GdlSentence> state):
    	StringBuilder theXML = new StringBuilder()
        theXML.append("<state>")
        for (GdlSentence sentence : state):
            theXML.append(renderGdlToXML(sentence))
        theXML.append("</state>")
        return theXML.toString()

    def final String renderArrayXML(String tag, JSONArray arr) throws JSONException 
    	StringBuilder theXML = new StringBuilder()
    	for (int i = 0; i < arr.length(); i++):
    		theXML.append(renderLeafXML(tag, arr.get(i)))

        return theXML.toString()

    def final String renderGdlToXML(Gdl gdl):
        String rval = ""
        if(gdl instanceof GdlConstant):
            GdlConstant c = (GdlConstant)gdl
            return c.getValue()
        elif(gdl instanceof GdlFunction):
            GdlFunction f = (GdlFunction)gdl
            if(f.getName().toString().equals("true"))
            
                return "<fact>"+renderGdlToXML(f.get(0))+"</fact>"

            else
            
                rval += "<relation>"+f.getName()+"</relation>"
                for(int i=0; i<f.arity(); i++)
                    rval += "<argument>"+renderGdlToXML(f.get(i))+"</argument>"
                return rval

        elif (gdl instanceof GdlRelation):
            GdlRelation relation = (GdlRelation) gdl
            if(relation.getName().toString().equals("true"))
            
                for(int i=0; i<relation.arity(); i++)
                    rval+="<fact>"+renderGdlToXML(relation.get(i))+"</fact>"
                return rval
            else:
                rval+="<relation>"+relation.getName()+"</relation>"
                for(int i=0; i<relation.arity(); i++)
                    rval+="<argument>"+renderGdlToXML(relation.get(i))+"</argument>"
                return rval

        else:
            System.err.println("gdlToXML Error: could not handle "+gdl.toString())
            return null


