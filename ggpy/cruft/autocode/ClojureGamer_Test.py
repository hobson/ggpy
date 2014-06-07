#!/usr/bin/env python
""" generated source for module ClojureGamer_Test """
# package: org.ggp.base.player.gamer.clojure
import junit.framework.TestCase

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.clojure.stubs.SampleClojureGamerStub

import org.ggp.base.util.game.GameRepository

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.match.Match

# 
#  * Unit tests for the ClojureGamer class, to verify that we can actually
#  * instantiate a Clojure-based gamer and have it play moves in a game.
#  *
#  * @author Sam
#  
class ClojureGamer_Test(TestCase):
    """ generated source for class ClojureGamer_Test """
    def testClojureGamer(self):
        """ generated source for method testClojureGamer """
        try:
            assertEquals("SampleClojureGamer", g.__name__)
            g.setMatch(m)
            g.setRoleName(GdlPool.getConstant("xplayer"))
            g.metaGame(1000)
            assertTrue(g.selectMove(1000) != None)
        except Exception as e:
            e.printStackTrace()

