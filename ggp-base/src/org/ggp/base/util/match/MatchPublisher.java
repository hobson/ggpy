package org.ggp.base.util.match

import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.net.HttpURLConnection
import java.net.MalformedURLException
import java.net.URL
import java.net.URLEncoder

class MatchPublisher(object):
    def String publishToSpectatorServer(String spectatorURL, Match theMatch) throws IOException 
        if (theMatch.getGameRepositoryURL().isEmpty()):
            throw new IOException("Match doesn't have appropriate metadata for publication to a spectator server: " + theMatch)
        else:
            return performPOST(spectatorURL, theMatch.getSpectatorAuthToken(), theMatch.toJSON())


    def String performPOST(String theURL, String theAuth, String theData) throws IOException 
        String message = URLEncoder.encode(theData, "UTF-8")

        try 
            URL url = new URL(theURL)
            HttpURLConnection connection = (HttpURLConnection) url.openConnection()
            connection.setDoOutput(true)
            connection.setRequestMethod("POST")

            OutputStreamWriter writer = new OutputStreamWriter(connection.getOutputStream())
            writer.write("AUTH=" + theAuth + "&DATA=" + message)
            writer.close()

            if (connection.getResponseCode() == HttpURLConnection.HTTP_OK):
                return new BufferedReader(new InputStreamReader(connection.getInputStream())).readLine()
            else:
                String errorDescription = "?"
                try  errorDescription = new BufferedReader(new InputStreamReader(connection.getInputStream())).readLine(); except Exception q)
                throw new IOException(connection.getResponseCode() + ": " + errorDescription)

        except MalformedURLException e):
            throw new IOException(e)
        except IOException e):
            throw e


    static class MatchPublisherThread(Thread):
        theMatch = Match()
        spectatorURL = String()

        def MatchPublisherThread(String spectatorURL, Match theMatch):
            self.theMatch = theMatch
            self.spectatorURL = spectatorURL

            def void run():
            try 
                MatchPublisher.publishToSpectatorServer(spectatorURL, theMatch)
            except IOException e):
                e.printStackTrace()



    def void publishToSpectatorServerAsync(String spectatorURL, Match theMatch) throws IOException 
        MatchPublisherThread theThread = new MatchPublisherThread(spectatorURL, theMatch)
        theThread.start()

