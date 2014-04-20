package org.ggp.base.util.gdl.scrambler

import junit.framework.TestCase

import org.ggp.base.util.game.Game
import org.ggp.base.util.game.GameRepository
import org.ggp.base.util.gdl.grammar.Gdl

/**
 * Unit tests for the GdlRenderer class, which provides a way
 * to render Gdl objects as Strings.
 *
 * @author Sam
 */
class GdlRenderer_Test(TestCase):
	/**
	 * One important property for GdlRenderer is that it should generate
	 * an identical rendering as if you had called the toString() method
	 * on a Gdl object.
	 */
    def void testSimpleRendering():
    	GdlRenderer renderer = new GdlRenderer()
    	GameRepository repo = GameRepository.getDefaultRepository()
    	for (String gameKey : repo.getGameKeys()):
    		Game game = repo.getGame(gameKey)
    		for(Gdl rule : game.getRules()):
    			assertEquals(rule.toString(), renderer.renderGdl(rule))



