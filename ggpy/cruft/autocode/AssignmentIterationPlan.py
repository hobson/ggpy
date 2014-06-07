#!/usr/bin/env python
""" generated source for module AssignmentIterationPlan """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.List

import java.util.Map

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlVariable

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableMap

class AssignmentIterationPlan(object):
    """ generated source for class AssignmentIterationPlan """
    # TODO: Come up with better representations
    varsToAssign = ImmutableList()
    tuplesBySource = ImmutableList()
    headAssignment = ImmutableMap()
    indicesToChangeWhenNull = ImmutableList()
    distincts = ImmutableList()
    varsToChangePerDistinct = ImmutableMap()
    valuesToCompute = ImmutableMap()
    sourceDefiningSlot = ImmutableList()
    valuesToIterate = ImmutableList()
    varsChosenBySource = ImmutableList()
    putDontCheckBySource = ImmutableList()
    empty = bool()
    allDone = bool()

    def __init__(self, varsToAssign, tuplesBySource, headAssignment, indicesToChangeWhenNull, distincts, varsToChangePerDistinct, valuesToCompute, sourceDefiningSlot, valuesToIterate, varsChosenBySource, putDontCheckBySource, empty, allDone):
        """ generated source for method __init__ """
        self.varsToAssign = varsToAssign
        self.tuplesBySource = tuplesBySource
        self.headAssignment = headAssignment
        self.indicesToChangeWhenNull = indicesToChangeWhenNull
        self.distincts = distincts
        self.varsToChangePerDistinct = varsToChangePerDistinct
        self.valuesToCompute = valuesToCompute
        self.sourceDefiningSlot = sourceDefiningSlot
        self.valuesToIterate = valuesToIterate
        self.varsChosenBySource = varsChosenBySource
        self.putDontCheckBySource = putDontCheckBySource
        self.empty = empty
        self.allDone = allDone

    def getVarsToAssign(self):
        """ generated source for method getVarsToAssign """
        return self.varsToAssign

    def getTuplesBySource(self):
        """ generated source for method getTuplesBySource """
        return self.tuplesBySource

    def getHeadAssignment(self):
        """ generated source for method getHeadAssignment """
        return self.headAssignment

    def getIndicesToChangeWhenNull(self):
        """ generated source for method getIndicesToChangeWhenNull """
        return self.indicesToChangeWhenNull

    def getDistincts(self):
        """ generated source for method getDistincts """
        return self.distincts

    def getVarsToChangePerDistinct(self):
        """ generated source for method getVarsToChangePerDistinct """
        return self.varsToChangePerDistinct

    def getValuesToCompute(self):
        """ generated source for method getValuesToCompute """
        return self.valuesToCompute

    def getSourceDefiningSlot(self):
        """ generated source for method getSourceDefiningSlot """
        return self.sourceDefiningSlot

    def getValuesToIterate(self):
        """ generated source for method getValuesToIterate """
        return self.valuesToIterate

    def getVarsChosenBySource(self):
        """ generated source for method getVarsChosenBySource """
        return self.varsChosenBySource

    def getPutDontCheckBySource(self):
        """ generated source for method getPutDontCheckBySource """
        return self.putDontCheckBySource

    def getEmpty(self):
        """ generated source for method getEmpty """
        return self.empty

    def getAllDone(self):
        """ generated source for method getAllDone """
        return self.allDone

    EMPTY_ITERATION_PLAN = AssignmentIterationPlan(None, None, None, None, None, None, None, None, None, None, None, True, False)

    @classmethod
    def create(cls, varsToAssign, tuplesBySource, headAssignment, indicesToChangeWhenNull, distincts, varsToChangePerDistinct, valuesToCompute, sourceDefiningSlot, valuesToIterate, varsChosenBySource, putDontCheckBySource, empty, allDone):
        """ generated source for method create """
        if empty:
            return cls.EMPTY_ITERATION_PLAN
        return AssignmentIterationPlan(ImmutableList.copyOf(varsToAssign), ImmutableList.copyOf(tuplesBySource), ImmutableMap.copyOf(headAssignment), ImmutableList.copyOf(indicesToChangeWhenNull), ImmutableList.copyOf(distincts), fromNullableList(varsToChangePerDistinct), fromNullableList(valuesToCompute), ImmutableList.copyOf(sourceDefiningSlot), ImmutableList.copyOf(valuesToIterate), ImmutableList.copyOf(varsChosenBySource), ImmutableList.copyOf(putDontCheckBySource), empty, allDone)

    @classmethod
    def fromNullableList(cls, nullableList):
        """ generated source for method fromNullableList """
        builder = ImmutableMap.builder()
        i = 0
        while i < len(nullableList):
            if nullableList.get(i) != None:
                builder.put(i, nullableList.get(i))
            i += 1
        return builder.build()

