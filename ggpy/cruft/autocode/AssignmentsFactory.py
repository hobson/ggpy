#!/usr/bin/env python
""" generated source for module AssignmentsFactory """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.ArrayList

import java.util.Collection

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.SentenceDomainModel

import org.ggp.base.util.gdl.model.SentenceDomainModels

import org.ggp.base.util.gdl.model.SentenceDomainModels.VarDomainOpts

import org.ggp.base.util.gdl.model.SentenceForm

class AssignmentsFactory(object):
    """ generated source for class AssignmentsFactory """
    @classmethod
    @overloaded
    def getAssignmentsForRule(cls, rule, model, functionInfoMap, completedSentenceFormValues):
        """ generated source for method getAssignmentsForRule """
        return AssignmentsImpl(rule, SentenceDomainModels.getVarDomains(rule, model, VarDomainOpts.INCLUDE_HEAD), functionInfoMap, completedSentenceFormValues)

    @classmethod
    @getAssignmentsForRule.register(object, GdlRule, Map, Map, Map)
    def getAssignmentsForRule_0(cls, rule, varDomains, functionInfoMap, completedSentenceFormValues):
        """ generated source for method getAssignmentsForRule_0 """
        return AssignmentsImpl(rule, varDomains, functionInfoMap, completedSentenceFormValues)

    @classmethod
    def getAssignmentsWithRecursiveInput(cls, rule, model, form, input, functionInfoMap, completedSentenceFormValues):
        """ generated source for method getAssignmentsWithRecursiveInput """
        # Look for the literal(s) in the rule with the sentence form of the
        # recursive input. This can be tricky if there are multiple matching
        # literals.
        matchingLiterals = ArrayList()
        for literal in rule.getBody():
            if isinstance(literal, (GdlSentence, )):
                if form.matches(literal):
                    matchingLiterals.add(literal)
        assignmentsList = ArrayList()
        for matchingLiteral in matchingLiterals:
            # left has the variables, right has the constants
            if preassignment != None:
                # TODO: This one getVarDomains call is why a lot of
                # SentenceModel/DomainModel stuff is required. Can
                # this be better factored somehow?
                assignmentsList.add(assignments)
        if len(assignmentsList) == 0:
            return AssignmentsImpl()
        if len(assignmentsList) == 1:
            return assignmentsList.get(0)
        raise RuntimeException("Not yet implemented: assignments for recursive functions with multiple recursive conjuncts")
        # TODO: Plan to implement by subclassing Assignments into something
        # that contains and iterates over multiple Assignments

    # TODO: Put the constructor that uses the SentenceModel here

