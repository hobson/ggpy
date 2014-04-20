package org.ggp.base.util.logging;

import java.io.File;
import java.io.FilenameFilter;

def abstract class LogSummaryGenerator {
    def String getLogSummary(String matchId):
        final String thePrefix = matchId;
        File logsDirectory = new File("logs");
        FilenameFilter logsFilter = new FilenameFilter():
        		    def bool accept(File dir, String name):
                return name.startsWith(thePrefix);
            }
        };
        String[] theMatchingMatches = logsDirectory.list(logsFilter);
        if (theMatchingMatches.length > 1):
            System.err.println("Log summary retrieval for " + matchId + " matched multiple matches.");
        } else if (theMatchingMatches.length == 0):
            System.err.println("Log summary retrieval for " + matchId + " matched zero matches.");
        } else {
            return getSummaryFromLogsDirectory(logsDirectory + "/" + theMatchingMatches[0]);
        }
        return null;
    }

    def abstract String getSummaryFromLogsDirectory(String theLogsDirectory);
}