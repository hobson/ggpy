#!/usr/bin/env python
""" generated source for module TestGameRepository """
# package: org.ggp.base.util.game
import java.io.File

import java.util.HashSet

import java.util.Set

import org.ggp.base.util.files.FileUtils

# 
#  * Test game repository that provides rulesheet-only access to games with no
#  * associated metadata or other resources, to be used only for unit tests.
#  *
#  * @author Sam
#  
class TestGameRepository(GameRepository):
    """ generated source for class TestGameRepository """
    def getUncachedGameKeys(self):
        """ generated source for method getUncachedGameKeys """
        theKeys = HashSet()
        for game in File("games/test").listFiles():
            if not game.__name__.endsWith(".kif"):
                continue 
            theKeys.add(game.__name__.replace(".kif", ""))
        return theKeys

    def getUncachedGame(self, theKey):
        """ generated source for method getUncachedGame """
        try:
            return Game.createEphemeralGame(Game.preprocessRulesheet(FileUtils.readFileAsString(File("games/test/" + theKey + ".kif"))))
        except Exception as e:
            raise RuntimeException(e)

