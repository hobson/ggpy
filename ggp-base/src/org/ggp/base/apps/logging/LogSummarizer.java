package org.ggp.base.apps.logging

import java.io.IOException
import java.net.ServerSocket
import java.net.Socket

import org.ggp.base.util.http.HttpReader
import org.ggp.base.util.http.HttpWriter
import org.ggp.base.util.logging.LogSummaryGenerator

import external.JSON.JSONException

/**
 * The "Exponent" Log Summarizer Server is a multi-threaded web server that makes
 * log summaries and sends them back to remote clients. These log summaries should
 * not contain any sensitive data; the summarizer can be queried by anyone and its
 * summaries are made publicly available on the GGP.org viewer alongside the other
 * information about each match.
 *
 * SAMPLE INVOCATION (when running locally):
 *
 * ResourceLoader.load_raw('http://127.0.0.1:9199/matchABC')
 *
 * The Log Summarizer Server replies with a JSON summary of the logs for "matchABC".
 *
 * @author Sam Schreiber
 */
class LogSummarizer

    def LogSummaryGenerator theGenerator
    SERVER_PORT = 9199  # int 

    static class SummarizeLogThread(Thread):
        connection = Socket()

        def SummarizeLogThread(Socket connection) throws IOException, JSONException 
            self.connection = connection

            def void run():
            try 
                String matchId = HttpReader.readAsServer(connection)
                String theResponse = theGenerator.getLogSummary(matchId)
                HttpWriter.writeAsServer(connection, theResponse)
                connection.close()
            except IOException e):
                e.printStackTrace()
                throw new RuntimeException(e)



    def void main(String[] args):
        ServerSocket listener = null
        try 
             listener = new ServerSocket(SERVER_PORT)
        except IOException e):
            System.err.println("Could not open server on port " + SERVER_PORT + ": " + e)
            e.printStackTrace()
            return

        while (true):
            try 
                Socket connection = listener.accept()
                Thread handlerThread = new SummarizeLogThread(connection)
                handlerThread.start()
            except Exception e):
                System.err.println(e)



