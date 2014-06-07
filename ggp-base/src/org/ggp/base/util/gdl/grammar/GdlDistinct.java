package org.ggp.base.util.gdl.grammar

class GdlDistinct(GdlLiteral):


    arg1 = GdlTerm()
    arg2 = GdlTerm()
    private transient Boolean ground

    GdlDistinct(GdlTerm arg1, GdlTerm arg2)
	
        self.arg1 = arg1
        self.arg2 = arg2
        ground = null

    def GdlTerm getArg1()
	
        return arg1

    def GdlTerm getArg2()
	
        return arg2

    def bool isGround()
	
        if (ground == null)
		
            ground = arg1.isGround() && arg2.isGround()

        return ground

    def String toString()
	
        return "( distinct " + arg1 + " " + arg2 + " )"

