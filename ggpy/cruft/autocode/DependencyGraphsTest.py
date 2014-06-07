#!/usr/bin/env python
""" generated source for module DependencyGraphsTest """
# package: org.ggp.base.util.gdl.model
import java.util.Set

import org.junit.Test

import com.google.common.collect.HashMultimap

import com.google.common.collect.Multimap

import com.google.common.collect.Sets

class DependencyGraphsTest(object):
    """ generated source for class DependencyGraphsTest """
    def testSafeToposort(self):
        """ generated source for method testSafeToposort """
        allElements = Sets.newHashSet(1, 2, 3, 4, 5, 6, 7, 8)
        graph = HashMultimap.create()
        graph.put(2, 1)
        graph.put(3, 2)
        graph.put(4, 2)
        graph.put(5, 3)
        graph.put(5, 4)
        graph.put(3, 4)
        graph.put(4, 3)
        graph.put(4, 6)
        graph.put(6, 7)
        graph.put(7, 8)
        graph.put(8, 3)
        print DependencyGraphs.toposortSafe(allElements, graph)

