#!/usr/bin/env python
""" generated source for module GdlUtils """
# package: org.ggp.base.util.gdl
import java.util.ArrayList

import java.util.Collection

import java.util.Collections

import java.util.HashMap

import java.util.HashSet

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

class GdlUtils(object):
    """ generated source for class GdlUtils """
    # TODO (AL): Check if we can switch over to just having this return a set.
    @classmethod
    def getVariables(cls, gdl):
        """ generated source for method getVariables """
        variablesList = ArrayList()
        variables = HashSet()
        GdlVisitors.visitAll(gdl, GdlVisitor())
        return variablesList

    @classmethod
    def getVariableNames(cls, gdl):
        """ generated source for method getVariableNames """
        variables = cls.getVariables(gdl)
        variableNames = ArrayList()
        for variable in variables:
            variableNames.add(variable.__name__)
        return variableNames

    @classmethod
    def getSentencesInRuleBody(cls, rule):
        """ generated source for method getSentencesInRuleBody """
        result = ArrayList()
        for literal in rule.getBody():
            addSentencesInLiteral(literal, result)
        return result

    @classmethod
    def addSentencesInLiteral(cls, literal, sentences):
        """ generated source for method addSentencesInLiteral """
        if isinstance(literal, (GdlSentence, )):
            sentences.add(literal)
        elif isinstance(literal, (GdlNot, )):
            cls.addSentencesInLiteral(not_.getBody(), sentences)
        elif isinstance(literal, (GdlOr, )):
            while i < or_.arity():
                pass
                i += 1
        elif not (isinstance(literal, (GdlDistinct, ))):
            raise RuntimeException("Unexpected GdlLiteral type encountered: " + literal.__class__.getSimpleName())

    @classmethod
    def getTupleFromSentence(cls, sentence):
        """ generated source for method getTupleFromSentence """
        if isinstance(sentence, (GdlProposition, )):
            return Collections.emptyList()
        # A simple crawl through the sentence.
        tuple_ = ArrayList()
        try:
            addBodyToTuple(sentence.getBody(), tuple_)
        except RuntimeException as e:
            raise RuntimeException(e.getMessage() + "\nSentence was " + sentence)
        return tuple_

    @classmethod
    def addBodyToTuple(cls, body, tuple_):
        """ generated source for method addBodyToTuple """
        for term in body:
            if isinstance(term, (GdlConstant, )):
                tuple_.add(term)
            elif isinstance(term, (GdlVariable, )):
                tuple_.add(term)
            elif isinstance(term, (GdlFunction, )):
                cls.addBodyToTuple(function_.getBody(), tuple_)
            else:
                raise RuntimeException("Unforeseen Gdl tupe in SentenceModel.addBodyToTuple()")

    @classmethod
    def getTupleFromGroundSentence(cls, sentence):
        """ generated source for method getTupleFromGroundSentence """
        if isinstance(sentence, (GdlProposition, )):
            return Collections.emptyList()
        # A simple crawl through the sentence.
        tuple_ = ArrayList()
        try:
            addBodyToGroundTuple(sentence.getBody(), tuple_)
        except RuntimeException as e:
            raise RuntimeException(e.getMessage() + "\nSentence was " + sentence)
        return tuple_

    @classmethod
    def addBodyToGroundTuple(cls, body, tuple_):
        """ generated source for method addBodyToGroundTuple """
        for term in body:
            if isinstance(term, (GdlConstant, )):
                tuple_.add(term)
            elif isinstance(term, (GdlVariable, )):
                raise RuntimeException("Asking for a ground tuple of a non-ground sentence")
            elif isinstance(term, (GdlFunction, )):
                cls.addBodyToGroundTuple(function_.getBody(), tuple_)
            else:
                raise RuntimeException("Unforeseen Gdl tupe in SentenceModel.addBodyToTuple()")

    @classmethod
    def getAssignmentMakingLeftIntoRight(cls, left, right):
        """ generated source for method getAssignmentMakingLeftIntoRight """
        assignment = HashMap()
        if not left.__name__ == right.__name__:
            return None
        if left.arity() != right.arity():
            return None
        if left.arity() == 0:
            return Collections.emptyMap()
        if not fillAssignmentBody(assignment, left.getBody(), right.getBody()):
            return None
        return assignment

    @classmethod
    def fillAssignmentBody(cls, assignment, leftBody, rightBody):
        """ generated source for method fillAssignmentBody """
        # left body contains variables; right body shouldn't
        if len(leftBody) != len(rightBody):
            return False
        i = 0
        while i < len(leftBody):
            if isinstance(leftTerm, (GdlConstant, )):
                if not leftTerm == rightTerm:
                    return False
            elif isinstance(leftTerm, (GdlVariable, )):
                if assignment.containsKey(leftTerm):
                    if not assignment.get(leftTerm) == rightTerm:
                        return False
                else:
                    if not (isinstance(rightTerm, (GdlConstant, ))):
                        return False
                    assignment.put(leftTerm, rightTerm)
            elif isinstance(leftTerm, (GdlFunction, )):
                if not (isinstance(rightTerm, (GdlFunction, ))):
                    return False
                if not leftFunction.__name__ == rightFunction.__name__:
                    return False
                if not cls.fillAssignmentBody(assignment, leftFunction.getBody(), rightFunction.getBody()):
                    return False
            i += 1
        return True

    @classmethod
    @overloaded
    def containsTerm(cls, sentence, term):
        """ generated source for method containsTerm """
        if isinstance(sentence, (GdlProposition, )):
            return False
        return cls.containsTerm(sentence.getBody(), term)

    @classmethod
    @containsTerm.register(object, List, GdlTerm)
    def containsTerm_0(cls, body, term):
        """ generated source for method containsTerm_0 """
        for curTerm in body:
            if curTerm == term:
                return True
            if isinstance(curTerm, (GdlFunction, )):
                if cls.containsTerm((curTerm).getBody(), term):
                    return True
        return False

