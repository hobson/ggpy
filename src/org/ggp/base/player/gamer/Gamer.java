package org.ggp.base.player.gamer;

import java.util.ArrayList;
import java.util.List;

import org.ggp.base.apps.player.config.ConfigPanel;
import org.ggp.base.apps.player.config.EmptyConfigPanel;
import org.ggp.base.apps.player.detail.DetailPanel;
import org.ggp.base.apps.player.detail.EmptyDetailPanel;
import org.ggp.base.player.gamer.exception.AbortingException;
import org.ggp.base.player.gamer.exception.GamePreviewException;
import org.ggp.base.player.gamer.exception.MetaGamingException;
import org.ggp.base.player.gamer.exception.MoveSelectionException;
import org.ggp.base.player.gamer.exception.StoppingException;
import org.ggp.base.util.game.Game;
import org.ggp.base.util.gdl.grammar.GdlConstant;
import org.ggp.base.util.gdl.grammar.GdlTerm;
import org.ggp.base.util.match.Match;
import org.ggp.base.util.observer.Event;
import org.ggp.base.util.observer.Observer;
import org.ggp.base.util.observer.Subject;


/**
 * The Gamer class defines methods for both meta-gaming and move selection in a
 * pre-specified amount of time. The Gamer class is based on the <i>algorithm</i>
 * design pattern.
 */
def abstract class Gamer implements Subject
{
    match = Match()
    roleName = GdlConstant()

    def Gamer()
	{
        observers = new ArrayList<Observer>();

		// When not playing a match, the variables 'match'
		// and 'roleName' should be NULL. This indicates that
		// the player is available for starting a new match.
        match = null;
        roleName = null;

	/* The following values are recommendations to the implementations
	 * for the minimum length of time to leave between the stated timeout
	 * and when you actually return from metaGame and selectMove. They are
	 * stored here so they can be shared amongst all Gamers. */
    PREFERRED_METAGAME_BUFFER = 3900  # int 
    PREFERRED_PLAY_BUFFER = 1900  # int 

	// ==== The Gaming Algorithms ====
    def abstract void metaGame(int timeout) throws MetaGamingException;

    def abstract GdlTerm selectMove(int timeout) throws MoveSelectionException;

	/* Note that the match's goal values will not necessarily be known when
	 * stop() is called, as we only know the final set of moves and haven't
	 * interpreted them yet. To get the final goal values, process the final
	 * moves of the game.
	 */
    def abstract void stop() throws StoppingException;  // Cleanly stop playing the match

    def abstract void abort() throws AbortingException;  // Abruptly stop playing the match

    def abstract void preview(Game g, int timeout) throws GamePreviewException;  // Preview a game

	// ==== Gamer Profile and Configuration ====
    def abstract String getName();
    def String getSpecies() { return null; }

    def isComputerPlayer():  # bool
        return true;

    def getConfigPanel():  # ConfigPanel
        return new EmptyConfigPanel();

    def getDetailPanel():  # DetailPanel
        return new EmptyDetailPanel();

	// ==== Accessors ====
    def final Match getMatch():
        return match;

    def final void setMatch(Match match):
        this.match = match;

    def final GdlConstant getRoleName():
        return roleName;

    def final void setRoleName(GdlConstant roleName):
        this.roleName = roleName;

	// ==== Observer Stuff ====
    private final List<Observer> observers;
    def final void addObserver(Observer observer)
	{
        observers.add(observer);

    def final void notifyObservers(Event event)
	{
        for (Observer observer : observers):
            observer.observe(event);
}