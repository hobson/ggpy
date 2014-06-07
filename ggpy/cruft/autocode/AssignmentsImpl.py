#!/usr/bin/env python
""" generated source for module AssignmentsImpl """
# 
#  *
#  
# package: org.ggp.base.util.gdl.model.assignments
import java.util.ArrayList

import java.util.Collection

import java.util.Collections

import java.util.HashMap

import java.util.HashSet

import java.util.Iterator

import java.util.List

import java.util.Map

import java.util.PriorityQueue

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SimpleSentenceForm

import org.ggp.base.util.gdl.transforms.CommonTransforms

import org.ggp.base.util.gdl.transforms.ConstantChecker

import com.google.common.collect.ImmutableList

import com.google.common.collect.Lists

class AssignmentsImpl(Assignments):
    """ generated source for class AssignmentsImpl """
    empty = bool()
    allDone = False

    # Contains all the assignments of variables we could make
    headAssignment = Map()
    varsToAssign = List()
    valuesToIterate = List()
    valuesToCompute = List()
    indicesToChangeWhenNull = List()

    # See note below
    distincts = List()
    varsToChangePerDistinct = List()

    # indexing same as distincts
    # 
    # 	 * What does indicesToChangeWhenNull do? Well, sometimes after incrementing
    # 	 * part of the iterator, we find that a function being used to define a slot
    # 	 * in the tuple has no value corresponding to its inputs (the inputs are
    # 	 * outside the function's domain). In that case, we set the value to null,
    # 	 * then leave it to the makeNextAssignmentValid() method to deal with it.
    # 	 * We want to increment something in the input, but we need to know what
    # 	 * in the input we should increment (i.e. which is the rightmost slot in
    # 	 * the function's input). This is recorded in indicesToChangeWhenNull. If
    # 	 * a slot is not defined by a function, then presumably it will not be null,
    # 	 * so its value here is unimportant. Setting its value to -1 would help
    # 	 * catch errors.
    # 	 
    tuplesBySource = List()

    # indexed by conjunct
    sourceDefiningSlot = List()

    # indexed by var slot
    varsChosenBySource = List()

    # indexed by conjunct, then slot
    putDontCheckBySource = List()

    # indexed by conjunct, then slot
    # 
    # 	 * Creates an Assignments object that generates AssignmentIterators.
    # 	 * These can be used to efficiently iterate over all possible assignments
    # 	 * for variables in a given rule.
    # 	 *
    # 	 * @param headAssignment An assignment of variables whose values should be
    # 	 * fixed. May be empty.
    # 	 * @param rule The rule whose assignments we want to iterate over.
    # 	 * @param varDomains A map containing the possible values for each variable
    # 	 * in the rule. (All such values are GdlConstants.)
    # 	 * @param functionInfoMap
    # 	 * @param completedSentenceFormValues
    # 	 
    @overloaded
    def __init__(self, headAssignment, rule, varDomains, functionInfoMap, completedSentenceFormValues):
        """ generated source for method __init__ """
        super(AssignmentsImpl, self).__init__()
        self.empty = False
        self.headAssignment = headAssignment
        # We first have to find the remaining variables in the body
        self.varsToAssign = GdlUtils.getVariables(rule)
        # Remove all the duplicates; we do, however, want to keep the ordering
        newVarsToAssign = ArrayList()
        for v in varsToAssign:
            if not newVarsToAssign.contains(v):
                newVarsToAssign.add(v)
        self.varsToAssign = newVarsToAssign
        self.varsToAssign.removeAll(headAssignment.keySet())
        # varsToAssign is set at this point
        # We see if iterating over entire tuples will give us a
        # better result, and we look for the best way of doing that.
        # Let's get the domains of the variables
        # Map<GdlVariable, Set<GdlConstant>> varDomains = model.getVarDomains(rule);
        # Since we're looking at a particular rule, we can do this one step better
        # by looking at the domain of the head, which may be more restrictive
        # and taking the intersections of the two domains where applicable
        # Map<GdlVariable, Set<GdlConstant>> headVarDomains = model.getVarDomainsInSentence(rule.getHead());
        # We can run the A* search for a good set of source conjuncts
        # at this point, then use the result to build the rest.
        completedSentenceFormSizes = HashMap()
        if completedSentenceFormValues != None:
            for form in completedSentenceFormValues.keySet():
                completedSentenceFormSizes.put(form, completedSentenceFormValues.get(form).size())
        varDomainSizes = HashMap()
        for var in varDomains.keySet():
            varDomainSizes.put(var, varDomains.get(var).size())
        bestOrdering = IterationOrderCandidate()
        bestOrdering = getBestIterationOrderCandidate(rule, varDomains, functionInfoMap, completedSentenceFormSizes, headAssignment, False)# model,
        # TODO: True here?
        # Want to replace next few things with order
        # Need a few extra things to handle the use of iteration over existing tuples
        self.varsToAssign = bestOrdering.getVariableOrdering()
        # For each of these vars, we have to find one or the other.
        # Let's start by finding all the domains, a task already done.
        self.valuesToIterate = Lists.newArrayListWithCapacity(len(self.varsToAssign))
        for var in varsToAssign:
            if varDomains.containsKey(var):
                if not varDomains.get(var).isEmpty():
                    self.valuesToIterate.add(ImmutableList.copyOf(varDomains.get(var)))
                else:
                    self.valuesToIterate.add(ImmutableList.of(GdlPool.getConstant("0")))
            else:
                self.valuesToIterate.add(ImmutableList.of(GdlPool.getConstant("0")))
        # Okay, the iteration-over-domain is done.
        # Now let's look at sourced iteration.
        self.sourceDefiningSlot = ArrayList(len(self.varsToAssign))
        i = 0
        while i < len(self.varsToAssign):
            self.sourceDefiningSlot.add(-1)
            i += 1
        # We also need to convert values into tuples
        # We should do so while constraining to any constants in the conjunct
        # Let's convert the conjuncts
        sourceConjuncts = bestOrdering.getSourceConjuncts()
        self.tuplesBySource = Lists.newArrayListWithCapacity(len(sourceConjuncts))
        # new ArrayList<List<List<GdlConstant>>>(len(sourceConjuncts));
        self.varsChosenBySource = Lists.newArrayListWithCapacity(len(sourceConjuncts))
        # new ArrayList<List<Integer>>(len(sourceConjuncts));
        self.putDontCheckBySource = Lists.newArrayListWithCapacity(len(sourceConjuncts))
        # new ArrayList<List<Boolean>>(len(sourceConjuncts));
        j = 0
        while j < len(sourceConjuncts):
            # flatten into a tuple
            # Go through the vars/constants in the tuple
            while i < len(conjunctTuple):
                if isinstance(term, (GdlConstant, )):
                    constraintSlots.add(i)
                    constraintValues.add(term)
                    # TODO: What if tuple size ends up being 0?
                    # Need to keep that in mind
                elif isinstance(term, (GdlVariable, )):
                    varsChosen.add(varIndex)
                    if self.sourceDefiningSlot.get(varIndex) == -1:
                        # We define it
                        self.sourceDefiningSlot.set(varIndex, j)
                        putDontCheck.add(True)
                    else:
                        # It's an overlap; we just check for consistency
                        putDontCheck.add(False)
                else:
                    raise RuntimeException("Function returned in tuple")
                i += 1
            self.varsChosenBySource.add(ImmutableList.copyOf(varsChosen))
            self.putDontCheckBySource.add(ImmutableList.copyOf(putDontCheck))
            # Now we put the tuples together
            # We use constraintSlots and constraintValues to check that the
            # tuples have compatible values
            for sentence in sentences:
                # Check that it doesn't conflict with our headAssignment
                if not headAssignment.isEmpty():
                    for var in headAssignment.keySet():
                        if tupleAssignment.containsKey(var) and tupleAssignment.get(var) != headAssignment.get(var):
                            continue 
                while c < len(constraintSlots):
                    if not longTuple.get(slot) == value:
                        continue 
                    c += 1
                while s < len(longTuple):
                    # constraintSlots is sorted in ascending order
                    if c < len(constraintSlots) and constraintSlots.get(c) == s:
                        c += 1
                    else:
                        shortTuple.add(longTuple.get(s))
                    s += 1
                # The tuple fits the source conjunct
                tuples.add(ImmutableList.copyOf(shortTuple))
            # sortTuples(tuples); //Needed? Useful? Not sure. Probably not?
            self.tuplesBySource.add(ImmutableList.copyOf(tuples))
            j += 1
        # We now want to see which we can give assignment functions to
        self.valuesToCompute = ArrayList(len(self.varsToAssign))
        for var in varsToAssign:
            self.valuesToCompute.add(None)
        self.indicesToChangeWhenNull = ArrayList(len(self.varsToAssign))
        i = 0
        while i < len(self.varsToAssign):
            # Change itself, why not?
            # Actually, instead let's try -1, to catch bugs better
            self.indicesToChangeWhenNull.add(-1)
            i += 1
        # Now we have our functions already selected by the ordering
        # bestOrdering.functionalConjunctIndices;
        # Make AssignmentFunctions out of the ordering
        functionalConjuncts = bestOrdering.getFunctionalConjuncts()
        # 		print "functionalConjuncts: " + functionalConjuncts;
        i = 0
        while i < len(functionalConjuncts):
            if functionalConjunct != None:
                # These are the only ones that could be constant functions
                if functionInfoMap != None:
                    functionInfo = functionInfoMap.get(conjForm)
                if functionInfo != None:
                    # Now we need to figure out which variables are involved
                    # and which are suitable as functional outputs.
                    # 1) Which vars are in this conjunct?
                    # 2) Of these vars, which is "rightmost"?
                    # 3) Is it only used once in the relation?
                    if Collections.frequency(varsInSentence, rightmostVar) != 1:
                        continue 
                    # Can't use it
                    # 4) Which slot is it used in in the relation?
                    # 5) Build an AssignmentFunction if appropriate.
                    #    This should be able to translate from values of
                    #    the other variables to the value of the wanted
                    #    variable.
                    # We don't guarantee that this works until we check
                    if not function_.functional():
                        continue 
                    self.valuesToCompute.set(index, function_)
                    remainingVarsInSentence.remove(rightmostVar)
                    self.indicesToChangeWhenNull.set(index, self.varsToAssign.indexOf(nextRightmostVar))
            i += 1
        # We now have the remainingVars also assigned their domains
        # We also cover the distincts here
        # Assume these are just variables and constants
        self.distincts = ArrayList()
        for literal in rule.getBody():
            if isinstance(literal, (GdlDistinct, )):
                self.distincts.add(literal)
        computeVarsToChangePerDistinct()
        # Need to add "distinct" restrictions to head assignment, too...
        checkDistinctsAgainstHead()
        # We are ready for iteration
        # 		print "headAssignment: " + headAssignment;
        # 		print "varsToAssign: " + varsToAssign;
        # 		print "valuesToCompute: " + valuesToCompute;
        # 		print "sourceDefiningSlot: " + sourceDefiningSlot;

    def getRightmostVar(self, vars):
        """ generated source for method getRightmostVar """
        rightmostVar = None
        for var in varsToAssign:
            if vars.contains(var):
                rightmostVar = var
        return rightmostVar

    @__init__.register(object)
    def __init___0(self):
        """ generated source for method __init___0 """
        super(AssignmentsImpl, self).__init__()
        # The assignment is impossible; return nothing
        self.empty = True

    @SuppressWarnings("unchecked")
    @__init__.register(object, GdlRule, Map, Map, Map)
    def __init___1(self, rule, varDomains, functionInfoMap, completedSentenceFormValues):
        """ generated source for method __init___1 """
        super(AssignmentsImpl, self).__init__()
        # SentenceModel model,
        self.__init__(Collections.EMPTY_MAP, rule, varDomains, functionInfoMap, completedSentenceFormValues)

    def checkDistinctsAgainstHead(self):
        """ generated source for method checkDistinctsAgainstHead """
        for distinct in distincts:
            if term1 == term2:
                # This fails
                self.empty = True
                self.allDone = True

    def iterator(self):
        """ generated source for method iterator """
        return AssignmentIteratorImpl(getPlan())

    def getIterator(self):
        """ generated source for method getIterator """
        return AssignmentIteratorImpl(getPlan())

    def getPlan(self):
        """ generated source for method getPlan """
        return AssignmentIterationPlan.create(self.varsToAssign, self.tuplesBySource, self.headAssignment, self.indicesToChangeWhenNull, self.distincts, self.varsToChangePerDistinct, self.valuesToCompute, self.sourceDefiningSlot, self.valuesToIterate, self.varsChosenBySource, self.putDontCheckBySource, self.empty, self.allDone)

    def computeVarsToChangePerDistinct(self):
        """ generated source for method computeVarsToChangePerDistinct """
        # remember that iterators must be set up first
        self.varsToChangePerDistinct = ArrayList(len(self.varsToAssign))
        for distinct in distincts:
            # For two vars, we want to record the later of the two
            # For one var, we want to record the one
            # For no vars, we just put null
            if isinstance(, (GdlVariable, )):
                varsInDistinct.add(distinct.getArg1())
            if isinstance(, (GdlVariable, )):
                varsInDistinct.add(distinct.getArg2())
            if len(varsInDistinct) == 1:
                varToChange = varsInDistinct.get(0)
            elif len(varsInDistinct) == 2:
                varToChange = self.getRightmostVar(varsInDistinct)
            self.varsToChangePerDistinct.add(varToChange)

    @classmethod
    def getAssignmentsProducingSentence(cls, rule, sentence, varDomains, functionInfoMap, completedSentenceFormValues):
        """ generated source for method getAssignmentsProducingSentence """
        # SentenceModel model,
        # First, we see which variables must be set according to the rule head
        # (and see if there's any contradiction)
        headAssignment = HashMap()
        if not setVariablesInHead(rule.getHead(), sentence, headAssignment):
            return AssignmentsImpl()
            # Collections.emptySet();
        # Then we come up with all the assignments of the rest of the variables
        # We need to look for functions we can make use of
        return AssignmentsImpl(headAssignment, rule, varDomains, functionInfoMap, completedSentenceFormValues)

    # returns true if all variables were set successfully
    @classmethod
    @overloaded
    def setVariablesInHead(cls, head, sentence, assignment):
        """ generated source for method setVariablesInHead """
        if isinstance(head, (GdlProposition, )):
            return True
        return cls.setVariablesInHead(head.getBody(), sentence.getBody(), assignment)

    @classmethod
    @setVariablesInHead.register(object, List, List, Map)
    def setVariablesInHead_0(cls, head, sentence, assignment):
        """ generated source for method setVariablesInHead_0 """
        i = 0
        while i < len(head):
            if isinstance(headTerm, (GdlConstant, )):
                if not refTerm == headTerm:
                    # The rule can't produce this sentence
                    return False
            elif isinstance(headTerm, (GdlVariable, )):
                if curValue != None and not curValue == refTerm:
                    # inconsistent assignment (e.g. head is (rel ?x ?x), sentence is (rel 1 2))
                    return False
                assignment.put(var, refTerm)
            elif isinstance(headTerm, (GdlFunction, )):
                # Recurse on the body
                if not cls.setVariablesInHead(headFunction.getBody(), refFunction.getBody(), assignment):
                    return False
            i += 1
        return True

    # 
    # 	 * Finds the iteration order (including variables, functions, and
    # 	 * source conjuncts) that is expected to result in the fastest iteration.
    # 	 *
    # 	 * The value that is compared for each ordering is the product of:
    # 	 * - For each source conjunct, the number of tuples offered by the conjunct;
    # 	 * - For each variable not defined by a function, the size of its domain.
    # 	 *
    # 	 * @param functionInfoMap
    # 	 * @param completedSentenceFormSizes For each sentence form, this may optionally
    # 	 * contain the number of possible sentences of this form. This is useful if the
    # 	 * number of sentences is much lower than the product of its variables' domain
    # 	 * sizes; however, if this contains sentence forms where the set of sentences
    # 	 * is unknown, then it may return an ordering that is unusable.
    # 	 
    @classmethod
    def getBestIterationOrderCandidate(cls, rule, varDomains, functionInfoMap, completedSentenceFormSizes, preassignment, analyticFunctionOrdering):
        """ generated source for method getBestIterationOrderCandidate """
        # SentenceModel model,
        # Here are the things we need to pass into the first IOC constructor
        sourceConjunctCandidates = ArrayList()
        # What is a source conjunct candidate?
        # - It is a positive conjunct in the rule (i.e. a GdlSentence in the body).
        # - It has already been fully defined; i.e. it is not recursively defined in terms of the current form.
        # Furthermore, we know the number of potentially true tuples in it.
        varsToAssign = GdlUtils.getVariables(rule)
        newVarsToAssign = ArrayList()
        for var in varsToAssign:
            if not newVarsToAssign.contains(var):
                newVarsToAssign.add(var)
        varsToAssign = newVarsToAssign
        if preassignment != None:
            varsToAssign.removeAll(preassignment.keySet())
        # Calculate var domain sizes
        varDomainSizes = getVarDomainSizes(varDomains)# rule, model
        sourceConjunctSizes = ArrayList()
        for conjunct in rule.getBody():
            if isinstance(conjunct, (GdlRelation, )):
                if completedSentenceFormSizes != None and completedSentenceFormSizes.containsKey(form):
                    # New: Don't add if it will be useless as a source
                    # For now, we take a strict definition of that
                    # Compare its size with the product of the domains
                    # of the variables it defines
                    # In the future, we could require a certain ratio
                    # to decide that this is worthwhile
                    for var in vars:
                        maxSize *= domainSize
                    if size >= maxSize:
                        continue 
                    sourceConjunctCandidates.add(relation)
                    sourceConjunctSizes.add(size)
        functionalSentences = ArrayList()
        functionalSentencesInfo = ArrayList()
        for conjunct in rule.getBody():
            if isinstance(conjunct, (GdlSentence, )):
                if functionInfoMap != None and functionInfoMap.containsKey(form):
                    functionalSentences.add(conjunct)
                    functionalSentencesInfo.add(functionInfoMap.get(form))
        # TODO: If we have a head assignment, treat everything as already replaced
        # Maybe just translate the rule? Or should we keep the pool clean?
        emptyCandidate = IterationOrderCandidate(varsToAssign, sourceConjunctCandidates, sourceConjunctSizes, functionalSentences, functionalSentencesInfo, varDomainSizes)
        searchQueue = PriorityQueue()
        searchQueue.add(emptyCandidate)
        while not searchQueue.isEmpty():
            # 			print "Node being checked out: " + curNode;
            if curNode.isComplete():
                # This is the complete ordering with the lowest heuristic value
                return curNode
            searchQueue.addAll(curNode.getChildren(analyticFunctionOrdering))
        raise RuntimeException("Found no complete iteration orderings")

    @classmethod
    def getVarDomainSizes(cls, varDomains):
        """ generated source for method getVarDomainSizes """
        # GdlRule rule,
        # 			SentenceModel model
        varDomainSizes = HashMap()
        # Map<GdlVariable, Set<GdlConstant>> varDomains = model.getVarDomains(rule);
        for var in varDomains.keySet():
            varDomainSizes.put(var, varDomains.get(var).size())
        return varDomainSizes

    @classmethod
    def getNumAssignmentsEstimate(cls, rule, varDomains, checker):
        """ generated source for method getNumAssignmentsEstimate """
        # First we need the best iteration order
        # Arguments we'll need to pass in:
        # - A SentenceModel
        # - constant forms
        # - completed sentence form sizes
        # - Variable domain sizes?
        functionInfoMap = HashMap()
        for form in checker.getConstantSentenceForms():
            functionInfoMap.put(form, FunctionInfoImpl.create(form, checker))
        # Populate variable domain sizes using the constant checker
        domainSizes = HashMap()
        for form in checker.getConstantSentenceForms():
            domainSizes.put(form, checker.getTrueSentences(form).size())
        # TODO: Propagate these domain sizes as estimates for other rules?
        # Look for literals in the body of the rule and their ancestors?
        # Could we possibly do this elsewhere?
        ordering = cls.getBestIterationOrderCandidate(rule, varDomains, functionInfoMap, None, None, True)# model,
        return ordering.getHeuristicValue()

