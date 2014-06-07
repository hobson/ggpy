#!/usr/bin/env python
""" generated source for module PythonGamer """
# package: org.ggp.base.player.gamer.python
import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.exception.AbortingException

import org.ggp.base.player.gamer.exception.GamePreviewException

import org.ggp.base.player.gamer.exception.MetaGamingException

import org.ggp.base.player.gamer.exception.MoveSelectionException

import org.ggp.base.player.gamer.exception.StoppingException

import org.ggp.base.util.game.Game

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.logging.GamerLogger

import org.python.core.PyObject

import org.python.util.PythonInterpreter

# 
#  * PythonGamer is a superclass that allows you to hook Python gamers into the
#  * rest of the Java framework. In order to do this, do the following:
#  *
#  * 1) Create a subclass of PythonGamer that overrides getPythonGamerName() and
#  *    getPythonGamerModule() to indicate where the Python source code file is.
#  *    This is the Java stub that refers to the real Python gamer class.
#  *
#  * 2) Create the Python source code file, in the /src_py/ directory in the root
#  *    directory for this project. Make sure that the stub points to this class,
#  *    and that the Python class is a valid subclass of Gamer.
#  *
#  * For examples where this has already been done, see @PythonRandomGamerStub, which
#  * is implemented in Python and hooks into the Java framework using the PythonGamer stub.
#  *
#  * @author Sam
#  * @author evancox
#  
class PythonGamer(Gamer):
    """ generated source for class PythonGamer """
    thePythonGamer = Gamer()

    def getPythonGamerName(self):
        """ generated source for method getPythonGamerName """

    def getPythonGamerModule(self):
        """ generated source for method getPythonGamerModule """

    #  Gamer stubs are lazily loaded because the Python interface takes
    #  time to initialize, so we only want to load it when necessary, and
    #  not for light-weight things like returning the player name.
    def lazilyLoadGamerStub(self):
        """ generated source for method lazilyLoadGamerStub """
        if self.thePythonGamer == None:
            try:
                #  Load in the Python gamer, using a Jython intepreter.
                interpreter.exec_("from " + self.getPythonGamerModule() + " import " + self.getPythonGamerName())
                self.thePythonGamer = PyGamerObject.__tojava__(Gamer.__class__)
            except Exception as e:
                GamerLogger.logError("GamePlayer", "Caught exception in Python initialization:")
                GamerLogger.logStackTrace("GamePlayer", e)

    #  The following methods are overriden as 'final' because they should not
    #  be changed in subclasses of this class. Subclasses of this class should
    #  only implement getPythonGamerName() and getPythonGamerModule(), and then
    #  implement the real methods in the actual Python gamer. Essentially, any
    #  subclass of this class is a Java-implementation stub for the actual real
    #  Python implementation.
    def preview(self, game, timeout):
        """ generated source for method preview """
        self.lazilyLoadGamerStub()
        try:
            self.thePythonGamer.preview(game, timeout)
        except GamePreviewException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Python stateMachinePreview:")
            GamerLogger.logStackTrace("GamePlayer", e)

    def metaGame(self, timeout):
        """ generated source for method metaGame """
        self.lazilyLoadGamerStub()
        self.thePythonGamer.setMatch(getMatch())
        self.thePythonGamer.setRoleName(getRoleName())
        try:
            self.thePythonGamer.metaGame(timeout)
        except MetaGamingException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Python stateMachineMetaGame:")
            GamerLogger.logStackTrace("GamePlayer", e)

    def selectMove(self, timeout):
        """ generated source for method selectMove """
        self.lazilyLoadGamerStub()
        self.thePythonGamer.setMatch(getMatch())
        self.thePythonGamer.setRoleName(getRoleName())
        try:
            return self.thePythonGamer.selectMove(timeout)
        except MoveSelectionException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Python stateMachineSelectMove:")
            GamerLogger.logStackTrace("GamePlayer", e)
            return None

    def stop(self):
        """ generated source for method stop """
        self.lazilyLoadGamerStub()
        self.thePythonGamer.setMatch(getMatch())
        self.thePythonGamer.setRoleName(getRoleName())
        try:
            self.thePythonGamer.stop()
        except StoppingException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Python stateMachineStop:")
            GamerLogger.logStackTrace("GamePlayer", e)

    def abort(self):
        """ generated source for method abort """
        self.lazilyLoadGamerStub()
        self.thePythonGamer.setMatch(getMatch())
        self.thePythonGamer.setRoleName(getRoleName())
        try:
            self.thePythonGamer.abort()
        except AbortingException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Python stateMachineAbort:")
            GamerLogger.logStackTrace("GamePlayer", e)

    def getName(self):
        """ generated source for method getName """
        return self.getPythonGamerName()

