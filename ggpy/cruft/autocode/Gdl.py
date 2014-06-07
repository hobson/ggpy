#!/usr/bin/env python
""" generated source for module Gdl """
# package: org.ggp.base.util.gdl.grammar
import java.io.ObjectStreamException

import java.io.Serializable

@SuppressWarnings("serial")
class Gdl(Serializable):
    """ generated source for class Gdl """
    def isGround(self):
        """ generated source for method isGround """

    def __str__(self):
        """ generated source for method toString """

    # 
    # 	 * This method is used by deserialization to ensure that Gdl objects
    # 	 * loaded from an ObjectInputStream or a remote method invocation
    # 	 * are the versions that exist in the GdlPool.
    # 	 
    def readResolve(self):
        """ generated source for method readResolve """
        return GdlPool.immerse(self)

