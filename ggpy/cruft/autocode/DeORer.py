#!/usr/bin/env python
""" generated source for module DeORer """
# package: org.ggp.base.util.gdl.transforms
import java.util.ArrayList

import java.util.List

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlVariable

# 
#  * As a GDL transformer, this class takes in a GDL description of a game,
#  * transforms it in some way, and outputs a new GDL descriptions of a game
#  * which is functionally equivalent to the original game.
#  *
#  * DeORer removes OR rules from the GDL. Technically, these rules shouldn't
#  * be in the GDL in the first place, but it's very straightforward to remove
#  * them, so we do that so that we can handle GDL descriptions that use OR.
#  *
#  * @author Ethan Dreyfuss
#  
class DeORer(object):
    """ generated source for class DeORer """
    @classmethod
    def run(cls, description):
        """ generated source for method run """
        newDesc = ArrayList()
        for gdl in description:
            if isinstance(gdl, (GdlRule, )):
                for body in newBodies:
                    newDesc.add(GdlPool.getRule(rule.getHead(), body))
            else:
                newDesc.add(gdl)
        return newDesc

    @classmethod
    def deOr(cls, rhs):
        """ generated source for method deOr """
        wrapped = ArrayList()
        wrapped.add(rhs)
        return deOr2(wrapped)

    @classmethod
    def deOr2(cls, rhsList):
        """ generated source for method deOr2 """
        rval = ArrayList()
        expandedSomething = False
        for rhs in rhsList:
            if not expandedSomething:
                for lit in rhs:
                    if not expandedSomething:
                        if len(expandedList) > 1:
                            for replacement in expandedList:
                                if not (isinstance(replacement, (GdlLiteral, ))):
                                    raise RuntimeException("Top level return value is different type of gdl.")
                                newRhs.set(i, newLit)
                                rval.add(newRhs)
                            expandedSomething = True
                            break
                    i += 1
                if not expandedSomething:
                    rval.add(rhs)
            else:
                rval.add(rhs)
            # If I've already expanded this function call
        if not expandedSomething:
            return rhsList
        else:
            return cls.deOr2(rval)

    @classmethod
    def expandFirstOr(cls, gdl):
        """ generated source for method expandFirstOr """
        rval = List()
        expandedChild = List()
        if isinstance(gdl, (GdlDistinct, )):
            # Can safely be ignored, won't contain 'or'
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlNot, )):
            expandedChild = cls.expandFirstOr(not_.getBody())
            rval = ArrayList()
            for g in expandedChild:
                if not (isinstance(g, (GdlLiteral, ))):
                    raise RuntimeException("Not must have literal child.")
                rval.add(GdlPool.getNot(lit))
            return rval
        elif isinstance(gdl, (GdlOr, )):
            rval = ArrayList()
            while i < or_.arity():
                rval.add(or_.get(i))
                i += 1
            return rval
        elif isinstance(gdl, (GdlProposition, )):
            # Can safely be ignored, won't contain 'or'
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlRelation, )):
            # Can safely be ignored, won't contain 'or'
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlRule, )):
            raise RuntimeException("This should be used to remove 'or's from the body of a rule, and rules can't be nested")
        elif isinstance(gdl, (GdlConstant, )):
            # Can safely be ignored, won't contain 'or'
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlFunction, )):
            # Can safely be ignored, won't contain 'or'
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlVariable, )):
            # Can safely be ignored, won't contain 'or'
            rval = ArrayList()
            rval.add(gdl)
            return rval
        else:
            raise RuntimeException("Uh oh, gdl hierarchy must have been extended without updating this code.")

