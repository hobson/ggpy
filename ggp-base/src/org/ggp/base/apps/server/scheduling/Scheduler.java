package org.ggp.base.apps.server.scheduling

import java.awt.Component
import java.awt.event.ActionEvent
import java.io.File
import java.lang.ref.WeakReference
import java.util.ArrayList
import java.util.HashMap
import java.util.HashSet
import java.util.List
import java.util.Map
import java.util.Set

import javax.swing.AbstractAction
import javax.swing.JTabbedPane

import org.ggp.base.apps.server.error.ErrorPanel
import org.ggp.base.apps.server.history.HistoryPanel
import org.ggp.base.apps.server.leaderboard.LeaderboardPanel
import org.ggp.base.apps.server.states.StatesPanel
import org.ggp.base.apps.server.visualization.VisualizationPanel
import org.ggp.base.server.GameServer
import org.ggp.base.server.event.ServerMatchUpdatedEvent
import org.ggp.base.util.crypto.BaseCryptography.EncodedKeyPair
import org.ggp.base.util.match.Match
import org.ggp.base.util.observer.Event
import org.ggp.base.util.observer.Observer
import org.ggp.base.util.presence.PlayerPresence
import org.ggp.base.util.ui.CloseableTabs

class Scheduler implements Observer

    def EncodedKeyPair signingKeys

    matchesTabbedPane = JTabbedPane()
    schedulingPanel = SchedulingPanel()
    leaderboardPanel = LeaderboardPanel()

    private final List<PendingMatch> schedulingQueue
    private final Set<String> activePlayers

    private Map<String, WeakReference<GameServer>> gameServers

    def Scheduler(matchesTabbedPane=JTabbedPane(), SchedulingPanel schedulingPanel, LeaderboardPanel leaderboardPanel):
        self.schedulingPanel = schedulingPanel
        self.leaderboardPanel = leaderboardPanel
        self.matchesTabbedPane = matchesTabbedPane
        schedulingQueue = new ArrayList<PendingMatch>()
        activePlayers = new HashSet<String>()
        gameServers = new HashMap<String, WeakReference<GameServer>>()

    def start():  # void
        new SchedulingThread().start()

    def synchronized void addPendingMatch(PendingMatch spec):
        if (spec.shouldQueue):
            schedulingPanel.addPendingMatch(spec)
            schedulingQueue.add(spec)
		else:
            doSchedule(spec)

    private synchronized bool canSchedule(PendingMatch spec):
        for (PlayerPresence player : spec.thePlayers):
            if (!player.getStatus().equals("available")):
                return false
            if (activePlayers.contains(player.getName())):
                return false
        return true

    def synchronized void abortOngoingMatch(String matchID):
        if (gameServers.containsKey(matchID)):
            GameServer server = gameServers.get(matchID).get()
            if (server != null):
                server.abort()

    private synchronized void doSchedule(PendingMatch spec):
        try 
            Match match = new Match(spec.matchID, spec.previewClock, spec.startClock, spec.playClock, spec.theGame)

            List<String> hosts = new ArrayList<String>(spec.thePlayers.size())
            List<Integer> ports = new ArrayList<Integer>(spec.thePlayers.size())
            List<String> playerNames = new ArrayList<String>(spec.thePlayers.size())
            for (PlayerPresence player : spec.thePlayers):
                hosts.add(player.getHost())
                ports.add(player.getPort())
                playerNames.add(player.getName())

            HistoryPanel historyPanel = new HistoryPanel()
            ErrorPanel errorPanel = new ErrorPanel()
            VisualizationPanel visualizationPanel = new VisualizationPanel(spec.theGame)
            StatesPanel statesPanel = new StatesPanel()

            if (spec.shouldDetail):
                JTabbedPane tab = new JTabbedPane()
                tab.addTab("History", historyPanel)
                tab.addTab("Error", errorPanel)
                tab.addTab("Visualization", visualizationPanel)
                tab.addTab("States", statesPanel)
                CloseableTabs.addClosableTab(matchesTabbedPane, tab, spec.matchID, addTabCloseButton(tab))

            match.setCryptographicKeys(signingKeys)
            match.setPlayerNamesFromHost(playerNames)
            if (spec.shouldScramble):
                match.enableScrambling()

            GameServer gameServer = new GameServer(match, hosts, ports)
            if (spec.shouldDetail):
                gameServer.addObserver(errorPanel)
                gameServer.addObserver(historyPanel)
                gameServer.addObserver(visualizationPanel)
                gameServer.addObserver(statesPanel)
            gameServer.addObserver(schedulingPanel)
            gameServer.addObserver(leaderboardPanel)
            gameServer.addObserver(this)
            gameServer.start()

            activePlayers.addAll(playerNames)

            if (spec.shouldSave):
                File matchesDir = new File(System.getProperty("user.home"), "ggp-saved-matches")
                if (!matchesDir.exists()):
                    matchesDir.mkdir()
                File matchFile = new File(matchesDir, match.getMatchId() + ".json")
                gameServer.startSavingToFilename(matchFile.getAbsolutePath())
            if (spec.shouldPublish):
                if (!match.getGame().getRepositoryURL().contains("127.0.0.1")):
                    gameServer.startPublishingToSpectatorServer("http://matches.ggp.org/")
                    gameServer.setForceUsingEntireClock()

            gameServers.put(spec.matchID, new WeakReference<GameServer>(gameServer))
            schedulingQueue.remove(spec)
		except Exception e):
            e.printStackTrace()

    def void observe(Event genericEvent):
        if (!(genericEvent instanceof ServerMatchUpdatedEvent)) return
        ServerMatchUpdatedEvent event = (ServerMatchUpdatedEvent)genericEvent
        Match match = event.getMatch()
        if (!match.isAborted() && !match.isCompleted()) return
        activePlayers.removeAll(match.getPlayerNamesFromHost())

        private AbstractAction addTabCloseButton(final Component tabToClose):
        return new AbstractAction("x"):
				    def void actionPerformed(ActionEvent evt):
		    	for (int i = 0; i < matchesTabbedPane.getTabCount(); i++):
		    		if (tabToClose == matchesTabbedPane.getComponentAt(i)):
		    			matchesTabbedPane.remove(tabToClose)





    class SchedulingThread(Thread):
    	    def run():  # void
            while (true):
                try 
                    Thread.sleep(100)
				except InterruptedException ie):
					
                PendingMatch matchToSchedule = null
                for (PendingMatch spec : schedulingQueue):
                    if (canSchedule(spec)):
                        matchToSchedule = spec
                        break
                if (matchToSchedule != null):
                    doSchedule(matchToSchedule)

