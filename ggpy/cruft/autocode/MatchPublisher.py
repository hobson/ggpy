#!/usr/bin/env python
""" generated source for module MatchPublisher """
# package: org.ggp.base.util.match
import java.io.BufferedReader

import java.io.IOException

import java.io.InputStreamReader

import java.io.OutputStreamWriter

import java.net.HttpURLConnection

import java.net.MalformedURLException

import java.net.URL

import java.net.URLEncoder

class MatchPublisher(object):
    """ generated source for class MatchPublisher """
    @classmethod
    def publishToSpectatorServer(cls, spectatorURL, theMatch):
        """ generated source for method publishToSpectatorServer """
        if theMatch.getGameRepositoryURL().isEmpty():
            raise IOException("Match doesn't have appropriate metadata for publication to a spectator server: " + theMatch)
        else:
            return performPOST(spectatorURL, theMatch.getSpectatorAuthToken(), theMatch.toJSON())

    @classmethod
    def performPOST(cls, theURL, theAuth, theData):
        """ generated source for method performPOST """
        message = URLEncoder.encode(theData, "UTF-8")
        try:
            connection.setDoOutput(True)
            connection.setRequestMethod("POST")
            writer.write("AUTH=" + theAuth + "&DATA=" + message)
            writer.close()
            if connection.getResponseCode() == HttpURLConnection.HTTP_OK:
                return BufferedReader(InputStreamReader(connection.getInputStream())).readLine()
            else:
                try:
                    errorDescription = BufferedReader(InputStreamReader(connection.getInputStream())).readLine()
                except Exception as q:
                    pass
                raise IOException(connection.getResponseCode() + ": " + errorDescription)
        except MalformedURLException as e:
            raise IOException(e)
        except IOException as e:
            raise e

    class MatchPublisherThread(Thread):
        """ generated source for class MatchPublisherThread """
        theMatch = Match()
        spectatorURL = str()

        def __init__(self, spectatorURL, theMatch):
            """ generated source for method __init__ """
            super(MatchPublisherThread, self).__init__()
            self.theMatch = theMatch
            self.spectatorURL = spectatorURL

        def run(self):
            """ generated source for method run """
            try:
                MatchPublisher.publishToSpectatorServer(self.spectatorURL, self.theMatch)
            except IOException as e:
                e.printStackTrace()

    @classmethod
    def publishToSpectatorServerAsync(cls, spectatorURL, theMatch):
        """ generated source for method publishToSpectatorServerAsync """
        theThread = cls.MatchPublisherThread(spectatorURL, theMatch)
        theThread.start()

