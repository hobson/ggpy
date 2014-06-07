#!/usr/bin/env python
""" generated source for module PlayerPresenceManager """
# package: org.ggp.base.util.presence
import java.io.BufferedReader

import java.io.BufferedWriter

import java.io.File

import java.io.FileInputStream

import java.io.FileWriter

import java.io.IOException

import java.io.InputStreamReader

import java.nio.charset.Charset

import java.util.HashMap

import java.util.HashSet

import java.util.Map

import java.util.Objects

import java.util.Set

import java.util.TreeSet

import org.ggp.base.util.observer.Event

import org.ggp.base.util.observer.Observer

import org.ggp.base.util.observer.Subject

import external.JSON.JSONArray

import external.JSON.JSONException

import external.JSON.JSONObject

class PlayerPresenceManager(Subject):
    """ generated source for class PlayerPresenceManager """
    monitoredPlayers = Map()

    class PlayerPresenceChanged(Event):
        """ generated source for class PlayerPresenceChanged """

    class PlayerPresenceAdded(Event):
        """ generated source for class PlayerPresenceAdded """

    class PlayerPresenceRemoved(Event):
        """ generated source for class PlayerPresenceRemoved """

    @classmethod
    def isDifferent(cls, a, b):
        """ generated source for method isDifferent """
        return not Objects == a, b

    INFO_PING_PERIOD_IN_SECONDS = 1

    class PresenceMonitor(Thread):
        """ generated source for class PresenceMonitor """
        def run(self):
            """ generated source for method run """
            while True:
                try:
                    Thread.sleep(self.INFO_PING_PERIOD_IN_SECONDS)
                except InterruptedException as e:
                    e.printStackTrace()
                for key in keys:
                    if presence == None:
                        continue 
                    if presence.getStatusAge() > self.INFO_PING_PERIOD_IN_SECONDS * 1000:
                        presence.updateInfo()
                        if self.isDifferent(old_status, new_status):
                            notifyObservers(self.PlayerPresenceChanged())
                        elif self.isDifferent(old_name, new_name):
                            notifyObservers(self.PlayerPresenceChanged())

    def __init__(self):
        """ generated source for method __init__ """
        super(PlayerPresenceManager, self).__init__()
        self.monitoredPlayers = HashMap()
        loadPlayersJSON()
        if len(self.monitoredPlayers) == 0:
            try:
                #  When starting from a blank slate, add some initial players to the
                #  monitoring list just so that it's clear how it works.
                addPlayer("127.0.0.1:9147")
                addPlayer("127.0.0.1:9148")
            except InvalidHostportException as e:
        self.PresenceMonitor().start()

    @SuppressWarnings("serial")
    class InvalidHostportException(Exception):
        """ generated source for class InvalidHostportException """

    def addPlayerSilently(self, hostport):
        """ generated source for method addPlayerSilently """
        try:
            if not self.monitoredPlayers.containsKey(hostport):
                self.monitoredPlayers.put(hostport, presence)
                return presence
            else:
                return self.monitoredPlayers.get(hostport)
        except ArrayIndexOutOfBoundsException as e:
            raise self.InvalidHostportException()
        except NumberFormatException as e:
            raise self.InvalidHostportException()

    def addPlayer(self, hostport):
        """ generated source for method addPlayer """
        presence = self.addPlayerSilently(hostport)
        notifyObservers(self.PlayerPresenceAdded())
        savePlayersJSON()
        return presence

    def removePlayer(self, hostport):
        """ generated source for method removePlayer """
        self.monitoredPlayers.remove(hostport)
        notifyObservers(self.PlayerPresenceRemoved())
        savePlayersJSON()

    def getPresence(self, hostport):
        """ generated source for method getPresence """
        return self.monitoredPlayers.get(hostport)

    def getSortedPlayerNames(self):
        """ generated source for method getSortedPlayerNames """
        return TreeSet(self.monitoredPlayers.keySet())

    observers = HashSet()

    def addObserver(self, observer):
        """ generated source for method addObserver """
        self.observers.add(observer)

    def notifyObservers(self, event):
        """ generated source for method notifyObservers """
        for observer in observers:
            observer.observe(event)

    playerListFilename = ".ggpserver-playerlist.json"

    def savePlayersJSON(self):
        """ generated source for method savePlayersJSON """
        try:
            playerListJSON.put("hostports", self.monitoredPlayers.keySet())
            if not file_.exists():
                file_.createNewFile()
            bw.write(playerListJSON.__str__())
            bw.close()
        except IOException as ie:
            ie.printStackTrace()
        except JSONException as e:
            e.printStackTrace()

    def loadPlayersJSON(self):
        """ generated source for method loadPlayersJSON """
        try:
            if not file_.exists():
                return
            try:
                while (line = br.readLine()) != None:
                    pdata.append(line)
            finally:
                br.close()
            if playerListJSON.has("hostports"):
                while i < len(theHostports):
                    try:
                        self.addPlayerSilently(theHostports.get(i).__str__())
                    except InvalidHostportException as e:
                        e.printStackTrace()
                    i += 1
        except IOException as ie:
            ie.printStackTrace()
        except JSONException as e:
            e.printStackTrace()

