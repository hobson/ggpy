#!/usr/bin/env python
""" generated source for module AssignmentIteratorImpl """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.ArrayList

import java.util.Collection

import java.util.Collections

import java.util.HashMap

import java.util.List

import java.util.Map

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import com.google.common.collect.ImmutableList

#  Not thread-safe
class AssignmentIteratorImpl(AssignmentIterator):
    """ generated source for class AssignmentIteratorImpl """
    sourceTupleIndices = None

    # This time we just have integers to deal with
    valueIndices = None
    nextAssignment = ArrayList()
    assignmentMap = HashMap()
    headOnly = False
    done = False
    plan = AssignmentIterationPlan()

    def __init__(self, plan):
        """ generated source for method __init__ """
        super(AssignmentIteratorImpl, self).__init__()
        self.plan = plan
        # TODO: Handle this case with a separate class
        if plan.getVarsToAssign() == None:
            self.headOnly = True
            return
        # Set up source tuple...
        self.sourceTupleIndices = ArrayList(plan.getTuplesBySource().size())
        i = 0
        while i < plan.getTuplesBySource().size():
            self.sourceTupleIndices.add(0)
            i += 1
        # Set up...
        self.valueIndices = ArrayList(plan.getVarsToAssign().size())
        i = 0
        while i < plan.getVarsToAssign().size():
            self.valueIndices.add(0)
            self.nextAssignment.add(None)
            i += 1
        self.assignmentMap.putAll(plan.getHeadAssignment())
        # Update "nextAssignment" according to the values of the
        # value indices
        updateNextAssignment()
        # Keep updating it until something really works
        makeNextAssignmentValid()

    def makeNextAssignmentValid(self):
        """ generated source for method makeNextAssignmentValid """
        if self.nextAssignment == None:
            return
        # Something new that can pop up with functional constants...
        i = 0
        while i < len(self.nextAssignment):
            if self.nextAssignment.get(i) == None:
                # Some function doesn't agree with the answer here
                # So what do we increment?
                incrementIndex(self.plan.getIndicesToChangeWhenNull().get(i))
                if self.nextAssignment == None:
                    return
                i = -1
            i += 1
        # Find all the unsatisfied distincts
        # Find the pair with the earliest var. that needs to be changed
        varsToChange = ArrayList()
        d = 0
        while d < self.plan.getDistincts().size():
            # The assignments must use the assignments implied by nextAssignment
            if term1 == term2:
                # need to change one of these
                varsToChange.add(self.plan.getVarsToChangePerDistinct().get(d))
            d += 1
        if not varsToChange.isEmpty():
            # We want just the one, as it is a full restriction on its
            # own behalf
            changeOneInNext(Collections.singleton(varToChange))

    def getLeftmostVar(self, vars):
        """ generated source for method getLeftmostVar """
        for var in plan.getVarsToAssign():
            if vars.contains(var):
                return var
        return None

    def replaceVariables(self, term):
        """ generated source for method replaceVariables """
        if isinstance(term, (GdlFunction, )):
            raise RuntimeException("Function in the distinct... not handled")
        # Use the assignments implied by nextAssignment
        if self.plan.getHeadAssignment().containsKey(term):
            return self.plan.getHeadAssignment().get(term)
        # Translated in head assignment
        if isinstance(term, (GdlConstant, )):
            return term
        index = self.plan.getVarsToAssign().indexOf(term)
        return self.nextAssignment.get(index)

    def incrementIndex(self, index):
        """ generated source for method incrementIndex """
        if index < 0:
            # Trash the iterator
            self.nextAssignment = None
            return
        if self.plan.getValuesToCompute() != None and self.plan.getValuesToCompute().containsKey(index):
            # The constant at this index is functionally computed
            self.incrementIndex(index - 1)
            return
        if self.plan.getSourceDefiningSlot().get(index) != -1:
            # This is set by a source; increment the source
            incrementSource(self.plan.getSourceDefiningSlot().get(index))
            return
        # We try increasing the var at index by 1.
        # Everything to the right of it gets reset.
        # If it can't be increased, increase the number
        # to the left instead. If nothing can be
        # increased, trash the iterator.
        curValue = self.valueIndices.get(index)
        if curValue == self.plan.getValuesToIterate().get(index).size() - 1:
            self.incrementIndex(index - 1)
            return
        self.valueIndices.set(index, curValue + 1)
        i = index + 1
        while i < len(self.valueIndices):
            pass
            i += 1
        updateNextAssignment()

    def incrementSource(self, source):
        """ generated source for method incrementSource """
        if source < 0:
            self.nextAssignment = None
            return
        curValue = self.sourceTupleIndices.get(source)
        if curValue == self.plan.getTuplesBySource().get(source).size() - 1:
            self.incrementSource(source - 1)
            return
        self.sourceTupleIndices.set(source, curValue + 1)
        i = source + 1
        while i < len(self.sourceTupleIndices):
            pass
            i += 1
        i = 0
        while i < len(self.valueIndices):
            pass
            i += 1
        updateNextAssignment()

    def updateNextAssignment(self):
        """ generated source for method updateNextAssignment """
        s = 0
        while s < len(self.sourceTupleIndices):
            if len(tuples) == 0:
                self.nextAssignment = None
                return
            while i < len(tuple_):
                if putDontCheck:
                    self.nextAssignment.set(varSlotChosen, value)
                else:
                    if not self.nextAssignment.get(varSlotChosen) == value:
                        self.incrementSource(s)
                        return
                i += 1
            s += 1
        i = 0
        while i < len(self.valueIndices):
            if (self.plan.getValuesToCompute() == None or not self.plan.getValuesToCompute().containsKey(i)) and self.plan.getSourceDefiningSlot().get(i) == -1:
                self.nextAssignment.set(i, self.plan.getValuesToIterate().get(i).get(self.valueIndices.get(i)))
            elif self.plan.getSourceDefiningSlot().get(i) == -1:
                self.nextAssignment.set(i, valueFromFunction)
            i += 1

    @overloaded
    def changeOneInNext(self, vars):
        """ generated source for method changeOneInNext """
        if self.nextAssignment == None:
            return
        if vars.isEmpty():
            if self.headOnly:
                self.done = True
                return
            else:
                self.done = True
                return
        if self.plan.getVarsToAssign() == None:
            print "headOnly: " + self.headOnly
        rightmostVar = getRightmostVar(vars)
        self.incrementIndex(self.plan.getVarsToAssign().indexOf(rightmostVar))
        self.makeNextAssignmentValid()

    @changeOneInNext.register(object, Collection, Map)
    def changeOneInNext_0(self, varsToChange, assignment):
        """ generated source for method changeOneInNext_0 """
        if self.nextAssignment == None:
            return
        for varToChange in varsToChange:
            if index != -1:
                if assignedValue == None:
                    raise IllegalArgumentException("assignedValue is null; " + "varToChange is " + varToChange + " and assignment is " + assignment)
                if self.nextAssignment == None:
                    raise IllegalStateException("nextAssignment is null")
                if not assignedValue == self.nextAssignment.get(index):
                    return
        self.changeOneInNext(varsToChange)

    def hasNext(self):
        """ generated source for method hasNext """
        if self.plan.getEmpty():
            return False
        if self.headOnly:
            return (not self.plan.getAllDone() and not self.done)
        return (self.nextAssignment != None)

    def next(self):
        """ generated source for method next """
        if self.headOnly:
            if self.plan.getAllDone() or self.done:
                raise RuntimeException("Asking for next when all done")
            self.done = True
            return self.plan.getHeadAssignment()
        updateMap()
        self.incrementIndex(len(self.valueIndices) - 1)
        self.makeNextAssignmentValid()
        return self.assignmentMap

    def updateMap(self):
        """ generated source for method updateMap """
        i = 0
        while i < self.plan.getVarsToAssign().size():
            self.assignmentMap.put(self.plan.getVarsToAssign().get(i), self.nextAssignment.get(i))
            i += 1

    def getRightmostVar(self, vars):
        """ generated source for method getRightmostVar """
        rightmostVar = None
        for var in plan.getVarsToAssign():
            if vars.contains(var):
                rightmostVar = var
        return rightmostVar

    def remove(self):
        """ generated source for method remove """

