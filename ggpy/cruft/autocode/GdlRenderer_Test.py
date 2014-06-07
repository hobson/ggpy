#!/usr/bin/env python
""" generated source for module GdlRenderer_Test """
# package: org.ggp.base.util.gdl.scrambler
import junit.framework.TestCase

import org.ggp.base.util.game.Game

import org.ggp.base.util.game.GameRepository

import org.ggp.base.util.gdl.grammar.Gdl

# 
#  * Unit tests for the GdlRenderer class, which provides a way
#  * to render Gdl objects as Strings.
#  *
#  * @author Sam
#  
class GdlRenderer_Test(TestCase):
    """ generated source for class GdlRenderer_Test """
    # 
    # 	 * One important property for GdlRenderer is that it should generate
    # 	 * an identical rendering as if you had called the toString() method
    # 	 * on a Gdl object.
    # 	 
    def testSimpleRendering(self):
        """ generated source for method testSimpleRendering """
        renderer = GdlRenderer()
        repo = GameRepository.getDefaultRepository()
        for gameKey in repo.getGameKeys():
            for rule in game.getRules():
                assertEquals(rule.__str__(), renderer.renderGdl(rule))

