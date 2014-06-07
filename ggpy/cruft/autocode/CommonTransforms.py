#!/usr/bin/env python
""" generated source for module CommonTransforms """
# package: org.ggp.base.util.gdl.transforms
import java.util.ArrayList

import java.util.List

import java.util.Map

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

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import com.google.common.collect.Lists

# 
#  * @author Sam Schreiber
#  
class CommonTransforms(object):
    """ generated source for class CommonTransforms """
    # We can avoid lots of client-side casts by providing these functions for the more specific cases -AL
    @classmethod
    @overloaded
    def replaceVariable(cls, rule, toSubstitute, theReplacement):
        """ generated source for method replaceVariable """
        return replaceVariableInternal(rule, toSubstitute, theReplacement)

    @classmethod
    @replaceVariable.register(object, GdlLiteral, GdlVariable, GdlTerm)
    def replaceVariable_0(cls, literal, toSubstitute, theReplacement):
        """ generated source for method replaceVariable_0 """
        return replaceVariableInternal(literal, toSubstitute, theReplacement)

    @classmethod
    @replaceVariable.register(object, GdlSentence, GdlVariable, GdlTerm)
    def replaceVariable_1(cls, sentence, toSubstitute, theReplacement):
        """ generated source for method replaceVariable_1 """
        return replaceVariableInternal(sentence, toSubstitute, theReplacement)

    @classmethod
    def replaceVariableInternal(cls, gdl, toSubstitute, theReplacement):
        """ generated source for method replaceVariableInternal """
        if isinstance(gdl, (GdlDistinct, )):
            return GdlPool.getDistinct(cls.replaceVariableInternal((gdl).getArg1(), toSubstitute, theReplacement), cls.replaceVariableInternal((gdl).getArg2(), toSubstitute, theReplacement))
        elif isinstance(gdl, (GdlNot, )):
            return GdlPool.getNot(cls.replaceVariableInternal((gdl).getBody(), toSubstitute, theReplacement))
        elif isinstance(gdl, (GdlOr, )):
            while i < or_.arity():
                rval.add(cls.replaceVariableInternal(or_.get(i), toSubstitute, theReplacement))
                i += 1
            return GdlPool.getOr(rval)
        elif isinstance(gdl, (GdlProposition, )):
            return gdl
        elif isinstance(gdl, (GdlRelation, )):
            while i < rel.arity():
                rval.add(cls.replaceVariableInternal(rel.get(i), toSubstitute, theReplacement))
                i += 1
            return GdlPool.getRelation(rel.__name__, rval)
        elif isinstance(gdl, (GdlRule, )):
            while i < rule.arity():
                rval.add(cls.replaceVariableInternal(rule.get(i), toSubstitute, theReplacement))
                i += 1
            return GdlPool.getRule(cls.replaceVariableInternal(rule.getHead(), toSubstitute, theReplacement), rval)
        elif isinstance(gdl, (GdlConstant, )):
            return gdl
        elif isinstance(gdl, (GdlFunction, )):
            while i < func.arity():
                rval.add(cls.replaceVariableInternal(func.get(i), toSubstitute, theReplacement))
                i += 1
            return GdlPool.getFunction(func.__name__, rval)
        elif isinstance(gdl, (GdlVariable, )):
            if gdl == toSubstitute:
                return theReplacement
            else:
                return gdl
        else:
            raise RuntimeException("Uh oh, gdl hierarchy must have been extended without updating this code.")

    # Apply a variable assignment to a Gdl object
    @classmethod
    @overloaded
    def replaceVariables(cls, sentence, assignment):
        """ generated source for method replaceVariables """
        return replaceVariablesInternal(sentence, assignment)

    @classmethod
    @replaceVariables.register(object, GdlTerm, Map)
    def replaceVariables_0(cls, term, assignment):
        """ generated source for method replaceVariables_0 """
        return replaceVariablesInternal(term, assignment)

    @classmethod
    @replaceVariables.register(object, GdlLiteral, Map)
    def replaceVariables_1(cls, literal, assignment):
        """ generated source for method replaceVariables_1 """
        return replaceVariablesInternal(literal, assignment)

    @classmethod
    @replaceVariables.register(object, GdlDistinct, Map)
    def replaceVariables_2(cls, distinct, assignment):
        """ generated source for method replaceVariables_2 """
        return replaceVariablesInternal(distinct, assignment)

    @classmethod
    @replaceVariables.register(object, GdlRule, Map)
    def replaceVariables_3(cls, rule, assignment):
        """ generated source for method replaceVariables_3 """
        return replaceVariablesInternal(rule, assignment)

    @classmethod
    def replaceVariablesInternal(cls, gdl, assignment):
        """ generated source for method replaceVariablesInternal """
        if isinstance(gdl, (GdlProposition, )):
            return gdl
        elif isinstance(gdl, (GdlRelation, )):
            for term in relation.getBody():
                newBody.add(cls.replaceVariables(term, assignment))
            return GdlPool.getRelation(name, newBody)
        elif isinstance(gdl, (GdlConstant, )):
            return gdl
        elif isinstance(gdl, (GdlVariable, )):
            if assignment.containsKey(gdl):
                return assignment.get(gdl)
            else:
                return gdl
        elif isinstance(gdl, (GdlFunction, )):
            for term in function_.getBody():
                newBody.add(cls.replaceVariables(term, assignment))
            return GdlPool.getFunction(name, newBody)
        elif isinstance(gdl, (GdlDistinct, )):
            return GdlPool.getDistinct(arg1, arg2)
        elif isinstance(gdl, (GdlNot, )):
            return GdlPool.getNot(cls.replaceVariables(internal, assignment))
        elif isinstance(gdl, (GdlOr, )):
            while i < or_.arity():
                newInternals.add(cls.replaceVariables(or_.get(i), assignment))
                i += 1
            return GdlPool.getOr(newInternals)
        elif isinstance(gdl, (GdlRule, )):
            for conjunct in rule.getBody():
                newBody.add(cls.replaceVariables(conjunct, assignment))
            return GdlPool.getRule(newHead, newBody)
        else:
            raise RuntimeException("Unforeseen Gdl subtype " + gdl.__class__.getSimpleName())

    @classmethod
    def replaceHead(cls, sentence, newHead):
        """ generated source for method replaceHead """
        return GdlPool.getRelation(newHead, sentence.getBody())

