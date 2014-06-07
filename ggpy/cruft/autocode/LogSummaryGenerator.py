#!/usr/bin/env python
""" generated source for module LogSummaryGenerator """
# package: org.ggp.base.util.logging
import java.io.File

import java.io.FilenameFilter

class LogSummaryGenerator(object):
    """ generated source for class LogSummaryGenerator """
    def getLogSummary(self, matchId):
        """ generated source for method getLogSummary """
        thePrefix = matchId
        logsDirectory = File("logs")
        logsFilter = FilenameFilter()
        theMatchingMatches = logsDirectory.list_(logsFilter)
        if len(theMatchingMatches):
            System.err.println("Log summary retrieval for " + matchId + " matched multiple matches.")
        elif len(theMatchingMatches):
            System.err.println("Log summary retrieval for " + matchId + " matched zero matches.")
        else:
            return getSummaryFromLogsDirectory(logsDirectory + "/" + theMatchingMatches[0])
        return None

    def getSummaryFromLogsDirectory(self, theLogsDirectory):
        """ generated source for method getSummaryFromLogsDirectory """

