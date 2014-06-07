#!/usr/bin/env python
""" generated source for module ClojureGamer """
# package: org.ggp.base.player.gamer.clojure
import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.exception.AbortingException

import org.ggp.base.player.gamer.exception.GamePreviewException

import org.ggp.base.player.gamer.exception.MetaGamingException

import org.ggp.base.player.gamer.exception.MoveSelectionException

import org.ggp.base.player.gamer.exception.StoppingException

import org.ggp.base.util.game.Game

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.logging.GamerLogger

import clojure.lang.RT

import clojure.lang.Var

# 
#  * ClojureGamer is a superclass that allows you to hook Clojure gamers into the
#  * rest of the Java framework. In order to do this, do the following:
#  *
#  * 1) Create a subclass of ClojureGamer that overrides getClojureGamerFile() and
#  *    getClojureGamerName() to indicate where the Clojure source code file is.
#  *    This is the Java stub that refers to the real Clojure gamer class.
#  *
#  * 2) Create the Clojure source code file, in the /src_clj/ directory in the root
#  *    directory for this project. Make sure that the stub points to this class,
#  *    and that the Clojure class is a valid subclass of Gamer.
#  *
#  * For examples where this has already been done, see @ClojureLegalGamerStub,
#  * which is implemented in Clojure and hook into the Java framework using the
#  * ClojureGamer stub.
#  *
#  * @author Sam Schreiber
#  
class ClojureGamer(Gamer):
    """ generated source for class ClojureGamer """
    theClojureGamer = Gamer()

    def getClojureGamerFile(self):
        """ generated source for method getClojureGamerFile """

    def getClojureGamerName(self):
        """ generated source for method getClojureGamerName """

    #  Gamer stubs are lazily loaded because the Clojure interface takes
    #  time to initialize, so we only want to load it when necessary, and
    #  not for light-weight things like returning the player name.
    def lazilyLoadGamerStub(self):
        """ generated source for method lazilyLoadGamerStub """
        if self.theClojureGamer == None:
            try:
                #  Load the Clojure script -- as a side effect this initializes the runtime.
                RT.loadResourceScript(self.getClojureGamerFile() + ".clj")
                #  Get a reference to the gamer-generating function.
                #  Call it!
                self.theClojureGamer = gamerVar.invoke()
            except Exception as e:
                GamerLogger.logError("GamePlayer", "Caught exception in Clojure initialization:")
                GamerLogger.logStackTrace("GamePlayer", e)

    #  The following methods are overriden as 'final' because they should not
    #  be changed in subclasses of this class. Subclasses of this class should
    #  only implement getClojureGamerFile() and getClojureGamerName(), and then
    #  implement the real methods in the actual Clojure gamer. Essentially, any
    #  subclass of this class is a Java-implementation stub for the actual real
    #  Clojure implementation.
    def preview(self, game, timeout):
        """ generated source for method preview """
        self.lazilyLoadGamerStub()
        try:
            self.theClojureGamer.preview(game, timeout)
        except GamePreviewException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Clojure stateMachineMetaGame:")
            GamerLogger.logStackTrace("GamePlayer", e)

    def metaGame(self, timeout):
        """ generated source for method metaGame """
        self.lazilyLoadGamerStub()
        self.theClojureGamer.setMatch(getMatch())
        self.theClojureGamer.setRoleName(getRoleName())
        try:
            self.theClojureGamer.metaGame(timeout)
        except MetaGamingException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Clojure stateMachineMetaGame:")
            GamerLogger.logStackTrace("GamePlayer", e)

    def selectMove(self, timeout):
        """ generated source for method selectMove """
        self.lazilyLoadGamerStub()
        self.theClojureGamer.setMatch(getMatch())
        self.theClojureGamer.setRoleName(getRoleName())
        try:
            return self.theClojureGamer.selectMove(timeout)
        except MoveSelectionException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Clojure stateMachineSelectMove:")
            GamerLogger.logStackTrace("GamePlayer", e)
            return None

    def stop(self):
        """ generated source for method stop """
        self.lazilyLoadGamerStub()
        self.theClojureGamer.setMatch(getMatch())
        self.theClojureGamer.setRoleName(getRoleName())
        try:
            self.theClojureGamer.stop()
        except StoppingException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Clojure stateMachineStop:")
            GamerLogger.logStackTrace("GamePlayer", e)

    def abort(self):
        """ generated source for method abort """
        self.lazilyLoadGamerStub()
        self.theClojureGamer.setMatch(getMatch())
        self.theClojureGamer.setRoleName(getRoleName())
        try:
            self.theClojureGamer.abort()
        except AbortingException as e:
            GamerLogger.logError("GamePlayer", "Caught exception in Clojure stateMachineAbort:")
            GamerLogger.logStackTrace("GamePlayer", e)

    def getName(self):
        """ generated source for method getName """
        return self.getClojureGamerName()

