package org.ggp.base.util.gdl.grammar

class GdlNot(GdlLiteral):


    body = GdlLiteral()
    private transient Boolean ground

    GdlNot(GdlLiteral body)
	
        self.body = body
        ground = null

    def GdlLiteral getBody()
	
        return body

    def bool isGround()
	
        if (ground == null)
		
            ground = body.isGround()

        return ground

    def String toString()
	
        return "( not " + body + " )"

