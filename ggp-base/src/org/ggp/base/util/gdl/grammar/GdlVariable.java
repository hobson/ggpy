package org.ggp.base.util.gdl.grammar

class GdlVariable(GdlTerm):


    name = ''

    GdlVariable(String name)
	
        self.name = name.intern()

    def String getName()
	
        return name

    def bool isGround()
	
        return false

    def GdlSentence toSentence()
	
        throw new RuntimeException("Unable to convert a GdlVariable to a GdlSentence!")

    def String toString()
	
        return name

