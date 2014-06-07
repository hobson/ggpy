#!/usr/bin/env python
""" generated source for module Role """
# package: org.ggp.base.util.statemachine
import java.io.Serializable

import java.util.ArrayList

import java.util.List

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlRelation

# 
#  * A Role represents the name used for a player in a game description.
#  * <p>
#  * The list of roles defined in a game description can be extracted
#  * using the {@link #computeRoles(List)} method.
#  
@SuppressWarnings("serial")
class Role(Serializable):
    """ generated source for class Role """
    name = GdlConstant()

    def __init__(self, name):
        """ generated source for method __init__ """
        super(Role, self).__init__()
        self.name = name

    def equals(self, o):
        """ generated source for method equals """
        if (o != None) and (isinstance(o, (Role, ))):
            return role.name == self.name
        return False

    def getName(self):
        """ generated source for method getName """
        return self.name

    def hashCode(self):
        """ generated source for method hashCode """
        return self.name.hashCode()

    def __str__(self):
        """ generated source for method toString """
        return self.name.__str__()

    # 
    #      * Compute all of the roles in a game, in the correct order.
    #      * <p>
    #      * Order matters, because a joint move is defined as an ordered list
    #      * of moves, in which the order determines which player took which of
    #      * the moves. This function will give an ordered list in which the roles
    #      * have that correct order.
    #      
    @classmethod
    def computeRoles(cls, description):
        """ generated source for method computeRoles """
        roles = ArrayList()
        for gdl in description:
            if isinstance(gdl, (GdlRelation, )):
                if relation.__name__.getValue() == "role":
                    roles.add(Role(relation.get(0)))
        return roles

