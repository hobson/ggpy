#!/usr/bin/env python
""" generated source for module DependencyGraphs """
# package: org.ggp.base.util.gdl.model
import java.util.Collection

import java.util.Deque

import java.util.List

import java.util.Map.Entry

import java.util.Set

import com.google.common.base.Predicate

import com.google.common.collect.Collections2

import com.google.common.collect.HashMultimap

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Iterables

import com.google.common.collect.Lists

import com.google.common.collect.Multimap

import com.google.common.collect.Multimaps

import com.google.common.collect.Queues

import com.google.common.collect.SetMultimap

import com.google.common.collect.Sets

# 
#  * When dealing with GDL, dependency graphs are often useful. DependencyGraphs
#  * offers a variety of functionality for dealing with dependency graphs expressed
#  * in the form of SetMultimaps.
#  *
#  * These multimaps are paired with sets of all nodes, to account for the
#  * possibility of nodes not included in the multimap representation.
#  *
#  * All methods assume that keys in multimaps depend on their associated values,
#  * or in other words are downstream of or are children of those values.
#  
class DependencyGraphs(object):
    """ generated source for class DependencyGraphs """
    def __init__(self):
        """ generated source for method __init__ """

    # 
    # 	 * Returns all elements of the dependency graph that match the
    # 	 * given predicate, and any elements upstream of those matching
    # 	 * elements.
    # 	 *
    # 	 * The graph may contain cycles.
    # 	 *
    # 	 * Each key in the dependency graph depends on/is downstream of
    # 	 * its associated values.
    # 	 
    @classmethod
    def getMatchingAndUpstream(cls, allNodes, dependencyGraph, matcher):
        """ generated source for method getMatchingAndUpstream """
        results = Sets.newHashSet()
        toTry = Queues.newArrayDeque()
        toTry.addAll(Collections2.filter(allNodes, matcher))
        while not toTry.isEmpty():
            if not results.contains(curElem):
                results.add(curElem)
                toTry.addAll(dependencyGraph.get(curElem))
        return ImmutableSet.copyOf(results)

    # 
    # 	 * Returns all elements of the dependency graph that match the
    # 	 * given predicate, and any elements downstream of those matching
    # 	 * elements.
    # 	 *
    # 	 * The graph may contain cycles.
    # 	 *
    # 	 * Each key in the dependency graph depends on/is downstream of
    # 	 * its associated values.
    # 	 
    @classmethod
    def getMatchingAndDownstream(cls, allNodes, dependencyGraph, matcher):
        """ generated source for method getMatchingAndDownstream """
        return cls.getMatchingAndUpstream(allNodes, reverseGraph(dependencyGraph), matcher)

    @classmethod
    def reverseGraph(cls, graph):
        """ generated source for method reverseGraph """
        return Multimaps.invertFrom(graph, HashMultimap.create())

    # 
    # 	 * Given a dependency graph, return a topologically sorted
    # 	 * ordering of its components, stratified in a way that allows
    # 	 * for recursion and cycles. (Each set in the list is one
    # 	 * unordered "stratum" of elements. Elements may depend on elements
    # 	 * in earlier strata or the same stratum, but not in later
    # 	 * strata.)
    # 	 *
    # 	 * If there are no cycles, the result will be a list of singleton
    # 	 * sets, topologically sorted.
    # 	 *
    # 	 * Each key in the given dependency graph depends on/is downstream of
    # 	 * its associated values.
    # 	 
    @classmethod
    def toposortSafe(cls, allElements, dependencyGraph):
        """ generated source for method toposortSafe """
        strataToAdd = createAllStrata(allElements)
        strataDependencyGraph = createStrataDependencyGraph(dependencyGraph)
        ordering = Lists.newArrayList()
        while not strataToAdd.isEmpty():
            addOrMergeStratumAndAncestors(curStratum, ordering, strataToAdd, strataDependencyGraph, Lists.newArrayList())
        return ordering

    @classmethod
    def addOrMergeStratumAndAncestors(cls, curStratum, ordering, toAdd, strataDependencyGraph, downstreamStrata):
        """ generated source for method addOrMergeStratumAndAncestors """
        if downstreamStrata.contains(curStratum):
            mergeStrata(Sets.newHashSet(toMerge), toAdd, strataDependencyGraph)
            return
        downstreamStrata.add(curStratum)
        for parent in ImmutableList.copyOf(strataDependencyGraph.get(curStratum)):
            # We could merge away the parent here, so we protect against CMEs and
            # make sure the parent is still in toAdd before recursing.
            if toAdd.contains(parent):
                cls.addOrMergeStratumAndAncestors(parent, ordering, toAdd, strataDependencyGraph, downstreamStrata)
        downstreamStrata.remove(curStratum)
        #  - If we've added all our parents, we will still be in toAdd
        #    and none of our dependencies will be in toAdd. Add to the ordering.
        #  - If there was a merge upstream that we weren't involved in,
        #    we will still be in toAdd, but we will have (possibly new)
        #    dependencies that are still in toAdd. Do nothing.
        #  - If there was a merge upstream that we were involved in,
        #    we won't be in toAdd anymore. Do nothing.
        if not toAdd.contains(curStratum):
            return
        for parent in strataDependencyGraph.get(curStratum):
            if toAdd.contains(parent):
                return
        ordering.add(curStratum)
        toAdd.remove(curStratum)

    # Replace the old strata with the new stratum in toAdd and strataDependencyGraph.
    @classmethod
    def mergeStrata(cls, toMerge, toAdd, strataDependencyGraph):
        """ generated source for method mergeStrata """
        newStratum = ImmutableSet.copyOf(Iterables.concat(toMerge))
        for oldStratum in toMerge:
            toAdd.remove(oldStratum)
        toAdd.add(newStratum)
        # Change the keys
        for oldStratum in toMerge:
            strataDependencyGraph.putAll(newStratum, parents)
            strataDependencyGraph.removeAll(oldStratum)
        # Change the values
        for entry in ImmutableList.copyOf(strataDependencyGraph.entries()):
            if toMerge.contains(entry.getValue()):
                strataDependencyGraph.remove(entry.getKey(), entry.getValue())
                strataDependencyGraph.put(entry.getKey(), newStratum)

    @classmethod
    def createAllStrata(cls, allElements):
        """ generated source for method createAllStrata """
        result = Sets.newHashSet()
        for element in allElements:
            result.add(ImmutableSet.of(element))
        return result

    @classmethod
    def createStrataDependencyGraph(cls, dependencyGraph):
        """ generated source for method createStrataDependencyGraph """
        strataDependencyGraph = HashMultimap.create()
        for entry in dependencyGraph.entries():
            strataDependencyGraph.put(ImmutableSet.of(entry.getKey()), ImmutableSet.of(entry.getValue()))
        return strataDependencyGraph

