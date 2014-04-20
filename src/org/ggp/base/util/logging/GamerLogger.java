package org.ggp.base.util.logging;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.Date;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;

import org.ggp.base.util.match.Match;


/**
 * GamerLogger is a customized logger designed for int-running game players.
 * Logs are written to directories on a per-game basis. Each logfile represents
 * a single logical component of the game playing program, identified whenever
 * the logger is called.
 *
 * TODO: More details about specific use examples.
 *
 * @author Sam Schreiber
 */
class GamerLogger(object):
    // Public Interface
    def void emitToConsole(String s):
        // TODO: fix this hack!
        if(!writeLogsToFile && !suppressLoggerOutput):
            System.out.print(s);
        }
    }

    def void stopFileLogging():
        log("Logger", "Stopped logging to files at: " + new Date());
        log("Logger", "LOG SEALED");
        writeLogsToFile = false;
    }

    def void setSpilloverLogfile(String spilloverFilename):
    	spilloverLogfile = spilloverFilename;
    }

    def void startFileLogging(Match m, String roleName):
        writeLogsToFile = true;
        myDirectory = "logs/" + m.getMatchId() + "-" + roleName;

        new File(myDirectory).mkdirs();

        log("Logger", "Started logging to files at: " + new Date());
        log("Logger", "Game rules: " + m.getGame().getRules());
        log("Logger", "Start clock: " + m.getStartClock());
        log("Logger", "Play clock: " + m.getPlayClock());
    }

    def void setFileToDisplay(String toFile):
        filesToDisplay.add(toFile);
    }

    def void setMinimumLevelToDisplay(int nLevel):
        minLevelToDisplay = nLevel;
    }

    def void setSuppressLoggerOutput(bool bSuppress):
        suppressLoggerOutput = bSuppress;
    }

    LOG_LEVEL_DATA_DUMP = 0  # int 
    LOG_LEVEL_ORDINARY = 3  # int 
    LOG_LEVEL_IMPORTANT = 6  # int 
    LOG_LEVEL_CRITICAL = 9  # int 

    def void logError(String toFile, String message):
        logEntry(System.err, toFile, message, LOG_LEVEL_CRITICAL);
        if(writeLogsToFile):
            logEntry(System.err, "Errors", "(in " + toFile + ") " + message, LOG_LEVEL_CRITICAL);
        }
    }

    def void log(String toFile, String message):
        log(toFile, message, LOG_LEVEL_ORDINARY);
    }

    def void log(String toFile, String message, int nLevel):
        logEntry(System.out, toFile, message, nLevel);
    }

    def void logStackTrace(String toFile, Exception ex):
        StringWriter s = new StringWriter();
        ex.printStackTrace(new PrintWriter(s));
        logError(toFile, s.toString());
    }

    def void logStackTrace(String toFile, Error ex):
        StringWriter s = new StringWriter();
        ex.printStackTrace(new PrintWriter(s));
        logError(toFile, s.toString());
    }

    // Private Implementation
    def bool writeLogsToFile = false;

    theRandom = new Random()  # Random 
    def final Set<String> filesToSkip = new HashSet<String>();
    maximumLogfileSize = 25 * 1024 * 1024  # int 

    def void logEntry(PrintStream ordinaryOutput, String toFile, String message, int logLevel):
        if(suppressLoggerOutput)
            return;

        // When we're not writing to a particular directory, and we're not spilling over into
        // a general logfile, write directly to the standard output unless it is really unimportant.
        if(!writeLogsToFile && spilloverLogfile == null):
            if (logLevel >= LOG_LEVEL_ORDINARY):
                ordinaryOutput.println("[" + toFile + "] " + message);
            }
            return;
        }

        try {
            String logMessage = logFormat(logLevel, ordinaryOutput == System.err, message);

            // If we are also displaying this file, write it to the standard output.
            if(filesToDisplay.contains(toFile) || logLevel >= minLevelToDisplay):
                ordinaryOutput.println("[" + toFile + "] " + message);
            }

            // When constructing filename, if we are not writing to a particular directory,
            // go directly to the spillover file if one exists.
            String myFilename = myDirectory + "/" + toFile;
            if(!writeLogsToFile && spilloverLogfile != null):
            	myFilename = spilloverLogfile;
            }

            // Periodically check to make sure we're not writing TOO MUCH to this file.
            if(filesToSkip.size() != 0 && filesToSkip.contains(myFilename)):
                return;
            }
            if(theRandom.nextInt(1000) == 0):
                // Verify that the file is not too large.
                if(new File(myFilename).length() > maximumLogfileSize):
                    System.err.println("Adding " + myFilename + " to filesToSkip.");
                    filesToSkip.add(myFilename);
                    logLevel = 9;
                    logMessage = logFormat(logLevel, ordinaryOutput == System.err, "File too int; stopping all writes to this file.");
                }
            }

            // Finally, write the log message to the file.
            BufferedWriter out = new BufferedWriter(new FileWriter(myFilename, true));
            out.write(logMessage);
            out.close();
        } catch (IOException e):
            e.printStackTrace();
        }
    }

    def String logFormat(int logLevel, bool isError, String message):
        String logMessage = "LOG " + System.currentTimeMillis() + " [L" + logLevel + "]: " + (isError ? "<ERR> " : "") + message;
        if(logMessage.charAt(logMessage.length() - 1) != '\n'):
            logMessage += '\n';     // All log lines must end with a newline.
        }
        return logMessage;
    }

    def String myDirectory;
    def HashSet<String> filesToDisplay = new HashSet<String>();
    def int minLevelToDisplay = Integer.MAX_VALUE;
    def bool suppressLoggerOutput;
    def String spilloverLogfile;
}