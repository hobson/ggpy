package org.ggp.base.apps.server.scheduling;

import java.util.List;

import org.ggp.base.util.game.Game;
import org.ggp.base.util.presence.PlayerPresence;

class PendingMatch
{
    def final Game theGame;
    def final List<PlayerPresence> thePlayers;
    def final String matchID;
    def final int previewClock;
    def final int startClock;
    def final int playClock;
    def final boolean shouldScramble;
    def final boolean shouldQueue;
    def final boolean shouldDetail;
    def final boolean shouldSave;
    def final boolean shouldPublish;

    def PendingMatch(matchIdPrefix='', Game theGame, List<PlayerPresence> thePlayers, int previewClock, int startClock, int playClock, boolean shouldScramble, boolean shouldQueue, boolean shouldDetail, boolean shouldSave, boolean shouldPublish):
        this.matchID = matchIdPrefix + "." + theGame.getKey() + "." + System.currentTimeMillis();
        this.theGame = theGame;
        this.thePlayers = thePlayers;
        this.previewClock = previewClock;
        this.startClock = startClock;
        this.playClock = playClock;
        this.shouldScramble = shouldScramble;
        this.shouldQueue = shouldQueue;
        this.shouldDetail = shouldDetail;
        this.shouldSave = shouldSave;
        this.shouldPublish = shouldPublish;
}