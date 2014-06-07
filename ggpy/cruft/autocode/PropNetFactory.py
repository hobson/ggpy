#!/usr/bin/env python
""" generated source for module PropNetFactory """
# package: org.ggp.base.util.propnet.factory
import java.util.List

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.propnet.architecture.PropNet

import org.ggp.base.util.propnet.factory.converter.PropNetConverter

import org.ggp.base.util.propnet.factory.flattener.PropNetFlattener

import org.ggp.base.util.statemachine.Role

# 
#  * The PropNetFactory class defines the creation of PropNets from game
#  * descriptions.
#  
class PropNetFactory(object):
    """ generated source for class PropNetFactory """
    # 
    # 	 * Creates a PropNet from a game description using the following process:
    # 	 * <ol>
    # 	 * <li>Flattens the game description to remove variables.</li>
    # 	 * <li>Converts the flattened description into an equivalent PropNet.</li>
    # 	 * </ol>
    # 	 *
    # 	 * @param description
    # 	 *            A game description.
    # 	 * @return An equivalent PropNet.
    # 	 
    @classmethod
    def create(cls, description):
        """ generated source for method create """
        try:
            GamerLogger.log("StateMachine", "Converting...")
            return PropNetConverter().convert(Role.computeRoles(description), flatDescription)
        except Exception as e:
            GamerLogger.logStackTrace("StateMachine", e)
            return None

