#!/usr/bin/env python
""" generated source for module PropNetAnnotatedFlattener """
# package: org.ggp.base.util.propnet.factory.flattener
import java.util.ArrayList

import java.util.HashMap

import java.util.HashSet

import java.util.LinkedList

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.transforms.DeORer

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.propnet.factory.annotater.PropNetAnnotater

import org.ggp.base.util.prover.aima.substituter.Substituter

import org.ggp.base.util.prover.aima.substitution.Substitution

import org.ggp.base.util.prover.aima.unifier.Unifier

# 
#  * PropNetAnnotatedFlattener is an implementation of a GDL flattener that needs
#  * the rules to contain ( base ?x ) propositions that explicitly specify domains
#  * for all of the base propositions.
#  *
#  * This flattener should work on all sizes of games, but requires these explicit
#  * annotations to be present in the game description; it cannot infer them.
#  *
#  * A separate PropNetAnnotater class is able to generate these annotations.
#  * Sadly, it can only annotate relatively simple games. If there are no base
#  * propositions in a game description, PropNetAnnotatedFlattener will call
#  * the annotater in an attempt to generate annotations.
#  *
#  * To use this class:
#  *      PropNetAnnotatedFlattener AF = new PropNetAnnotatedFlattener(description);
#  *      List<GdlRule> flatDescription = AF.flatten();
#  *      return converter.convert(flatDescription);
#  
class PropNetAnnotatedFlattener(object):
    """ generated source for class PropNetAnnotatedFlattener """
    #  An archive of Rule instantiations, indexed by head name. 
    instantiations = Map()

    #  An archive of the rules in a game description, indexed by head name. 
    templates = Map()

    # 
    #      * Construct a BasicPropNetFlattener for a given game.
    #      
    description = List()

    def __init__(self, description):
        """ generated source for method __init__ """
        self.description = description

    # 
    #      * Flattens a game description using the following process:
    #      * <ol>
    #      * <li>Records the rules in the description, and indexes them by head name.</li>
    #      * <li>Creates an archive of rule instantiations, initialized with
    #      * <tt>true</tt> rules.</li>
    #      * <li>Creates every instantiation of each rule in the description and
    #      * records the result.</li>
    #      * </ol>
    #      *
    #      * @param description
    #      *            A game description.
    #      * @return An equivalent description, without variables.
    #      
    def flatten(self):
        """ generated source for method flatten """
        self.description = DeORer.run(self.description)
        if noAnnotations():
            GamerLogger.log("StateMachine", "Could not find 'base' annotations. Attempting to generate them...")
            self.description = PropNetAnnotater(self.description).getAugmentedDescription()
            GamerLogger.log("StateMachine", "Annotations generated.")
        self.templates = recordTemplates(self.description)
        self.instantiations = initializeInstantiations(self.description)
        flatDescription = ArrayList()
        for constant in templates.keySet():
            flatDescription.addAll(getInstantiations(constant))
        return flatDescription

    def noAnnotations(self):
        """ generated source for method noAnnotations """
        for gdl in description:
            if not (isinstance(gdl, (GdlSentence, ))):
                continue 
            if sentence.__name__.getValue() == "base":
                return False
        return True

    def expandTrue(self, base, index, workingSet, results):
        """ generated source for method expandTrue """
        if base.arity() == index:
            results.add(GdlPool.getRule(GdlPool.getRelation(GdlPool.getConstant("true"), [None]*)))
        else:
            for term in (base.get(index)).getBody():
                workingSet.addLast(term)
                self.expandTrue(base, index + 1, workingSet, results)
                workingSet.removeLast()

    def getInstantiations(self, constant):
        """ generated source for method getInstantiations """
        if not self.instantiations.containsKey(constant):
            self.instantiations.put(constant, ArrayList())
            if constant.getValue() == "does":
                for rule in getInstantiations(GdlPool.getConstant("legal")):
                    self.instantiations.get(constant).add(equivalentDoesRule)
            else:
                for template in templates.get(constant):
                    instantiate(template, 0, Substitution(), results)
                    self.instantiations.get(constant).addAll(results)
        return self.instantiations.get(constant)

    def initializeInstantiations(self, description):
        """ generated source for method initializeInstantiations """
        trues = ArrayList()
        for gdl in description:
            if isinstance(gdl, (GdlSentence, )):
                if sentence.__name__.getValue() == "base":
                    if sentence.arity() == 1:
                        trues.add(GdlPool.getRule(GdlPool.getRelation(GdlPool.getConstant("true"), [None]*)))
                    else:
                        self.expandTrue(sentence, 1, LinkedList(), results)
                        trues.addAll(results)
        instantiations = HashMap()
        instantiations.put(GdlPool.getConstant("true"), trues)
        return instantiations

    def instantiate(self, template, index, theta, results):
        """ generated source for method instantiate """
        if template.getBody().size() == index:
            results.add(Substituter.substitute(template, theta))
        else:
            if isinstance(literal, (GdlSentence, )):
                for instantiation in getInstantiations(sentence.__name__):
                    if thetaPrime != None:
                        thetaCopy = thetaCopy.compose(thetaPrime)
                        self.instantiate(template, index + 1, thetaCopy, results)
            else:
                self.instantiate(template, index + 1, theta, results)

    def recordTemplates(self, description):
        """ generated source for method recordTemplates """
        templates = HashMap()
        for gdl in description:
            if not name.getValue() == "base":
                if not templates.containsKey(name):
                    templates.put(name, ArrayList())
                templates.get(name).add(rule)
        return templates

