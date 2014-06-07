#!/usr/bin/env python
""" generated source for module PropNetConverter """
# package: org.ggp.base.util.propnet.factory.converter
import java.util.ArrayList

import java.util.HashMap

import java.util.HashSet

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.propnet.architecture.Component

import org.ggp.base.util.propnet.architecture.PropNet

import org.ggp.base.util.propnet.architecture.components.And

import org.ggp.base.util.propnet.architecture.components.Constant

import org.ggp.base.util.propnet.architecture.components.Not

import org.ggp.base.util.propnet.architecture.components.Or

import org.ggp.base.util.propnet.architecture.components.Proposition

import org.ggp.base.util.propnet.architecture.components.Transition

import org.ggp.base.util.statemachine.Role

# 
#  * The PropNetConverter class defines PropNet conversion for the PropNetFactory
#  * class. This takes in a flattened game description, and converts it into an
#  * equivalent PropNet.
#  
class PropNetConverter(object):
    """ generated source for class PropNetConverter """
    #  An archive of Propositions, indexed by name. 
    propositions = Map()

    #  An archive of Components. 
    components = Set()

    # 
    # 	 * Converts a game description to a PropNet using the following process
    # 	 * (note that this method and all of the methods that it invokes assume that
    # 	 * <tt>description</tt> has already been flattened by a PropNetFlattener):
    # 	 * <ol>
    # 	 * <li>Transforms each of the rules in <tt>description</tt> into
    # 	 * equivalent PropNet Components.</li>
    # 	 * <li>Adds or gates to Propositions with more than one input.</li>
    # 	 * <li>Adds inputs that are implicitly specified by <tt>description</tt>.</li>
    # 	 * </ol>
    # 	 *
    # 	 * @param description
    # 	 *            A game description.
    # 	 * @return An equivalent PropNet.
    # 	 
    def convert(self, roles, description):
        """ generated source for method convert """
        self.propositions = HashMap()
        self.components = HashSet()
        for rule in description:
            if rule.arity() > 0:
                convertRule(rule)
            else:
                convertStatic(rule.getHead())
        fixDisjunctions()
        addMissingInputs()
        return PropNet(roles, self.components)

    # 
    # 	 * Creates an equivalent InputProposition for every LegalProposition where
    # 	 * none already exists.
    # 	 
    def addMissingInputs(self):
        """ generated source for method addMissingInputs """
        addList = ArrayList()
        for proposition in propositions.values():
            if isinstance(, (GdlRelation, )):
                if relation.__name__.getValue() == "legal":
                    addList.add(proposition)
        for addItem in addList:
            self.components.add(getProposition(GdlPool.getRelation(GdlPool.getConstant("does"), relation.getBody())))

    def convertConjunct(self, literal):
        """ generated source for method convertConjunct """
        if isinstance(literal, (GdlDistinct, )):
            link(constant, proposition)
            self.components.add(proposition)
            self.components.add(constant)
            return proposition
        elif isinstance(literal, (GdlNot, )):
            link(input, no)
            link(no, output)
            self.components.add(input)
            self.components.add(no)
            self.components.add(output)
            return output
        else:
            self.components.add(proposition)
            return proposition

    def convertHead(self, sentence):
        """ generated source for method convertHead """
        if sentence.__name__.getValue() == "next":
            link(preTransition, transition)
            link(transition, head)
            self.components.add(head)
            self.components.add(transition)
            self.components.add(preTransition)
            return preTransition
        else:
            self.components.add(proposition)
            return proposition

    def convertRule(self, rule):
        """ generated source for method convertRule """
        head = self.convertHead(rule.getHead())
        and_ = And()
        link(and_, head)
        self.components.add(head)
        self.components.add(and_)
        for literal in rule.getBody():
            link(conjunct, and_)

    def convertStatic(self, sentence):
        """ generated source for method convertStatic """
        if sentence.__name__.getValue() == "init":
            link(init, transition)
            link(transition, proposition)
            self.components.add(init)
            self.components.add(transition)
            self.components.add(proposition)
        constant = Constant(True)
        proposition = getProposition(sentence)
        link(constant, proposition)
        self.components.add(constant)
        self.components.add(proposition)

    def fixDisjunctions(self):
        """ generated source for method fixDisjunctions """
        fixList = ArrayList()
        for proposition in propositions.values():
            if proposition.getInputs().size() > 1:
                fixList.add(proposition)
        for fixItem in fixList:
            for input in fixItem.getInputs():
                i += 1
                if isinstance(, (GdlProposition, )):
                    disjunct = Proposition(GdlPool.getProposition(GdlPool.getConstant(proposition.__name__.getValue() + "-" + i)))
                else:
                    disjunct = Proposition(GdlPool.getRelation(GdlPool.getConstant(relation.__name__.getValue() + "-" + i), relation.getBody()))
                input.getOutputs().clear()
                link(input, disjunct)
                link(disjunct, or_)
                self.components.add(disjunct)
            fixItem.getInputs().clear()
            link(or_, fixItem)
            self.components.add(or_)

    def getProposition(self, sentence):
        """ generated source for method getProposition """
        if not self.propositions.containsKey(sentence):
            self.propositions.put(sentence, Proposition(sentence))
        return self.propositions.get(sentence)

    def link(self, source, target):
        """ generated source for method link """
        source.addOutput(target)
        target.addInput(source)

