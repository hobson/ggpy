#!/usr/bin/env python
""" generated source for module IterationOrderCandidate """
# package: org.ggp.base.util.gdl.model.assignments
import java.util.ArrayList

import java.util.Collections

import java.util.HashMap

import java.util.HashSet

import java.util.List

import java.util.Map

import java.util.Map.Entry

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

# This class has a natural ordering that is inconsistent with equals.
class IterationOrderCandidate(Comparable, IterationOrderCandidate):
    """ generated source for class IterationOrderCandidate """
    # Information specific to this ordering
    sourceConjunctIndices = List()

    # Which conjuncts are we using as sources, and in what order?
    varOrdering = List()

    # In what order do we assign variables?
    functionalConjunctIndices = List()

    # Same size as varOrdering
    # Index of conjunct if functional, -1 otherwise
    varSources = List()

    # Same size as varOrdering
    # For each variable: Which source conjunct
    # originally contributes it? -1 if none
    # Becomes sourceResponsibleForVar
    # Information shared by the orderings
    # Presumably, this will also be used to construct the iterator to be used...
    varsToAssign = List()
    sourceConjunctCandidates = List()
    sourceConjunctSizes = List()

    # same indexing as candidates
    functionalSentences = List()
    functionalSentencesInfo = List()

    # Indexing same as functionalSentences
    varDomainSizes = Map()

    # 
    # 		 * This constructor is for creating the start node of the
    # 		 * search. No part of the ordering is specified.
    # 		 *
    # 		 * @param sourceConjunctCandidates
    # 		 * @param sourceConjunctSizes
    # 		 * @param functionalSentences
    # 		 * @param functionalSentencesInfo
    # 		 * @param allVars
    # 		 * @param varDomainSizes
    # 		 
    @overloaded
    def __init__(self, varsToAssign, sourceConjunctCandidates, sourceConjunctSizes, functionalSentences, functionalSentencesInfo, varDomainSizes):
        """ generated source for method __init__ """
        super(IterationOrderCandidate, self).__init__()
        self.sourceConjunctIndices = ArrayList()
        self.varOrdering = ArrayList()
        self.functionalConjunctIndices = ArrayList()
        self.varSources = ArrayList()
        self.varsToAssign = varsToAssign
        self.sourceConjunctCandidates = sourceConjunctCandidates
        self.sourceConjunctSizes = sourceConjunctSizes
        self.functionalSentences = functionalSentences
        self.functionalSentencesInfo = functionalSentencesInfo
        self.varDomainSizes = varDomainSizes

    def getFunctionalConjuncts(self):
        """ generated source for method getFunctionalConjuncts """
        # Returns, for each var, the conjunct defining it (if any)
        functionalConjuncts = ArrayList(len(self.functionalConjunctIndices))
        for index in functionalConjunctIndices:
            if index == -1:
                functionalConjuncts.add(None)
            else:
                functionalConjuncts.add(self.functionalSentences.get(index))
        return functionalConjuncts

    def getSourceConjuncts(self):
        """ generated source for method getSourceConjuncts """
        # These are the selected source conjuncts, not just the candidates.
        sourceConjuncts = ArrayList(len(self.sourceConjunctIndices))
        for index in sourceConjunctIndices:
            sourceConjuncts.add(self.sourceConjunctCandidates.get(index))
        return sourceConjuncts

    def getVariableOrdering(self):
        """ generated source for method getVariableOrdering """
        return self.varOrdering

    # 
    # 		 * This constructor is for "completing" the ordering by
    # 		 * adding all remaining variables, in some arbitrary order.
    # 		 * No source conjuncts or functions are added.
    # 		 
    @__init__.register(object, IterationOrderCandidate)
    def __init___0(self, parent):
        """ generated source for method __init___0 """
        super(IterationOrderCandidate, self).__init__()
        # Shared rules
        self.varsToAssign = parent.varsToAssign
        self.sourceConjunctCandidates = parent.sourceConjunctCandidates
        self.sourceConjunctSizes = parent.sourceConjunctSizes
        self.functionalSentences = parent.functionalSentences
        self.functionalSentencesInfo = parent.functionalSentencesInfo
        self.varDomainSizes = parent.varDomainSizes
        # Individual rules:
        # We can share this because we won't be adding to it
        self.sourceConjunctIndices = parent.sourceConjunctIndices
        # These others we'll be adding to
        self.varOrdering = ArrayList(parent.varOrdering)
        self.functionalConjunctIndices = ArrayList(parent.functionalConjunctIndices)
        self.varSources = ArrayList(parent.varSources)
        # Fill out the ordering with all remaining variables: Easy enough
        for var in varsToAssign:
            if not self.varOrdering.contains(var):
                self.varOrdering.add(var)
                self.functionalConjunctIndices.add(-1)
                self.varSources.add(-1)

    # 
    # 		 * This constructor is for adding a source conjunct to an
    # 		 * ordering.
    # 		 * @param i The index of the source conjunct being added.
    # 		 
    @__init__.register(object, IterationOrderCandidate, int)
    def __init___1(self, parent, i):
        """ generated source for method __init___1 """
        super(IterationOrderCandidate, self).__init__()
        # Shared rules:
        self.varsToAssign = parent.varsToAssign
        self.sourceConjunctCandidates = parent.sourceConjunctCandidates
        self.sourceConjunctSizes = parent.sourceConjunctSizes
        self.functionalSentences = parent.functionalSentences
        self.functionalSentencesInfo = parent.functionalSentencesInfo
        self.varDomainSizes = parent.varDomainSizes
        # Individual rules:
        self.sourceConjunctIndices = ArrayList(parent.sourceConjunctIndices)
        self.varOrdering = ArrayList(parent.varOrdering)
        self.functionalConjunctIndices = ArrayList(parent.functionalConjunctIndices)
        self.varSources = ArrayList(parent.varSources)
        # Add the new source conjunct
        self.sourceConjunctIndices.add(i)
        sourceConjunctCandidate = self.sourceConjunctCandidates.get(i)
        varsFromConjunct = GdlUtils.getVariables(sourceConjunctCandidate)
        # Ignore both previously added vars and duplicates
        # Oh, but we need to be careful here, at some point.
        # i.e., what if there are multiple of the same variable
        # in a single statement?
        # That should probably be handled later.
        for var in varsFromConjunct:
            if not self.varOrdering.contains(var):
                self.varOrdering.add(var)
                self.varSources.add(i)
                self.functionalConjunctIndices.add(-1)

    # 
    # 		 * This constructor is for adding a function to the ordering.
    # 		 
    @__init__.register(object, IterationOrderCandidate, GdlSentence, int, GdlVariable)
    def __init___2(self, parent, functionalSentence, functionalSentenceIndex, functionOutput):
        """ generated source for method __init___2 """
        super(IterationOrderCandidate, self).__init__()
        # Shared rules:
        self.varsToAssign = parent.varsToAssign
        self.sourceConjunctCandidates = parent.sourceConjunctCandidates
        self.sourceConjunctSizes = parent.sourceConjunctSizes
        self.functionalSentences = parent.functionalSentences
        self.functionalSentencesInfo = parent.functionalSentencesInfo
        self.varDomainSizes = parent.varDomainSizes
        # Individual rules:
        self.sourceConjunctIndices = ArrayList(parent.sourceConjunctIndices)
        self.varOrdering = ArrayList(parent.varOrdering)
        self.functionalConjunctIndices = ArrayList(parent.functionalConjunctIndices)
        self.varSources = ArrayList(parent.varSources)
        # And we add the function
        varsInFunction = GdlUtils.getVariables(functionalSentence)
        # First, add the remaining arguments
        for var in varsInFunction:
            if not self.varOrdering.contains(var) and not var == functionOutput and self.varsToAssign.contains(var):
                self.varOrdering.add(var)
                self.functionalConjunctIndices.add(-1)
                self.varSources.add(-1)
        # Then the output
        self.varOrdering.add(functionOutput)
        self.functionalConjunctIndices.add(functionalSentenceIndex)
        self.varSources.add(-1)

    def getHeuristicValue(self):
        """ generated source for method getHeuristicValue """
        heuristic = 1
        for sourceIndex in sourceConjunctIndices:
            heuristic *= self.sourceConjunctSizes.get(sourceIndex)
        v = 0
        while v < len(self.varOrdering):
            if self.varSources.get(v) == -1 and self.functionalConjunctIndices.get(v) == -1:
                # It's not set by a source conjunct or a function
                heuristic *= self.varDomainSizes.get(self.varOrdering.get(v))
            v += 1
        # We want complete orderings to show up faster
        # so we add a little incentive to pick them
        # Add 1 to the value of non-complete orderings
        if len(self.varOrdering) < len(self.varsToAssign):
            heuristic += 1
        # 			print "Heuristic value is " + heuristic + " with functionalConjunctIndices " + functionalConjunctIndices;
        return heuristic

    def isComplete(self):
        """ generated source for method isComplete """
        return self.varOrdering.containsAll(self.varsToAssign)

    def getChildren(self, analyticFunctionOrdering):
        """ generated source for method getChildren """
        allChildren = ArrayList()
        allChildren.addAll(getSourceConjunctChildren())
        allChildren.addAll(getFunctionAddedChildren(analyticFunctionOrdering))
        # 			print "Number of children being added: " + len(allChildren);
        return allChildren

    def getSourceConjunctChildren(self):
        """ generated source for method getSourceConjunctChildren """
        children = ArrayList()
        # If we are already using functions, short-circuit to cut off
        # repetition of the search space
        for index in functionalConjunctIndices:
            if index != -1:
                return Collections.emptyList()
        # This means we want a reference to the original list of conjuncts.
        lastSourceConjunctIndex = -1
        if not self.sourceConjunctIndices.isEmpty():
            lastSourceConjunctIndex = self.sourceConjunctIndices.get(len(self.sourceConjunctIndices) - 1)
        i = lastSourceConjunctIndex + 1
        while i < len(self.sourceConjunctCandidates):
            children.add(IterationOrderCandidate(self, i))
            i += 1
        return children

    def getFunctionAddedChildren(self, analyticFunctionOrdering):
        """ generated source for method getFunctionAddedChildren """
        # We can't just add those functions that
        # are "ready" to be added. We should be adding all those variables
        # "leading up to" the functions and then applying the functions.
        # We can even take this one step further by only adding one child
        # per remaining constant function; we choose as our function output the
        # variable that is a candidate for functionhood that has the
        # largest domain, or one that is tied for largest.
        # New criterion: Must also NOT be in preassignment.
        children = ArrayList()
        # It would be really nice here to just analytically choose
        # the set of functions we're going to use.
        # Here's one approach for doing that:
        # For each variable, get a list of the functions that could
        # potentially produce it.
        # For all the variables with no functions, add them.
        # Then repeatedly find the function with the fewest
        # number of additional variables (hopefully 0!) needed to
        # specify it and add it as a function.
        # The goal here is not to be optimal, but to be efficient!
        # Certain games (e.g. Pentago) break the old complete search method!
        # TODO: Eventual possible optimization here:
        # If something is dependent on a connected component that it is
        # not part of, wait until the connected component is resolved
        # (or something like that...)
        if analyticFunctionOrdering and len(self.functionalSentencesInfo) > 8:
            # For each variable, a list of functions
            # (refer to functions by their indices)
            # and the set of outstanding vars they depend on...
            # We start by adding to the varOrdering the vars not produced by functions
            # First, we have to find them
            while i < len(self.functionalSentencesInfo):
                for producibleVar in producibleVars:
                    if not functionsProducingVars.containsKey(producibleVar):
                        functionsProducingVars.put(producibleVar, HashSet())
                    functionsProducingVars.get(producibleVar).add(i)
                i += 1
            # Non-producible vars get iterated over before we start
            # deciding which functions to add
            for var in varsToAssign:
                if not self.varOrdering.contains(var):
                    if not functionsProducingVars.containsKey(var):
                        # Add var to the ordering
                        self.varOrdering.add(var)
                        self.functionalConjunctIndices.add(-1)
                        self.varSources.add(-1)
            # Map is from potential set of dependencies to function indices
            # Create this map...
            while i < len(self.functionalSentencesInfo):
                # Variables already in varOrdering don't go in dependents list
                producibleVars.removeAll(self.varOrdering)
                allVars.removeAll(self.varOrdering)
                for producibleVar in producibleVars:
                    dependencies.addAll(allVars)
                    dependencies.remove(producibleVar)
                    if not functionsHavingDependencies.containsKey(dependencies):
                        functionsHavingDependencies.put(dependencies, HashSet())
                    functionsHavingDependencies.get(dependencies).add(i)
                i += 1
            # Now, we can keep creating functions to generate the remaining variables
            while len(self.varOrdering) < len(self.varsToAssign):
                if functionsHavingDependencies.isEmpty():
                    raise RuntimeException("We should not run out of functions we could use")
                # Find the smallest set of dependencies
                if functionsHavingDependencies.containsKey(Collections.emptySet()):
                    dependencySetToUse = Collections.emptySet()
                else:
                    for dependencySet in functionsHavingDependencies.keySet():
                        if len(dependencySet) < smallestSize:
                            smallestSize = len(dependencySet)
                            dependencySetToUse = dependencySet
                # See if any of the functions are applicable
                for function_ in functions:
                    producibleVars.removeAll(dependencySetToUse)
                    producibleVars.removeAll(self.varOrdering)
                    if not producibleVars.isEmpty():
                        functionToUse = function_
                        varProduced = producibleVars.iterator().next()
                        break
                if functionToUse == -1:
                    # None of these functions were actually useful now?
                    # Dump the dependency set
                    functionsHavingDependencies.remove(dependencySetToUse)
                else:
                    # Apply the function
                    # 1) Add the remaining dependencies as iterated variables
                    for var in dependencySetToUse:
                        self.varOrdering.add(var)
                        self.functionalConjunctIndices.add(-1)
                        self.varSources.add(-1)
                    # 2) Add the function's produced variable (varProduced)
                    self.varOrdering.add(varProduced)
                    self.functionalConjunctIndices.add(functionToUse)
                    self.varSources.add(-1)
                    # 3) Remove all vars added this way from all dependency sets
                    addedVars.addAll(dependencySetToUse)
                    addedVars.add(varProduced)
                    # Tricky, because we have to merge sets
                    # Easier to use a new map
                    for entry in functionsHavingDependencies.entrySet():
                        newKey.removeAll(addedVars)
                        if not newFunctionsHavingDependencies.containsKey(newKey):
                            newFunctionsHavingDependencies.put(newKey, HashSet())
                        newFunctionsHavingDependencies.get(newKey).addAll(entry.getValue())
                    functionsHavingDependencies = newFunctionsHavingDependencies
                    # 4) Remove this function from the lists?
                    for functionSet in functionsHavingDependencies.values():
                        functionSet.remove(functionToUse)
            # Now we need to actually return the ordering in a list
            # Here's the quick way to do that...
            # (since we've added all the new stuff to ourself already)
            return Collections.singletonList(IterationOrderCandidate(self))
        else:
            # Let's try a new technique for restricting the space of possibilities...
            # We already have an ordering on the functions
            # Let's try to constrain things to that order
            # Namely, if i<j and constant form j is already used as a function,
            # we cannot use constant form i UNLESS constant form j supplies
            # as its variable something used by constant form i.
            # We might also try requiring that c.f. i NOT provide a variable
            # used by c.f. j, though there may be multiple possibilities as
            # to what it could provide.
            if not self.functionalConjunctIndices.isEmpty():
                lastFunctionUsedIndex = Collections.max(self.functionalConjunctIndices)
            while i < len(self.functionalConjunctIndices):
                if self.functionalConjunctIndices.get(i) != -1:
                    varsProducedByFunctions.add(self.varOrdering.get(i))
                i += 1
            while i < len(self.functionalSentencesInfo):
                if i < lastFunctionUsedIndex:
                    # We need to figure out whether i could use any of the
                    # vars we're producing with functions
                    # TODO: Try this with a finer grain
                    # i.e., see if i needs a var from a function that is after
                    # it, not one that might be before it
                    if Collections.disjoint(varsInSentence, varsProducedByFunctions):
                        continue 
                # What is the best variable to grab from this form, if there are any?
                if bestVariable == None:
                    continue 
                children.add(newCandidate)
                i += 1
            # If there are no more functions to add, add the completed version
            if children.isEmpty():
                children.add(IterationOrderCandidate(self))
            return children

    def getBestVariable(self, functionalSentence, functionInfo):
        """ generated source for method getBestVariable """
        # If all the variables that can be set by the functional sentence are in
        # the varOrdering, we return null. Otherwise, we return one of
        # those with the largest domain.
        # The FunctionInfo is sentence-independent, so we need the context
        # of the sentence (which has variables in it).
        tuple_ = GdlUtils.getTupleFromSentence(functionalSentence)
        dependentSlots = functionInfo.getDependentSlots()
        if len(tuple_) != len(dependentSlots):
            raise RuntimeException("Mismatched sentence " + functionalSentence + " and constant form " + functionInfo)
        candidateVars = HashSet()
        i = 0
        while i < len(tuple_):
            if isinstance(term, (GdlVariable, )) and dependentSlots.get(i) and not self.varOrdering.contains(term) and self.varsToAssign.contains(term):
                candidateVars.add(term)
            i += 1
        # Now we look at the domains, trying to find the largest
        bestVar = None
        bestDomainSize = 0
        for var in candidateVars:
            if domainSize > bestDomainSize:
                bestVar = var
                bestDomainSize = domainSize
        return bestVar
        # null if none are usable

    # This class has a natural ordering that is inconsistent with equals.
    def compareTo(self, o):
        """ generated source for method compareTo """
        diff = self.getHeuristicValue() - o.getHeuristicValue()
        if diff < 0:
            return -1
        elif diff == 0:
            return 0
        else:
            return 1

    def __str__(self):
        """ generated source for method toString """
        return self.varOrdering.__str__() + " with sources " + self.getSourceConjuncts().__str__() + "; functional?: " + self.functionalConjunctIndices + "; domain sizes are " + self.varDomainSizes

