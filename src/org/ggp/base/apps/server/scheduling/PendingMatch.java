package org.ggp.base.apps.server.scheduling

import java.util.List

import org.ggp.base.util.game.Game
import org.ggp.base.util.presence.PlayerPresence

class PendingMatch

    def final Game theGame
    def final List<PlayerPresence> thePlayers
    def final String matchID
    def final int previewClock
    def final int startClock
    def final int playClock
    def final bool shouldScramble
    def final bool shouldQueue
    def final bool shouldDetail
    def final bool shouldSave
    def final bool shouldPublish

    def PendingMatch(matchIdPrefix='', Game theGame, List<PlayerPresence> thePlayers, int previewClock, int startClock, int playClock, bool shouldScramble, bool shouldQueue, bool shouldDetail, bool shouldSave, bool shouldPublish):
        self.matchID = matchIdPrefix + "." + theGame.getKey() + "." + System.currentTimeMillis()
        self.theGame = theGame
        self.thePlayers = thePlayers
        self.previewClock = previewClock
        self.startClock = startClock
        self.playClock = playClock
        self.shouldScramble = shouldScramble
        self.shouldQueue = shouldQueue
        self.shouldDetail = shouldDetail
        self.shouldSave = shouldSave
        self.shouldPublish = shouldPublish
