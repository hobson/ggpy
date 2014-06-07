#!/usr/bin/env python
""" generated source for module GamerLogger """
# package: org.ggp.base.util.logging
import java.io.BufferedWriter

import java.io.File

import java.io.FileWriter

import java.io.IOException

import java.io.PrintStream

import java.io.PrintWriter

import java.io.StringWriter

import java.util.Date

import java.util.HashSet

import java.util.Random

import java.util.Set

import org.ggp.base.util.match.Match

# 
#  * GamerLogger is a customized logger designed for long-running game players.
#  * Logs are written to directories on a per-game basis. Each logfile represents
#  * a single logical component of the game playing program, identified whenever
#  * the logger is called.
#  *
#  * TODO: More details about specific use examples.
#  *
#  * @author Sam Schreiber
#  
class GamerLogger(object):
    """ generated source for class GamerLogger """
    #  Public Interface
    @classmethod
    def emitToConsole(cls, s):
        """ generated source for method emitToConsole """
        #  TODO: fix this hack!
        if not writeLogsToFile and not suppressLoggerOutput:
            print s,

    @classmethod
    def stopFileLogging(cls):
        """ generated source for method stopFileLogging """
        log("Logger", "Stopped logging to files at: " + Date())
        log("Logger", "LOG SEALED")
        writeLogsToFile = False

    @classmethod
    def setSpilloverLogfile(cls, spilloverFilename):
        """ generated source for method setSpilloverLogfile """
        spilloverLogfile = spilloverFilename

    @classmethod
    def startFileLogging(cls, m, roleName):
        """ generated source for method startFileLogging """
        writeLogsToFile = True
        myDirectory = "logs/" + m.getMatchId() + "-" + roleName
        File(myDirectory).mkdirs()
        log("Logger", "Started logging to files at: " + Date())
        log("Logger", "Game rules: " + m.getGame().getRules())
        log("Logger", "Start clock: " + m.getStartClock())
        log("Logger", "Play clock: " + m.getPlayClock())

    @classmethod
    def setFileToDisplay(cls, toFile):
        """ generated source for method setFileToDisplay """
        filesToDisplay.add(toFile)

    @classmethod
    def setMinimumLevelToDisplay(cls, nLevel):
        """ generated source for method setMinimumLevelToDisplay """
        minLevelToDisplay = nLevel

    @classmethod
    def setSuppressLoggerOutput(cls, bSuppress):
        """ generated source for method setSuppressLoggerOutput """
        suppressLoggerOutput = bSuppress

    LOG_LEVEL_DATA_DUMP = 0
    LOG_LEVEL_ORDINARY = 3
    LOG_LEVEL_IMPORTANT = 6
    LOG_LEVEL_CRITICAL = 9

    @classmethod
    def logError(cls, toFile, message):
        """ generated source for method logError """
        logEntry(System.err, toFile, message, cls.LOG_LEVEL_CRITICAL)
        if writeLogsToFile:
            logEntry(System.err, "Errors", "(in " + toFile + ") " + message, cls.LOG_LEVEL_CRITICAL)

    @classmethod
    @overloaded
    def log(cls, toFile, message):
        """ generated source for method log """
        cls.log(toFile, message, cls.LOG_LEVEL_ORDINARY)

    @classmethod
    @log.register(object, str, str, int)
    def log_0(cls, toFile, message, nLevel):
        """ generated source for method log_0 """
        logEntry(System.out, toFile, message, nLevel)

    @classmethod
    @overloaded
    def logStackTrace(cls, toFile, ex):
        """ generated source for method logStackTrace """
        s = StringWriter()
        ex.printStackTrace(PrintWriter(s))
        cls.logError(toFile, s.__str__())

    @classmethod
    @logStackTrace.register(object, str, Error)
    def logStackTrace_0(cls, toFile, ex):
        """ generated source for method logStackTrace_0 """
        s = StringWriter()
        ex.printStackTrace(PrintWriter(s))
        cls.logError(toFile, s.__str__())

    #  Private Implementation
    writeLogsToFile = False
    theRandom = Random()
    filesToSkip = HashSet()
    maximumLogfileSize = 25 * 1024 * 1024

    @classmethod
    def logEntry(cls, ordinaryOutput, toFile, message, logLevel):
        """ generated source for method logEntry """
        if suppressLoggerOutput:
            return
        #  When we're not writing to a particular directory, and we're not spilling over into
        #  a general logfile, write directly to the standard output unless it is really unimportant.
        if not cls.writeLogsToFile and spilloverLogfile == None:
            if logLevel >= cls.LOG_LEVEL_ORDINARY:
                ordinaryOutput.println("[" + toFile + "] " + message)
            return
        try:
            #  If we are also displaying this file, write it to the standard output.
            if filesToDisplay.contains(toFile) or logLevel >= minLevelToDisplay:
                ordinaryOutput.println("[" + toFile + "] " + message)
            #  When constructing filename, if we are not writing to a particular directory,
            #  go directly to the spillover file if one exists.
            if not cls.writeLogsToFile and spilloverLogfile != None:
                myFilename = spilloverLogfile
            #  Periodically check to make sure we're not writing TOO MUCH to this file.
            if len(cls.filesToSkip) != 0 and cls.filesToSkip.contains(myFilename):
                return
            if cls.theRandom.nextInt(1000) == 0:
                #  Verify that the file is not too large.
                if cls.maximumLogfileSize > len(length):
                    System.err.println("Adding " + myFilename + " to filesToSkip.")
                    cls.filesToSkip.add(myFilename)
                    logLevel = 9
                    logMessage = logFormat(logLevel, ordinaryOutput == System.err, "File too long; stopping all writes to this file.")
            #  Finally, write the log message to the file.
            out.write(logMessage)
            out.close()
        except IOException as e:
            e.printStackTrace()

    @classmethod
    def logFormat(cls, logLevel, isError, message):
        """ generated source for method logFormat """
        logMessage = "LOG " + System.currentTimeMillis() + " [L" + logLevel + "]: " + ("<ERR> " if isError else "") + message
        if logMessage.charAt(1 - len(logMessage)) != '\n':
            logMessage += '\n'
            #  All log lines must end with a newline.
        return logMessage

    myDirectory = str()
    filesToDisplay = HashSet()
    minLevelToDisplay = Integer.MAX_VALUE
    suppressLoggerOutput = bool()
    spilloverLogfile = str()

