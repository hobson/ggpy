#!/usr/bin/env python
""" generated source for module OptimizingPropNetFactory """
# package: org.ggp.base.util.propnet.factory
import java.util.ArrayList

import java.util.Collection

import java.util.Collections

import java.util.HashMap

import java.util.HashSet

import java.util.LinkedList

import java.util.List

import java.util.Map

import java.util.Map.Entry

import java.util.Queue

import java.util.Set

import java.util.Stack

import org.ggp.base.util.Pair

import org.ggp.base.util.concurrency.ConcurrencyUtils

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.gdl.model.SentenceDomainModel

import org.ggp.base.util.gdl.model.SentenceDomainModelFactory

import org.ggp.base.util.gdl.model.SentenceDomainModelOptimizer

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SentenceForms

import org.ggp.base.util.gdl.model.SentenceModelUtils

import org.ggp.base.util.gdl.model.assignments.AssignmentIterator

import org.ggp.base.util.gdl.model.assignments.Assignments

import org.ggp.base.util.gdl.model.assignments.AssignmentsFactory

import org.ggp.base.util.gdl.model.assignments.FunctionInfo

import org.ggp.base.util.gdl.model.assignments.FunctionInfoImpl

import org.ggp.base.util.gdl.transforms.CommonTransforms

import org.ggp.base.util.gdl.transforms.CondensationIsolator

import org.ggp.base.util.gdl.transforms.ConstantChecker

import org.ggp.base.util.gdl.transforms.ConstantCheckerFactory

import org.ggp.base.util.gdl.transforms.DeORer

import org.ggp.base.util.gdl.transforms.GdlCleaner

import org.ggp.base.util.gdl.transforms.Relationizer

import org.ggp.base.util.gdl.transforms.VariableConstrainer

import org.ggp.base.util.propnet.architecture.Component

import org.ggp.base.util.propnet.architecture.PropNet

import org.ggp.base.util.propnet.architecture.components.And

import org.ggp.base.util.propnet.architecture.components.Constant

import org.ggp.base.util.propnet.architecture.components.Not

import org.ggp.base.util.propnet.architecture.components.Or

import org.ggp.base.util.propnet.architecture.components.Proposition

import org.ggp.base.util.propnet.architecture.components.Transition

import org.ggp.base.util.statemachine.Role

import com.google.common.collect.HashMultiset

import com.google.common.collect.Iterables

import com.google.common.collect.Lists

import com.google.common.collect.Maps

import com.google.common.collect.Multimap

import com.google.common.collect.Multiset

# 
#  * A propnet factory meant to optimize the propnet before it's even built,
#  * mostly through transforming the GDL. (The transformations identify certain
#  * classes of rules that have poor performance and replace them with equivalent
#  * rules that have better performance, with performance measured by the size of
#  * the propnet.)
#  *
#  * Known issues:
#  * - Does not work on games with many advanced forms of recursion. These include:
#  *   - Anything that breaks the SentenceModel
#  *   - Multiple sentence forms which reference one another in rules
#  *   - Not 100% confirmed to work on games where recursive rules have multiple
#  *     recursive conjuncts
#  * - Currently runs some of the transformations multiple times. A Description
#  *   object containing information about the description and its properties would
#  *   alleviate this.
#  * - It does not have a way of automatically solving the "unaffected piece rule" problem.
#  * - Depending on the settings and the situation, the behavior of the
#  *   CondensationIsolator can be either too aggressive or not aggressive enough.
#  *   Both result in excessively large games. A more sophisticated version of the
#  *   CondensationIsolator could solve these problems. A stopgap alternative is to
#  *   try both settings and use the smaller propnet (or the first to be created,
#  *   if multithreading).
#  *
#  
class OptimizingPropNetFactory(object):
    """ generated source for class OptimizingPropNetFactory """
    LEGAL = GdlPool.getConstant("legal")
    NEXT = GdlPool.getConstant("next")
    TRUE = GdlPool.getConstant("true")
    DOES = GdlPool.getConstant("does")
    GOAL = GdlPool.getConstant("goal")
    INIT = GdlPool.getConstant("init")

    # TODO: This currently doesn't actually give a different constant from INIT
    INIT_CAPS = GdlPool.getConstant("INIT")
    TERMINAL = GdlPool.getConstant("terminal")
    BASE = GdlPool.getConstant("base")
    INPUT = GdlPool.getConstant("input")
    TEMP = GdlPool.getProposition(GdlPool.getConstant("TEMP"))

    # 
    # 	 * Creates a PropNet for the game with the given description.
    # 	 *
    # 	 * @throws InterruptedException if the thread is interrupted during
    # 	 * PropNet creation.
    # 	 
    @classmethod
    @overloaded
    def create(cls, description):
        """ generated source for method create """
        return cls.create(description, False)

    @classmethod
    @create.register(object, List, bool)
    def create_0(cls, description, verbose):
        """ generated source for method create_0 """
        print "Building propnet..."
        startTime = System.currentTimeMillis()
        description = GdlCleaner.run(description)
        description = DeORer.run(description)
        description = VariableConstrainer.replaceFunctionValuedVariables(description)
        description = Relationizer.run(description)
        description = CondensationIsolator.run(description)
        if verbose:
            for gdl in description:
                print gdl
        # We want to start with a rule graph and follow the rule graph.
        # Start by finding general information about the game
        model = SentenceDomainModelFactory.createWithCartesianDomains(description)
        # Restrict domains to values that could actually come up in rules.
        # See chinesecheckers4's "count" relation for an example of why this
        # could be useful.
        model = SentenceDomainModelOptimizer.restrictDomainsToUsefulValues(model)
        if verbose:
            print "Setting constants..."
        constantChecker = ConstantCheckerFactory.createWithForwardChaining(model)
        if verbose:
            print "Done setting constants"
        sentenceFormNames = SentenceForms.getNames(model.getSentenceForms())
        usingBase = sentenceFormNames.contains("base")
        usingInput = sentenceFormNames.contains("input")
        # For now, we're going to build this to work on those with a
        # particular restriction on the dependency graph:
        # Recursive loops may only contain one sentence form.
        # This describes most games, but not all legal games.
        dependencyGraph = model.getDependencyGraph()
        if verbose:
            print "Computing topological ordering... ",
            System.out.flush()
        ConcurrencyUtils.checkForInterruption()
        topologicalOrdering = getTopologicalOrdering(model.getSentenceForms(), dependencyGraph, usingBase, usingInput)
        if verbose:
            print "done"
        roles = Role.computeRoles(description)
        components = HashMap()
        negations = HashMap()
        trueComponent = Constant(True)
        falseComponent = Constant(False)
        functionInfoMap = HashMap()
        completedSentenceFormValues = HashMap()
        for form in topologicalOrdering:
            ConcurrencyUtils.checkForInterruption()
            if verbose:
                print "Adding sentence form " + form,
                System.out.flush()
            if constantChecker.isConstantForm(form):
                if verbose:
                    print " (constant)"
                # Only add it if it's important
                if form.__name__ == cls.LEGAL or form.__name__ == cls.GOAL or form.__name__ == cls.INIT:
                    # Add it
                    for trueSentence in constantChecker.getTrueSentences(form):
                        trueProp.addInput(trueComponent)
                        trueComponent.addOutput(trueProp)
                        components.put(trueSentence, trueComponent)
                if verbose:
                    print "Checking whether " + form + " is a functional constant..."
                addConstantsToFunctionInfo(form, constantChecker, functionInfoMap)
                addFormToCompletedValues(form, completedSentenceFormValues, constantChecker)
                continue 
            if verbose:
                print 
            # TODO: Adjust "recursive forms" appropriately
            # Add a temporary sentence form thingy? ...
            addSentenceForm(form, model, components, negations, trueComponent, falseComponent, usingBase, usingInput, Collections.singleton(form), temporaryComponents, temporaryNegations, functionInfoMap, constantChecker, completedSentenceFormValues)
            # TODO: Pass these over groups of multiple sentence forms
            if verbose and not temporaryComponents.isEmpty():
                print "Processing temporary components..."
            processTemporaryComponents(temporaryComponents, temporaryNegations, components, negations, trueComponent, falseComponent)
            addFormToCompletedValues(form, completedSentenceFormValues, components)
            # if(verbose)
            # TODO: Add this, but with the correct total number of components (not just Propositions)
            # print "  "+completedSentenceFormValues.get(form).size() + " components added";
        # Connect "next" to "true"
        if verbose:
            print "Adding transitions..."
        addTransitions(components)
        # Set up "init" proposition
        if verbose:
            print "Setting up 'init' proposition..."
        setUpInit(components, trueComponent, falseComponent)
        # Now we can safely...
        removeUselessBasePropositions(components, negations, trueComponent, falseComponent)
        if verbose:
            print "Creating component set..."
        componentSet = HashSet(components.values())
        # Try saving some memory here...
        components = None
        negations = None
        completeComponentSet(componentSet)
        ConcurrencyUtils.checkForInterruption()
        if verbose:
            print "Initializing propnet object..."
        # Make it look the same as the PropNetFactory results, until we decide
        # how we want it to look
        normalizePropositions(componentSet)
        propnet = PropNet(roles, componentSet)
        if verbose:
            print "Done setting up propnet; took " + (System.currentTimeMillis() - startTime) + "ms, has " + len(componentSet) + " components and " + propnet.getNumLinks() + " links"
            print "Propnet has " + propnet.getNumAnds() + " ands; " + propnet.getNumOrs() + " ors; " + propnet.getNumNots() + " nots"
        # print propnet;
        return propnet

    @classmethod
    def removeUselessBasePropositions(cls, components, negations, trueComponent, falseComponent):
        """ generated source for method removeUselessBasePropositions """
        changedSomething = False
        for entry in components.entrySet():
            if entry.getKey().__name__ == cls.TRUE:
                if comp.getInputs().size() == 0:
                    comp.addInput(falseComponent)
                    falseComponent.addOutput(comp)
                    changedSomething = True
        if not changedSomething:
            return
        optimizeAwayTrueAndFalse(components, negations, trueComponent, falseComponent)

    # 
    # 	 * Changes the propositions contained in the propnet so that they correspond
    # 	 * to the outputs of the PropNetFactory. This is for consistency and for
    # 	 * backwards compatibility with respect to state machines designed for the
    # 	 * old propnet factory. Feel free to remove this for your player.
    # 	 *
    # 	 * @param componentSet
    # 	 
    @classmethod
    def normalizePropositions(cls, componentSet):
        """ generated source for method normalizePropositions """
        for component in componentSet:
            if isinstance(component, (Proposition, )):
                if isinstance(sentence, (GdlRelation, )):
                    if relation.__name__ == cls.NEXT:
                        p.setName(GdlPool.getProposition(GdlPool.getConstant("anon")))

    @classmethod
    @overloaded
    def addFormToCompletedValues(cls, form, completedSentenceFormValues, constantChecker):
        """ generated source for method addFormToCompletedValues """
        sentences = ArrayList()
        sentences.addAll(constantChecker.getTrueSentences(form))
        completedSentenceFormValues.put(form, sentences)

    @classmethod
    @addFormToCompletedValues.register(object, SentenceForm, Map, Map)
    def addFormToCompletedValues_0(cls, form, completedSentenceFormValues, components):
        """ generated source for method addFormToCompletedValues_0 """
        # Kind of inefficient. Could do better by collecting these as we go,
        # then adding them back into the CSFV map once the sentence forms are complete.
        # completedSentenceFormValues.put(form, new ArrayList<GdlSentence>());
        sentences = ArrayList()
        for sentence in components.keySet():
            ConcurrencyUtils.checkForInterruption()
            if form.matches(sentence):
                # The sentence has a node associated with it
                sentences.add(sentence)
        completedSentenceFormValues.put(form, sentences)

    @classmethod
    def addConstantsToFunctionInfo(cls, form, constantChecker, functionInfoMap):
        """ generated source for method addConstantsToFunctionInfo """
        functionInfoMap.put(form, FunctionInfoImpl.create(form, constantChecker))

    @classmethod
    def processTemporaryComponents(cls, temporaryComponents, temporaryNegations, components, negations, trueComponent, falseComponent):
        """ generated source for method processTemporaryComponents """
        # For each component in temporary components, we want to "put it back"
        # into the main components section.
        # We also want to do optimization here...
        # We don't want to end up with anything following from true/false.
        # Everything following from a temporary component (its outputs)
        # should instead become an output of the actual component.
        # If there is no actual component generated, then the statement
        # is necessarily FALSE and should be replaced by the false
        # component.
        for sentence in temporaryComponents.keySet():
            if realComp == None:
                realComp = falseComponent
            for output in tempComp.getOutputs():
                # Disconnect
                output.removeInput(tempComp)
                # tempComp.removeOutput(output); //do at end
                # Connect
                output.addInput(realComp)
                realComp.addOutput(output)
            tempComp.removeAllOutputs()
            if temporaryNegations.containsKey(sentence):
                # Should be pointing to a "not" that now gets input from realComp
                # Should be fine to put into negations
                negations.put(sentence, temporaryNegations.get(sentence))
                # If this follows true/false, will get resolved by the next set of optimizations
            optimizeAwayTrueAndFalse(components, negations, trueComponent, falseComponent)

    # 
    # 	 * Components and negations may be null, if e.g. this is a post-optimization.
    # 	 * TrueComponent and falseComponent are required.
    # 	 *
    # 	 * Doesn't actually work that way... shoot. Need something that will remove the
    # 	 * component from the propnet entirely.
    # 	 * @throws InterruptedException
    # 	 
    @classmethod
    @overloaded
    def optimizeAwayTrueAndFalse(cls, components, negations, trueComponent, falseComponent):
        """ generated source for method optimizeAwayTrueAndFalse """
        while hasNonessentialChildren(trueComponent) or hasNonessentialChildren(falseComponent):
            ConcurrencyUtils.checkForInterruption()
            optimizeAwayTrue(components, negations, None, trueComponent, falseComponent)
            optimizeAwayFalse(components, negations, None, trueComponent, falseComponent)

    @classmethod
    @optimizeAwayTrueAndFalse.register(object, PropNet, Component, Component)
    def optimizeAwayTrueAndFalse_0(cls, pn, trueComponent, falseComponent):
        """ generated source for method optimizeAwayTrueAndFalse_0 """
        while hasNonessentialChildren(trueComponent) or hasNonessentialChildren(falseComponent):
            optimizeAwayTrue(None, None, pn, trueComponent, falseComponent)
            optimizeAwayFalse(None, None, pn, trueComponent, falseComponent)

    # TODO: Create a version with just a set of components that we can share with post-optimizations
    @classmethod
    def optimizeAwayFalse(cls, components, negations, pn, trueComponent, falseComponent):
        """ generated source for method optimizeAwayFalse """
        assert ((components != None and negations != None) or pn != None)
        assert ((components == None and negations == None) or pn == None)
        for output in Lists.newArrayList(falseComponent.getOutputs()):
            if isEssentialProposition(output) or isinstance(output, (Transition, )):
                # Since this is the false constant, there are a few "essential" types
                # we don't actually want to keep around.
                if not isLegalOrGoalProposition(output):
                    continue 
            if isinstance(output, (Proposition, )):
                # Move its outputs to be outputs of false
                for child in output.getOutputs():
                    # Disconnect
                    child.removeInput(output)
                    # output.removeOutput(child); //do at end
                    # Reconnect; will get children before returning, if nonessential
                    falseComponent.addOutput(child)
                    child.addInput(falseComponent)
                output.removeAllOutputs()
                if not isEssentialProposition(output):
                    # Remove the proposition entirely
                    falseComponent.removeOutput(output)
                    output.removeInput(falseComponent)
                    # Update its location to the trueComponent in our map
                    if components != None:
                        components.put(prop.__name__, falseComponent)
                        negations.put(prop.__name__, trueComponent)
                    else:
                        pn.removeComponent(output)
            elif isinstance(output, (And, )):
                # Attach children of and to falseComponent
                for child in and_.getOutputs():
                    child.addInput(falseComponent)
                    falseComponent.addOutput(child)
                    child.removeInput(and_)
                # Disconnect and completely
                and_.removeAllOutputs()
                for parent in and_.getInputs():
                    parent.removeOutput(and_)
                and_.removeAllInputs()
                if pn != None:
                    pn.removeComponent(and_)
            elif isinstance(output, (Or, )):
                # Remove as input from or
                or_.removeInput(falseComponent)
                falseComponent.removeOutput(or_)
                # If or has only one input, remove it
                if or_.getInputs().size() == 1:
                    or_.removeInput(in_)
                    in_.removeOutput(or_)
                    for out in or_.getOutputs():
                        # Disconnect from and
                        out.removeInput(or_)
                        # or.removeOutput(out); //do at end
                        # Connect directly to the new input
                        out.addInput(in_)
                        in_.addOutput(out)
                    or_.removeAllOutputs()
                    if pn != None:
                        pn.removeComponent(or_)
                elif or_.getInputs().size() == 0:
                    if pn != None:
                        pn.removeComponent(or_)
            elif isinstance(output, (Not, )):
                # Disconnect from falseComponent
                not_.removeInput(falseComponent)
                falseComponent.removeOutput(not_)
                # Connect all children of the not to trueComponent
                for child in not_.getOutputs():
                    # Disconnect
                    child.removeInput(not_)
                    # not.removeOutput(child); //Do at end
                    # Connect to trueComponent
                    child.addInput(trueComponent)
                    trueComponent.addOutput(child)
                not_.removeAllOutputs()
                if pn != None:
                    pn.removeComponent(not_)
            elif isinstance(output, (Transition, )):
                # ???
                System.err.println("Fix optimizeAwayFalse's case for Transitions")

    @classmethod
    def isLegalOrGoalProposition(cls, comp):
        """ generated source for method isLegalOrGoalProposition """
        if not (isinstance(comp, (Proposition, ))):
            return False
        prop = comp
        name = prop.__name__
        return name.__name__ == GdlPool.LEGAL or name.__name__ == GdlPool.GOAL

    @classmethod
    def optimizeAwayTrue(cls, components, negations, pn, trueComponent, falseComponent):
        """ generated source for method optimizeAwayTrue """
        assert ((components != None and negations != None) or pn != None)
        for output in Lists.newArrayList(trueComponent.getOutputs()):
            if isEssentialProposition(output) or isinstance(output, (Transition, )):
                continue 
            if isinstance(output, (Proposition, )):
                # Move its outputs to be outputs of true
                for child in output.getOutputs():
                    # Disconnect
                    child.removeInput(output)
                    # output.removeOutput(child); //do at end
                    # Reconnect; will get children before returning, if nonessential
                    trueComponent.addOutput(child)
                    child.addInput(trueComponent)
                output.removeAllOutputs()
                if not isEssentialProposition(output):
                    # Remove the proposition entirely
                    trueComponent.removeOutput(output)
                    output.removeInput(trueComponent)
                    # Update its location to the trueComponent in our map
                    if components != None:
                        components.put(prop.__name__, trueComponent)
                        negations.put(prop.__name__, falseComponent)
                    else:
                        pn.removeComponent(output)
            elif isinstance(output, (Or, )):
                # Attach children of or to trueComponent
                for child in or_.getOutputs():
                    child.addInput(trueComponent)
                    trueComponent.addOutput(child)
                    child.removeInput(or_)
                # Disconnect or completely
                or_.removeAllOutputs()
                for parent in or_.getInputs():
                    parent.removeOutput(or_)
                or_.removeAllInputs()
                if pn != None:
                    pn.removeComponent(or_)
            elif isinstance(output, (And, )):
                # Remove as input from and
                and_.removeInput(trueComponent)
                trueComponent.removeOutput(and_)
                # If and has only one input, remove it
                if and_.getInputs().size() == 1:
                    and_.removeInput(in_)
                    in_.removeOutput(and_)
                    for out in and_.getOutputs():
                        # Disconnect from and
                        out.removeInput(and_)
                        # and.removeOutput(out); //do at end
                        # Connect directly to the new input
                        out.addInput(in_)
                        in_.addOutput(out)
                    and_.removeAllOutputs()
                    if pn != None:
                        pn.removeComponent(and_)
                elif and_.getInputs().size() == 0:
                    if pn != None:
                        pn.removeComponent(and_)
            elif isinstance(output, (Not, )):
                # Disconnect from trueComponent
                not_.removeInput(trueComponent)
                trueComponent.removeOutput(not_)
                # Connect all children of the not to falseComponent
                for child in not_.getOutputs():
                    # Disconnect
                    child.removeInput(not_)
                    # not.removeOutput(child); //Do at end
                    # Connect to falseComponent
                    child.addInput(falseComponent)
                    falseComponent.addOutput(child)
                not_.removeAllOutputs()
                if pn != None:
                    pn.removeComponent(not_)
            elif isinstance(output, (Transition, )):
                # ???
                System.err.println("Fix optimizeAwayTrue's case for Transitions")

    @classmethod
    def hasNonessentialChildren(cls, trueComponent):
        """ generated source for method hasNonessentialChildren """
        for child in trueComponent.getOutputs():
            if isinstance(child, (Transition, )):
                continue 
            if not isEssentialProposition(child):
                return True
            # We don't want any grandchildren, either
            if not child.getOutputs().isEmpty():
                return True
        return False

    @classmethod
    def isEssentialProposition(cls, component):
        """ generated source for method isEssentialProposition """
        if not (isinstance(component, (Proposition, ))):
            return False
        # We're looking for things that would be outputs of "true" or "false",
        # but we would still want to keep as propositions to be read by the
        # state machine
        prop = component
        name = prop.__name__.__name__
        return name == cls.LEGAL or name == cls.GOAL or name == cls.INIT or name == cls.TERMINAL

    @classmethod
    def completeComponentSet(cls, componentSet):
        """ generated source for method completeComponentSet """
        newComponents = HashSet()
        componentsToTry = HashSet(componentSet)
        while not componentsToTry.isEmpty():
            for c in componentsToTry:
                for out in c.getOutputs():
                    if not componentSet.contains(out):
                        newComponents.add(out)
                for in_ in c.getInputs():
                    if not componentSet.contains(in_):
                        newComponents.add(in_)
            componentSet.addAll(newComponents)
            componentsToTry = newComponents
            newComponents = HashSet()

    @classmethod
    def addTransitions(cls, components):
        """ generated source for method addTransitions """
        for entry in components.entrySet():
            if sentence.__name__ == cls.NEXT:
                # connect to true
                # There might be no true component (for example, because the bases
                # told us so). If that's the case, don't have a transition.
                if trueComponent == None:
                    #  Skipping transition to supposedly impossible 'trueSentence'
                    continue 
                transition.addInput(nextComponent)
                nextComponent.addOutput(transition)
                transition.addOutput(trueComponent)
                trueComponent.addInput(transition)

    # TODO: Replace with version using constantChecker only
    # TODO: This can give problematic results if interpreted in
    # the standard way (see test_case_3d)
    @classmethod
    def setUpInit(cls, components, trueComponent, falseComponent):
        """ generated source for method setUpInit """
        initProposition = Proposition(GdlPool.getProposition(cls.INIT_CAPS))
        for entry in components.entrySet():
            # Is this something that will be true?
            if entry.getValue() == trueComponent:
                if entry.getKey().__name__ == cls.INIT:
                    if trueSentenceComponent.getInputs().isEmpty():
                        transition.addInput(initProposition)
                        initProposition.addOutput(transition)
                        trueSentenceComponent.addInput(transition)
                        transition.addOutput(trueSentenceComponent)
                    else:
                        input.removeOutput(transition)
                        transition.removeInput(input)
                        orInputs.add(input)
                        orInputs.add(initProposition)
                        orify(orInputs, transition, falseComponent)

    @classmethod
    def orify(cls, inputs, output, falseProp):
        """ generated source for method orify """
        for in_ in inputs:
            if isinstance(in_, (Constant, )) and in_.getValue():
                in_.addOutput(output)
                output.addInput(in_)
                return
        or_ = Or()
        for in_ in inputs:
            if not (isinstance(in_, (Constant, ))):
                in_.addOutput(or_)
                or_.addInput(in_)
        if or_.getInputs().isEmpty():
            falseProp.addOutput(output)
            output.addInput(falseProp)
            return
        if or_.getInputs().size() == 1:
            in_.removeOutput(or_)
            or_.removeInput(in_)
            in_.addOutput(output)
            output.addInput(in_)
            return
        or_.addOutput(output)
        output.addInput(or_)

    @classmethod
    def getTopologicalOrdering(cls, forms, dependencyGraph, usingBase, usingInput):
        """ generated source for method getTopologicalOrdering """
        queue = LinkedList(forms)
        ordering = ArrayList(len(forms))
        alreadyOrdered = HashSet()
        while not queue.isEmpty():
            for dependency in dependencyGraph.get(curForm):
                if not dependency == curForm and not alreadyOrdered.contains(dependency):
                    readyToAdd = False
                    break
            if usingBase and (curForm.__name__ == cls.TRUE or curForm.__name__ == cls.NEXT or curForm.__name__ == cls.INIT):
                if not alreadyOrdered.contains(baseForm):
                    readyToAdd = False
            if usingInput and (curForm.__name__ == cls.DOES or curForm.__name__ == cls.LEGAL):
                if not alreadyOrdered.contains(inputForm):
                    readyToAdd = False
            if readyToAdd:
                ordering.add(curForm)
                alreadyOrdered.add(curForm)
            else:
                queue.add(curForm)
            ConcurrencyUtils.checkForInterruption()
        return ordering

    @classmethod
    def addSentenceForm(cls, form, model, components, negations, trueComponent, falseComponent, usingBase, usingInput, recursionForms, temporaryComponents, temporaryNegations, functionInfoMap, constantChecker, completedSentenceFormValues):
        """ generated source for method addSentenceForm """
        alwaysTrueSentences = model.getSentencesListedAsTrue(form)
        rules = model.getRules(form)
        for alwaysTrueSentence in alwaysTrueSentences:
            if alwaysTrueSentence.__name__ == cls.LEGAL or alwaysTrueSentence.__name__ == cls.NEXT or alwaysTrueSentence.__name__ == cls.GOAL:
                trueComponent.addOutput(prop)
                prop.addInput(trueComponent)
            components.put(alwaysTrueSentence, trueComponent)
            negations.put(alwaysTrueSentence, falseComponent)
            continue 
        if usingInput and form.__name__ == cls.DOES:
            for inputSentence in constantChecker.getTrueSentences(inputForm):
                components.put(doesSentence, prop)
            return
        if usingBase and form.__name__ == cls.TRUE:
            for baseSentence in constantChecker.getTrueSentences(baseForm):
                components.put(trueSentence, prop)
            return
        inputsToOr = HashMap()
        for rule in rules:
            varsInLiveConjuncts.addAll(GdlUtils.getVariables(rule.getHead()))
            while asnItr.hasNext():
                if assignment == None:
                    continue 
                ConcurrencyUtils.checkForInterruption()
                for literal in rule.getBody():
                    if isinstance(literal, (GdlSentence, )):
                        if constantChecker.isConstantForm(conjunctForm):
                            if not constantChecker.isTrueConstant(transformed):
                                asnItr.changeOneInNext(varsToChange, assignment)
                                componentsToConnect.add(None)
                            continue 
                        if conj == None:
                            conj = temporaryComponents.get(transformed)
                        if conj == None and SentenceModelUtils.inSentenceFormGroup(transformed, recursionForms):
                            temporaryComponents.put(transformed, tempProp)
                            conj = tempProp
                        if conj == None or isThisConstant(conj, falseComponent):
                            asnItr.changeOneInNext(varsInConjunct, assignment)
                            componentsToConnect.add(None)
                            continue 
                        componentsToConnect.add(conj)
                    elif isinstance(literal, (GdlNot, )):
                        if constantChecker.isConstantForm(conjunctForm):
                            if constantChecker.isTrueConstant(transformed):
                                asnItr.changeOneInNext(varsToChange, assignment)
                                componentsToConnect.add(None)
                            continue 
                        if isThisConstant(conj, falseComponent):
                            asnItr.changeOneInNext(varsInConjunct, assignment)
                            componentsToConnect.add(None)
                            continue 
                        if conj == None:
                            conj = temporaryNegations.get(transformed)
                        if conj == None and SentenceModelUtils.inSentenceFormGroup(transformed, recursionForms):
                            if positive == None:
                                positive = temporaryComponents.get(transformed)
                            if positive == None:
                                temporaryComponents.put(transformed, tempProp)
                                positive = tempProp
                            not_.addInput(positive)
                            positive.addOutput(not_)
                            temporaryNegations.put(transformed, not_)
                            conj = not_
                        if conj == None:
                            if positive == None:
                                continue 
                            if existingNotOutput != None:
                                componentsToConnect.add(existingNotOutput)
                                negations.put(transformed, existingNotOutput)
                                continue 
                            not_.addInput(positive)
                            positive.addOutput(not_)
                            negations.put(transformed, not_)
                            conj = not_
                        componentsToConnect.add(conj)
                    elif isinstance(literal, (GdlDistinct, )):
                    else:
                        raise RuntimeException("Unwanted GdlLiteral type")
                if not componentsToConnect.contains(None):
                    andify(componentsToConnect, andComponent, trueComponent)
                    if not isThisConstant(andComponent, falseComponent):
                        if not inputsToOr.containsKey(sentence):
                            inputsToOr.put(sentence, HashSet())
                        inputsToOr.get(sentence).add(andComponent)
                        if preventDuplicatesFromConstants:
                            asnItr.changeOneInNext(varsInLiveConjuncts, assignment)

        for entry in inputsToOr.entrySet():
            ConcurrencyUtils.checkForInterruption()
            for input in inputs:
                if isinstance(input, (Constant, )) or input.getInputs().size() == 0:
                    realInputs.add(input)
                else:
                    realInputs.add(input.getSingleInput())
                    input.getSingleInput().removeOutput(input)
                    input.removeAllInputs()
            cls.orify(realInputs, prop, falseComponent)
            components.put(sentence, prop)
        if form.__name__ == cls.TRUE or form.__name__ == cls.DOES:
            for sentence in model.getDomain(form):
                ConcurrencyUtils.checkForInterruption()
                components.put(sentence, prop)

    @classmethod
    def getVarsInLiveConjuncts(cls, rule, constantSentenceForms):
        """ generated source for method getVarsInLiveConjuncts """
        result = HashSet()
        for literal in rule.getBody():
            if isinstance(literal, (GdlRelation, )):
                if not SentenceModelUtils.inSentenceFormGroup(literal, constantSentenceForms):
                    result.addAll(GdlUtils.getVariables(literal))
            elif isinstance(literal, (GdlNot, )):
                if not SentenceModelUtils.inSentenceFormGroup(inner, constantSentenceForms):
                    result.addAll(GdlUtils.getVariables(literal))
        return result

    @classmethod
    def isThisConstant(cls, conj, constantComponent):
        """ generated source for method isThisConstant """
        if conj == constantComponent:
            return True
        return (isinstance(conj, (Proposition, )) and conj.getInputs().size() == 1 and conj.getSingleInput() == constantComponent)

    @classmethod
    def getNotOutput(cls, positive):
        """ generated source for method getNotOutput """
        for c in positive.getOutputs():
            if isinstance(c, (Not, )):
                return c
        return None

    @classmethod
    def getVarsInConjunct(cls, literal):
        """ generated source for method getVarsInConjunct """
        return GdlUtils.getVariables(literal)

    @classmethod
    def andify(cls, inputs, output, trueProp):
        """ generated source for method andify """
        for c in inputs:
            if isinstance(c, (Constant, )) and not c.getValue():
                output.addInput(c)
                c.addOutput(output)
                return
        and_ = And()
        for in_ in inputs:
            if not (isinstance(in_, (Constant, ))):
                in_.addOutput(and_)
                and_.addInput(in_)
        if and_.getInputs().isEmpty():
            trueProp.addOutput(output)
            output.addInput(trueProp)
            return
        if and_.getInputs().size() == 1:
            in_.removeOutput(and_)
            and_.removeInput(in_)
            in_.addOutput(output)
            output.addInput(in_)
            return
        and_.addOutput(output)
        output.addInput(and_)

    class Type:
        """ generated source for enum Type """
        hasTrue = bool()
        hasFalse = bool()

        def __init__(self, hasTrue, hasFalse):
            """ generated source for method __init__ """
            self.hasTrue = hasTrue
            self.hasFalse = hasFalse

        def includes(self, other):
            """ generated source for method includes """
            if other==BOTH:
                return self.hasTrue and self.hasFalse
            elif other==FALSE:
                return self.hasFalse
            elif other==NEITHER:
                return True
            elif other==self.TRUE:
                return self.hasTrue
            raise RuntimeException()

        def with_(self, otherType):
            """ generated source for method with_ """
            if otherType == None:
                otherType = NEITHER
            if otherType==BOTH:
                return BOTH
            elif otherType==NEITHER:
                return self
            elif otherType==self.TRUE:
                if self.hasFalse:
                    return BOTH
                else:
                    return self.TRUE
            elif otherType==FALSE:
                if self.hasTrue:
                    return BOTH
                else:
                    return FALSE
            raise RuntimeException()

        def minus(self, other):
            """ generated source for method minus """
            if other==BOTH:
                return NEITHER
            elif other==self.TRUE:
                return FALSE if self.hasFalse else NEITHER
            elif other==FALSE:
                return self.TRUE if self.hasTrue else NEITHER
            elif other==NEITHER:
                return self
            raise RuntimeException()

        def opposite(self):
            """ generated source for method opposite """
            if self==self.TRUE:
                return FALSE
            elif self==FALSE:
                return self.TRUE
            elif self==NEITHER:
                pass
            elif self==BOTH:
                return self
            raise RuntimeException()

    Type.NEITHER = Type(False, False)
    Type.TRUE = Type(True, False)
    Type.FALSE = Type(False, True)
    Type.BOTH = Type(True, True)

    @classmethod
    def removeUnreachableBasesAndInputs(cls, pn, basesTrueByInit):
        """ generated source for method removeUnreachableBasesAndInputs """
        reachability = Maps.newHashMap()
        numTrueInputs = HashMultiset.create()
        numFalseInputs = HashMultiset.create()
        toAdd = Stack()
        legalsToInputs = Maps.newHashMap()
        for legalProp in Iterables.concat(pn.getLegalPropositions().values()):
            if inputProp != None:
                legalsToInputs.put(legalProp, inputProp)
        for c in pn.getComponents():
            ConcurrencyUtils.checkForInterruption()
            if isinstance(c, (Constant, )):
                if c.getValue():
                    toAdd.add(Pair.of(c, cls.Type.TRUE))
                else:
                    toAdd.add(Pair.of(c, cls.Type.FALSE))
        for p in pn.getInputPropositions().values():
            toAdd.add(Pair.of(p, cls.Type.FALSE))
        for baseProp in pn.getBasePropositions().values():
            if basesTrueByInit.contains(baseProp):
                toAdd.add(Pair.of(baseProp, cls.Type.TRUE))
            else:
                toAdd.add(Pair.of(baseProp, cls.Type.FALSE))
        initProposition = pn.getInitProposition()
        toAdd.add(Pair.of(initProposition, cls.Type.BOTH))
        while not toAdd.isEmpty():
            ConcurrencyUtils.checkForInterruption()
            if oldType == None:
                oldType = cls.Type.NEITHER
            if isinstance(curComp, (Proposition, )):
                typeToAdd = newInputType
            elif isinstance(curComp, (Transition, )):
                typeToAdd = newInputType
            elif isinstance(curComp, (Constant, )):
                typeToAdd = newInputType
            elif isinstance(curComp, (Not, )):
                typeToAdd = newInputType.opposite()
            elif isinstance(curComp, (And, )):
                if newInputType.hasTrue:
                    numTrueInputs.add(curComp)
                    if numTrueInputs.count(curComp) == curComp.getInputs().size():
                        typeToAdd = cls.Type.TRUE
                if newInputType.hasFalse:
                    typeToAdd = typeToAdd.with_(cls.Type.FALSE)
            elif isinstance(curComp, (Or, )):
                if newInputType.hasFalse:
                    numFalseInputs.add(curComp)
                    if numFalseInputs.count(curComp) == curComp.getInputs().size():
                        typeToAdd = cls.Type.FALSE
                if newInputType.hasTrue:
                    typeToAdd = typeToAdd.with_(cls.Type.TRUE)
            else:
                raise RuntimeException("Unhandled component type " + curComp.__class__)
            if oldType.includes(typeToAdd):
                continue 
            reachability.put(curComp, typeToAdd.with_(oldType))
            typeToAdd = typeToAdd.minus(oldType)
            if typeToAdd == cls.Type.NEITHER:
                raise RuntimeException("Something's messed up here")
            for output in curComp.getOutputs():
                toAdd.add(Pair.of(output, typeToAdd))
            if legalsToInputs.containsKey(curComp):
                if inputProp == None:
                    raise IllegalStateException()
                toAdd.add(Pair.of(inputProp, typeToAdd))
        trueConst = Constant(True)
        falseConst = Constant(False)
        pn.addComponent(trueConst)
        pn.addComponent(falseConst)
        for entry in reachability.entrySet():
            if type_ == cls.Type.TRUE or type_ == cls.Type.FALSE:
                if isinstance(c, (Constant, )):
                    continue 
                for input in c.getInputs():
                    input.removeOutput(c)
                c.removeAllInputs()
                if type_ == cls.Type.TRUE ^ (isinstance(c, (Not, ))):
                    c.addInput(trueConst)
                    trueConst.addOutput(c)
                else:
                    c.addInput(falseConst)
                    falseConst.addOutput(c)
        cls.optimizeAwayTrueAndFalse(pn, trueConst, falseConst)

    @classmethod
    def lopUselessLeaves(cls, pn):
        """ generated source for method lopUselessLeaves """
        usefulComponents = HashSet()
        toAdd = Stack()
        toAdd.add(pn.getTerminalProposition())
        usefulComponents.add(pn.getInitProposition())
        for goalProps in pn.getGoalPropositions().values():
            toAdd.addAll(goalProps)
        for legalProps in pn.getLegalPropositions().values():
            toAdd.addAll(legalProps)
        while not toAdd.isEmpty():
            if usefulComponents.contains(curComp):
                continue 
            usefulComponents.add(curComp)
            toAdd.addAll(curComp.getInputs())
        allComponents = ArrayList(pn.getComponents())
        for c in allComponents:
            if not usefulComponents.contains(c):
                pn.removeComponent(c)

    @classmethod
    def removeInits(cls, pn):
        """ generated source for method removeInits """
        toRemove = ArrayList()
        for p in pn.getPropositions():
            if isinstance(, (GdlRelation, )):
                if relation.__name__ == cls.INIT:
                    toRemove.add(p)
        for p in toRemove:
            pn.removeComponent(p)

    @classmethod
    def removeAnonymousPropositions(cls, pn):
        """ generated source for method removeAnonymousPropositions """
        toSplice = ArrayList()
        toReplaceWithFalse = ArrayList()
        for p in pn.getPropositions():
            if p.getInputs().size() == 1 and isinstance(, (Transition, )):
                continue 
            if isinstance(sentence, (GdlProposition, )):
                if sentence.__name__ == cls.TERMINAL or sentence.__name__ == cls.INIT_CAPS:
                    continue 
            else:
                if name == cls.LEGAL or name == cls.GOAL or name == cls.DOES or name == cls.INIT:
                    continue 
            if p.getInputs().size() < 1:
                toReplaceWithFalse.add(p)
                continue 
            if p.getInputs().size() != 1:
                System.err.println("Might have falsely declared " + p.__name__ + " to be unimportant?")
            toSplice.add(p)
        for p in toSplice:
            pn.removeComponent(p)
            if len(inputs) > 1:
                System.err.println("Programmer made a bad assumption here... might lead to trouble?")
            for input in inputs:
                for output in outputs:
                    input.addOutput(output)
                    output.addInput(input)
        for p in toReplaceWithFalse:
            print "Should be replacing " + p + " with false, but should do that in the OPNF, really; better equipped to do that there"

