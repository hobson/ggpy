#!/usr/bin/env python
""" generated source for module AssignmentFunction """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.ArrayList

import java.util.List

import java.util.Map

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableMap

import com.google.common.collect.Maps

class AssignmentFunction(object):
    """ generated source for class AssignmentFunction """
    # How is the AssignmentFunction going to operate?
    # Well, some of the variables are going to be
    # specified as having one or more of these functions
    # apply to them. (If multiple apply, they all have
    # to agree.)
    # We pass in the current value of the tuple and
    # it gives us the value desired (or null).
    # This means it just has to know which indices in
    # the tuple (i.e. which variables) correspond to
    # which slots in its native tuple.
    # Used when multiple assignment functions are relevant
    # to the same variable. In this case we call these other
    # functions with the same arguments and return null if
    # any of the answers differ.
    internalFunctions = ImmutableList()
    querySize = int()
    isInputConstant = ImmutableList()
    queryConstants = ImmutableMap()
    queryInputIndices = ImmutableList()
    function_ = ImmutableMap()

    # Some sort of trie might work better here...
    def __init__(self, internalFunctions, querySize, isInputConstant, queryConstants, queryInputIndices, function_):
        """ generated source for method __init__ """
        self.internalFunctions = internalFunctions
        self.querySize = querySize
        self.isInputConstant = isInputConstant
        self.queryConstants = queryConstants
        self.queryInputIndices = queryInputIndices
        self.function_ = function_

    @classmethod
    def create(cls, conjunct, functionInfo, rightmostVar, varOrder, preassignment):
        """ generated source for method create """
        # We have to set up the things mentioned above...
        internalFunctions = ArrayList()
        # We can traverse the conjunct for the list of variables/constants...
        terms = ArrayList()
        gatherVars(conjunct.getBody(), terms)
        # Note that we assume here that the var of interest only
        # appears once in the relation...
        varIndex = terms.indexOf(rightmostVar)
        if varIndex == -1:
            print "conjunct is: " + conjunct
            print "terms are: " + terms
            print "righmostVar is: " + rightmostVar
        terms.remove(rightmostVar)
        function_ = functionInfo.getValueMap(varIndex)
        # Set up inputs and such, using terms
        querySize = len(terms)
        isInputConstant = ArrayList(len(terms))
        queryConstants = Maps.newHashMap()
        queryInputIndices = ArrayList(len(terms))
        i = 0
        while i < len(terms):
            if isinstance(term, (GdlConstant, )):
                isInputConstant.add(True)
                queryConstants.put(i, term)
                queryInputIndices.add(-1)
            elif isinstance(term, (GdlVariable, )):
                # Is it in the head assignment?
                if preassignment.containsKey(term):
                    isInputConstant.add(True)
                    queryConstants.put(i, preassignment.get(term))
                    queryInputIndices.add(-1)
                else:
                    isInputConstant.add(False)
                    # 						queryConstants.add(null);
                    # What value do we put here?
                    # We want to grab some value out of the
                    # input tuple, which uses functional ordering
                    # Index of the relevant variable, by the
                    # assignment's ordering
                    queryInputIndices.add(varOrder.indexOf(term))
            i += 1
        return AssignmentFunction(ImmutableList.copyOf(internalFunctions), querySize, ImmutableList.copyOf(isInputConstant), ImmutableMap.copyOf(queryConstants), ImmutableList.copyOf(queryInputIndices), ImmutableMap.copyOf(function_))

    def functional(self):
        """ generated source for method functional """
        return (self.function_ != None)

    @classmethod
    def gatherVars(cls, body, terms):
        """ generated source for method gatherVars """
        for term in body:
            if isinstance(term, (GdlConstant, )) or isinstance(term, (GdlVariable, )):
                terms.add(term)
            elif isinstance(term, (GdlFunction, )):
                cls.gatherVars((term).getBody(), terms)

    def getValue(self, remainingTuple):
        """ generated source for method getValue """
        # We have a map from a tuple of GdlConstants
        # to the GdlConstant we need, provided by the FunctionInfo.
        # We need to make the tuple for this map.
        queryTuple = ArrayList(self.querySize)
        # Now we have to fill in the query
        i = 0
        while i < self.querySize:
            if self.isInputConstant.get(i):
                queryTuple.add(self.queryConstants.get(i))
            else:
                queryTuple.add(remainingTuple.get(self.queryInputIndices.get(i)))
            i += 1
        # The query is filled; we ask the map
        answer = self.function_.get(queryTuple)
        for internalFunction in internalFunctions:
            if internalFunction.getValue(remainingTuple) != answer:
                return None
        return answer

