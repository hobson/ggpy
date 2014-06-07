#!/usr/bin/env python
""" generated source for module PythonGamer_Test """
# package: org.ggp.base.player.gamer.python
import junit.framework.TestCase

import org.ggp.base.player.gamer.Gamer

import org.ggp.base.player.gamer.python.stubs.SamplePythonGamerStub

import org.ggp.base.util.game.GameRepository

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.match.Match

# 
#  * Unit tests for the PythonGamer class, to verify that we can actually
#  * instantiate a Python-based gamer and have it play moves in a game.
#  *
#  * @author Sam
#  
class PythonGamer_Test(TestCase):
    """ generated source for class PythonGamer_Test """
    def testPythonGamer(self):
        """ generated source for method testPythonGamer """
        try:
            assertEquals("SamplePythonGamer", g.__name__)
            g.setMatch(m)
            g.setRoleName(GdlPool.getConstant("xplayer"))
            g.metaGame(1000)
            assertTrue(g.selectMove(1000) != None)
        except Exception as e:
            e.printStackTrace()

