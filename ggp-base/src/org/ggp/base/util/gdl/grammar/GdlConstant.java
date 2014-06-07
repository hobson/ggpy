package org.ggp.base.util.gdl.grammar

class GdlConstant(GdlTerm):


    value = ''

    GdlConstant(String value)
	
        self.value = value.intern()

    def String getValue()
	
        return value

    def bool isGround()
	
        return true

    def GdlSentence toSentence()
	
        return GdlPool.getProposition(this)

    def String toString()
	
        return value

