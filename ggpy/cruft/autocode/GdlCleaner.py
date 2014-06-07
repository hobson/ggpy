#!/usr/bin/env python
""" generated source for module GdlCleaner """
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

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

# Cleans up various issues with games to make them more standardized.
class GdlCleaner(object):
    """ generated source for class GdlCleaner """
    MAX_ITERATIONS = 100
    BASE = GdlPool.getConstant("base")

    @classmethod
    def run(cls, description):
        """ generated source for method run """
        i = 0
        while i < cls.MAX_ITERATIONS:
            if newDescription == description:
                break
            description = newDescription
            i += 1
        return description

    @classmethod
    def runOnce(cls, description):
        """ generated source for method runOnce """
        newDescription = ArrayList()
        # First: Clean up all rules with zero-element bodies
        for gdl in description:
            if isinstance(gdl, (GdlRule, )):
                if rule.getBody().size() == 0:
                    newDescription.add(rule.getHead())
                else:
                    newDescription.add(gdl)
            else:
                newDescription.add(gdl)
        # TODO: Add (role ?player) where appropriate, i.e. in rules for
        # "legal" or "input" where the first argument is an undefined
        # variable
        # Get rid of "extra parentheses", i.e. zero-arity functions
        description = newDescription
        newDescription = ArrayList()
        for gdl in description:
            if isinstance(gdl, (GdlRelation, )):
                newDescription.add(cleanParentheses(gdl))
            elif isinstance(gdl, (GdlRule, )):
                newDescription.add(cleanParentheses(gdl))
            else:
                newDescription.add(gdl)
        # TODO: Get rid of GdlPropositions in the description
        # Get rid of (not (distinct _ _)) literals in rules
        # TODO: Expand to functions
        description = newDescription
        newDescription = ArrayList()
        for gdl in description:
            if isinstance(gdl, (GdlRule, )):
                if cleaned != None:
                    newDescription.add(cleaned)
            else:
                newDescription.add(gdl)
        # Get rid of the old style of "base" sentences (with arity more than 1, not in rules)
        # See e.g. current version of Qyshinsu on the Dresden server
        description = newDescription
        newDescription = ArrayList()
        removeBaseSentences = False
        for gdl in description:
            if isinstance(gdl, (GdlRelation, )):
                if relation.__name__ == cls.BASE and relation.arity() != 1:
                    removeBaseSentences = True
                    break
        # Note that in this case, we have to remove ALL of them or we might
        # misinterpret this as being the new kind of "base" relation
        for gdl in description:
            if isinstance(gdl, (GdlRelation, )):
                if removeBaseSentences and relation.__name__ == cls.BASE:
                    # Leave out the relation
                else:
                    newDescription.add(gdl)
            else:
                newDescription.add(gdl)
        return newDescription

    @classmethod
    def removeNotDistinctLiterals(cls, rule):
        """ generated source for method removeNotDistinctLiterals """
        while rule != None and getNotDistinctLiteral(rule) != None:
            rule = removeNotDistinctLiteral(rule, getNotDistinctLiteral(rule))
        return rule

    @classmethod
    def getNotDistinctLiteral(cls, rule):
        """ generated source for method getNotDistinctLiteral """
        for literal in rule.getBody():
            if isinstance(literal, (GdlNot, )):
                if isinstance(, (GdlDistinct, )):
                    # For now, we can only deal with this if not both are functions.
                    # That means we have to skip that case at this point.
                    if not (isinstance(, (GdlFunction, ))) or not (isinstance(, (GdlFunction, ))):
                        return not_
        return None

    # Returns null if the rule is useless.
    @classmethod
    def removeNotDistinctLiteral(cls, rule, notDistinctLiteral):
        """ generated source for method removeNotDistinctLiteral """
        # Figure out the substitution we want...
        # If we have two constants: Either remove one or
        # maybe get rid of the ___?
        # One is a variable: Replace the variable with the other thing
        # throughout the rule
        distinct = notDistinctLiteral.getBody()
        arg1 = distinct.getArg1()
        arg2 = distinct.getArg2()
        if arg1 == arg2:
            # Just remove that literal
            newBody.addAll(rule.getBody())
            newBody.remove(notDistinctLiteral)
            return GdlPool.getRule(rule.getHead(), newBody)
        if isinstance(arg1, (GdlVariable, )):
            # What we return will still have the not-distinct literal,
            # but it will get replaced in the next pass.
            # (Even if we have two variables, they will be equal next time through.)
            return CommonTransforms.replaceVariable(rule, arg1, arg2)
        if isinstance(arg2, (GdlVariable, )):
            return CommonTransforms.replaceVariable(rule, arg2, arg1)
        if isinstance(arg1, (GdlConstant, )) or isinstance(arg2, (GdlConstant, )):
            # We have two non-equal constants, or a constant and a function.
            # The rule should have no effect.
            return None
        # We have two functions. Complicated! (Have to replace them with unified version.)
        # We pass on this case for now.
        # TODO: Implement correctly.
        raise UnsupportedOperationException("We can't currently handle (not (distinct <function> <function>)).")

    @classmethod
    @overloaded
    def cleanParentheses(cls, rule):
        """ generated source for method cleanParentheses """
        cleanedHead = cls.cleanParentheses(rule.getHead())
        cleanedBody = ArrayList()
        for literal in rule.getBody():
            cleanedBody.add(cls.cleanParentheses(literal))
        return GdlPool.getRule(cleanedHead, cleanedBody)

    @classmethod
    @cleanParentheses.register(object, GdlLiteral)
    def cleanParentheses_0(cls, literal):
        """ generated source for method cleanParentheses_0 """
        if isinstance(literal, (GdlSentence, )):
            return cls.cleanParentheses(literal)
        elif isinstance(literal, (GdlDistinct, )):
            return GdlPool.getDistinct(term1, term2)
        elif isinstance(literal, (GdlNot, )):
            return GdlPool.getNot(cls.cleanParentheses(body))
        elif isinstance(literal, (GdlOr, )):
            while i < or_.arity():
                pass
                i += 1
            return GdlPool.getOr(disjuncts)
        raise RuntimeException("Unexpected literal type in GdlCleaner")

    @classmethod
    @cleanParentheses.register(object, GdlSentence)
    def cleanParentheses_1(cls, sentence):
        """ generated source for method cleanParentheses_1 """
        if isinstance(sentence, (GdlProposition, )):
            return sentence
        cleanedBody = ArrayList()
        for term in sentence.getBody():
            cleanedBody.add(cls.cleanParentheses(term))
        if len(cleanedBody) == 0:
            return GdlPool.getProposition(sentence.__name__)
        else:
            return GdlPool.getRelation(sentence.__name__, cleanedBody)

    @classmethod
    @cleanParentheses.register(object, GdlTerm)
    def cleanParentheses_2(cls, term):
        """ generated source for method cleanParentheses_2 """
        if isinstance(term, (GdlConstant, )) or isinstance(term, (GdlVariable, )):
            return term
        if isinstance(term, (GdlFunction, )):
            # The whole point of the function
            if function_.arity() == 0:
                return function_.__name__
            for functionTerm in function_.getBody():
                cleanedBody.add(cls.cleanParentheses(functionTerm))
            return GdlPool.getFunction(function_.__name__, cleanedBody)
        raise RuntimeException("Unexpected term type in GdlCleaner")

