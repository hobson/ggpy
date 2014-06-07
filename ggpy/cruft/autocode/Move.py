#!/usr/bin/env python
""" generated source for module Move """
# package: org.ggp.base.util.statemachine
import java.io.Serializable

import org.ggp.base.util.gdl.grammar.GdlTerm

# 
#  * A Move represents a possible move that can be made by a role. Each
#  * player makes exactly one move on every turn. This includes moves
#  * that represent passing, or taking no action.
#  * <p>
#  * Note that Move objects are not intrinsically tied to a role. They
#  * only express the action itself.
#  
@SuppressWarnings("serial")
class Move(Serializable):
    """ generated source for class Move """
    contents = GdlTerm()

    def __init__(self, contents):
        """ generated source for method __init__ """
        super(Move, self).__init__()
        self.contents = contents

    def equals(self, o):
        """ generated source for method equals """
        if (o != None) and (isinstance(o, (Move, ))):
            return move.contents == self.contents
        return False

    def getContents(self):
        """ generated source for method getContents """
        return self.contents

    def hashCode(self):
        """ generated source for method hashCode """
        return self.contents.hashCode()

    def __str__(self):
        """ generated source for method toString """
        return self.contents.__str__()

