#!/usr/bin/env python
""" generated source for module PropNetFlattener """
# package: org.ggp.base.util.propnet.factory.flattener
import java.util.ArrayList

import java.util.Collections

import java.util.HashMap

import java.util.HashSet

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.game.GameRepository

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlFunction

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import org.ggp.base.util.logging.GamerLogger

# 
#  * PropNetFlattener is an implementation of a GDL flattener using fixed-point
#  * analysis of the rules. This flattener works on many small and medium-sized
#  * games, but can fail on very large games.
#  *
#  * To use this class:
#  *      PropNetFlattener PF = new PropNetFlattener(description);
#  *      List<GdlRule> flatDescription = PF.flatten();
#  *      return converter.convert(flatDescription);
#  *
#  * @author Ethan Dreyfuss
#  * @author Sam Schreiber (comments)
#  
class PropNetFlattener(object):
    """ generated source for class PropNetFlattener """
    description = List()

    class Assignment(ArrayList, GdlConstant):
        """ generated source for class Assignment """
        serialVersionUID = 1L

    class Assignments(HashSet, Assignment):
        """ generated source for class Assignments """
        serialVersionUID = 1L

    class Index(HashMap, GdlConstant, Assignments):
        """ generated source for class Index """
        serialVersionUID = 1L

    class Condition(object):
        """ generated source for class Condition """
        def __init__(self, template):
            """ generated source for method __init__ """
            self.template = getConstantAndVariableList(template)
            key = findGenericForm(template)
            updateDom()

        def updateDom(self):
            """ generated source for method updateDom """
            if not domains.containsKey(key):
                dom = None
            else:
                dom = domains.get(key)

        template = List()
        dom = Domain()
        key = GdlTerm()

        def __str__(self):
            """ generated source for method toString """
            return self.template.__str__()

    class RuleReference(object):
        """ generated source for class RuleReference """
        productionTemplate = List()

        # The template from the rule head, contains only variables and constants
        conditions = ArrayList()

        # the conditions (right hand side of the rule)
        originalRule = Gdl()

        def __init__(self, originalRule):
            """ generated source for method __init__ """
            self.originalRule = originalRule

        def __str__(self):
            """ generated source for method toString """
            return "\n\tProduction: " + (self.productionTemplate.__str__() if self.productionTemplate != None else "null") + " conditions: " + (self.conditions.__str__() if self.conditions != None else "null")

        def equals(self, other):
            """ generated source for method equals """
            if not (isinstance(other, (self.RuleReference, ))):
                return False
            rhs = other
            return rhs.productionTemplate == self.productionTemplate and rhs.conditions == self.conditions

        def hashCode(self):
            """ generated source for method hashCode """
            return self.productionTemplate.hashCode() + self.conditions.hashCode()

    @SuppressWarnings("unused")
    class Domain(object):
        """ generated source for class Domain """
        def __init__(self, name, name2):
            """ generated source for method __init__ """
            self.name = name
            self.name2 = name2

        assignments = Assignments()
        indices = ArrayList()
        ruleRefs = HashSet()
        name = GdlTerm()
        name2 = GdlTerm()

        def __str__(self):
            """ generated source for method toString """
            return "\nName: " + self.name + "\nvalues: " + self.assignments
            # +"\nruleRefs: "+ruleRefs;

        def buildIndices(self):
            """ generated source for method buildIndices """
            for assignment in assignments:
                addAssignmentToIndex(assignment)
            for ruleRef in ruleRefs:
                for c in ruleRef.conditions:
                    if c.dom == None:
                        c.updateDom()
                    if c.dom != None:
                        newConditions.add(c)
                if len(newConditions) != len(ruleRef.conditions):
                    ruleRef.conditions = newConditions

        def addAssignmentToIndex(self, assignment):
            """ generated source for method addAssignmentToIndex """
            i = 0
            while i < len(assignment):
                if len(self.indices) <= i:
                    self.indices.add(self.Index())
                if not index.containsKey(c):
                    index.put(c, self.Assignments())
                val.add(assignment)
                i += 1

    fillerVar = GdlPool.getVariable("?#*#")
    domains = HashMap()
    extraRefs = ArrayList()

    def __init__(self, description):
        """ generated source for method __init__ """
        self.description = description

    def flatten(self):
        """ generated source for method flatten """
        # Find universe and initial domains
        for gdl in description:
            initializeDomains(gdl)
        for d in domains.values():
            d.buildIndices()
        # Compute the actual domains of everything
        updateDomains()
        # printDomains();
        # printDomainRefs();
        return getAllInstantiations()

    def getAllInstantiations(self):
        """ generated source for method getAllInstantiations """
        rval = ArrayList()
        for gdl in description:
            if isinstance(gdl, (GdlRelation, )):
                if name == "base":
                    continue 
                rval.add(GdlPool.getRule(relation))
        for d in domains.values():
            for r in d.ruleRefs:
                for varInstantiation in varInstantiations:
                    if varInstantiation.containsValue(None):
                        raise RuntimeException("Shouldn't instantiate anything to null.")
                    rval.add(getInstantiation(r.originalRule, varInstantiation))
                    if rval.get(len(rval) - 1).__str__().contains("null"):
                        raise RuntimeException("Shouldn't instantiate anything to null: " + rval.get(len(rval) - 1).__str__())
        for ruleRef in extraRefs:
            for c in ruleRef.conditions:
                if c.dom == None:
                    c.updateDom()
                if c.dom != None:
                    newConditions.add(c)
            if len(newConditions) != len(ruleRef.conditions):
                ruleRef.conditions = newConditions
        for r in extraRefs:
            for varInstantiation in varInstantiations:
                if varInstantiation.containsValue(None):
                    raise RuntimeException("Shouldn't instantiate anything to null.")
                rval.add(getInstantiation(r.originalRule, varInstantiation))
                if rval.get(len(rval) - 1).__str__().contains("null"):
                    raise RuntimeException("Shouldn't instantiate anything to null.")
            if len(varInstantiations) == 0:
                rval.add(getInstantiation(r.originalRule, HashMap()))
        return rval

    def getInstantiation(self, gdl, varInstantiation):
        """ generated source for method getInstantiation """
        instant = getInstantiationAux(gdl, varInstantiation)
        return instant

    def getInstantiationAux(self, gdl, varInstantiation):
        """ generated source for method getInstantiationAux """
        if isinstance(gdl, (GdlRelation, )):
            while i < relation.arity():
                body.add(self.getInstantiationAux(relation.get(i), varInstantiation))
                i += 1
            return GdlPool.getRelation(relation.__name__, body)
        elif isinstance(gdl, (GdlRule, )):
            while i < rule.arity():
                body.add(self.getInstantiationAux(rule.get(i), varInstantiation))
                i += 1
            return GdlPool.getRule(head, body)
        elif isinstance(gdl, (GdlDistinct, )):
            return GdlPool.getDistinct(arg1, arg2)
        elif isinstance(gdl, (GdlNot, )):
            return GdlPool.getNot(body)
        elif isinstance(gdl, (GdlOr, )):
            while i < or_.arity():
                body.add(self.getInstantiationAux(or_.get(i), varInstantiation))
                i += 1
            return GdlPool.getOr(body)
        elif isinstance(gdl, (GdlProposition, )):
            return gdl
        elif isinstance(gdl, (GdlConstant, )):
            return gdl
        elif isinstance(gdl, (GdlFunction, )):
            while i < func.arity():
                body.add(self.getInstantiationAux(func.get(i), varInstantiation))
                i += 1
            return GdlPool.getFunction(func.__name__, body)
        elif isinstance(gdl, (GdlVariable, )):
            return varInstantiation.get(variable)
        else:
            raise RuntimeException("Someone went and extended the GDL hierarchy without updating this code.")

    def initializeDomains(self, gdl):
        """ generated source for method initializeDomains """
        if isinstance(gdl, (GdlRelation, )):
            if not name == "base":
                if not self.domains.containsKey(generified):
                    self.domains.put(generified, self.Domain(generified, term))
                dom.assignments.add(instantiation)
        elif isinstance(gdl, (GdlRule, )):
            if isinstance(head, (GdlRelation, )):
                if not self.domains.containsKey(generified):
                    self.domains.put(generified, self.Domain(generified, term))
                for RHS in newRHSs:
                    ruleRef.productionTemplate = productionTemplate
                    for lit in RHS:
                        if isinstance(lit, (GdlSentence, )):
                            ruleRef.conditions.add(cond)
                    dom.ruleRefs.add(ruleRef)
            else:
                for RHS in newRHSs:
                    for lit in RHS:
                        if isinstance(lit, (GdlSentence, )):
                            ruleRef.conditions.add(cond)
                    self.extraRefs.add(ruleRef)

    def getConstantList(self, term):
        """ generated source for method getConstantList """
        rval = self.Assignment()
        if isinstance(term, (GdlConstant, )):
            rval.add(term)
            return rval
        elif isinstance(term, (GdlVariable, )):
            raise RuntimeException("Called getConstantList on something containing a variable.")
        func = term
        for t in func.getBody():
            rval.addAll(self.getConstantList(t))
        return rval

    def getConstantAndVariableList(self, term):
        """ generated source for method getConstantAndVariableList """
        rval = ArrayList()
        if isinstance(term, (GdlConstant, )):
            rval.add(term)
            return rval
        elif isinstance(term, (GdlVariable, )):
            rval.add(term)
            return rval
        func = term
        for t in func.getBody():
            rval.addAll(self.getConstantAndVariableList(t))
        return rval

    legalConst = GdlPool.getConstant("legal")
    trueConst = GdlPool.getConstant("true")
    doesConst = GdlPool.getConstant("does")
    nextConst = GdlPool.getConstant("next")
    initConst = GdlPool.getConstant("init")

    def findGenericForm(self, term):
        """ generated source for method findGenericForm """
        if isinstance(term, (GdlConstant, )):
            return self.fillerVar
        elif isinstance(term, (GdlVariable, )):
            return self.fillerVar
        func = term
        newBody = ArrayList()
        for t in func.getBody():
            newBody.add(self.findGenericForm(t))
        name = func.__name__
        if name == self.legalConst:
            name = self.doesConst
        elif name == self.nextConst:
            name = self.trueConst
        elif name == self.initConst:
            name = self.trueConst
        return GdlPool.getFunction(name, newBody)

    def deOr(self, rhs):
        """ generated source for method deOr """
        wrapped = ArrayList()
        wrapped.add(rhs)
        return deOr2(wrapped)

    def deOr2(self, rhsList):
        """ generated source for method deOr2 """
        rval = ArrayList()
        expandedSomething = False
        for rhs in rhsList:
            if not expandedSomething:
                for lit in rhs:
                    if not expandedSomething:
                        if len(expandedList) > 1:
                            for replacement in expandedList:
                                if not (isinstance(replacement, (GdlLiteral, ))):
                                    raise RuntimeException("Top level return value is different type of gdl.")
                                newRhs.set(i, newLit)
                                rval.add(newRhs)
                            expandedSomething = True
                            break
                    i += 1
                if not expandedSomething:
                    rval.add(rhs)
            else:
                rval.add(rhs)
        if not expandedSomething:
            return rhsList
        else:
            return self.deOr2(rval)

    def expandFirstOr(self, gdl):
        """ generated source for method expandFirstOr """
        rval = List()
        expandedChild = List()
        if isinstance(gdl, (GdlDistinct, )):
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlNot, )):
            expandedChild = self.expandFirstOr(not_.getBody())
            rval = ArrayList()
            for g in expandedChild:
                if not (isinstance(g, (GdlLiteral, ))):
                    raise RuntimeException("Not must have literal child.")
                rval.add(GdlPool.getNot(lit))
            return rval
        elif isinstance(gdl, (GdlOr, )):
            rval = ArrayList()
            while i < or_.arity():
                rval.add(or_.get(i))
                i += 1
            return rval
        elif isinstance(gdl, (GdlProposition, )):
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlRelation, )):
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlRule, )):
            raise RuntimeException("This should be used to remove 'or's from the body of a rule, and rules can't be nested")
        elif isinstance(gdl, (GdlConstant, )):
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlFunction, )):
            rval = ArrayList()
            rval.add(gdl)
            return rval
        elif isinstance(gdl, (GdlVariable, )):
            rval = ArrayList()
            rval.add(gdl)
            return rval
        else:
            raise RuntimeException("Uh oh, gdl hierarchy must have been extended without updating this code.")

    def updateDomains(self):
        """ generated source for method updateDomains """
        changedSomething = True
        itrNum = 0
        lastUpdatedDomains = HashSet(self.domains.values())
        while changedSomething:
            GamerLogger.log("StateMachine", "Beginning domain finding iteration: " + itrNum)
            changedSomething = False
            for d in domains.values():
                for ruleRef in d.ruleRefs:
                    for c in ruleRef.conditions:
                        if lastUpdatedDomains.contains(c.dom):
                            containsUpdatedDomain = True
                            break
                    if not containsUpdatedDomain:
                        continue 
                    rulesConsidered += 1
                    for instantiation in instantiations:
                        for t in ruleRef.productionTemplate:
                            if isinstance(t, (GdlConstant, )):
                                a.add(t)
                            else:
                                a.add(instantiation.get(var))
                        if not d.assignments.contains(a):
                            currUpdatedDomains.add(d)
                            d.assignments.add(a)
                            changedSomething = True
                            d.addAssignmentToIndex(a)
                    if len(instantiations) == 0:
                        findSatisfyingInstantiations(ruleRef)
                        for t in ruleRef.productionTemplate:
                            if isinstance(t, (GdlConstant, )):
                                a.add(t)
                            else:
                                isVar = True
                                break
                        if not isVar and not d.assignments.contains(a):
                            currUpdatedDomains.add(d)
                            d.assignments.add(a)
                            changedSomething = True
                            d.addAssignmentToIndex(a)
            itrNum += 1
            lastUpdatedDomains = currUpdatedDomains
            GamerLogger.log("StateMachine", "\tDone with iteration.  Considered " + rulesConsidered + " rules.")

    @overloaded
    def findSatisfyingInstantiations(self, ruleRef):
        """ generated source for method findSatisfyingInstantiations """
        emptyInstantiation = HashMap()
        return self.findSatisfyingInstantiations(ruleRef.conditions, 0, emptyInstantiation)

    @findSatisfyingInstantiations.register(object, List, int, Map)
    def findSatisfyingInstantiations_0(self, conditions, idx, instantiation):
        """ generated source for method findSatisfyingInstantiations_0 """
        rval = HashSet()
        if idx == len(conditions):
            rval.add(instantiation)
            return rval
        cond = conditions.get(idx)
        dom = cond.dom
        assignments = None
        i = 0
        while i < len(cond.template):
            if isinstance(t, (GdlVariable, )):
                if instantiation.containsKey(v):
                    c = instantiation.get(v)
            elif isinstance(t, (GdlConstant, )):
                c = t
            if c != None:
                if assignments == None:
                    assignments = self.Assignments()
                    if len(dom.indices) > i:
                        if index.containsKey(c):
                            assignments.addAll(index.get(c))
                else:
                    if len(dom.indices) > i:
                        if index.containsKey(c):
                            assignments.retainAll(index.get(c))
                    else:
                        assignments.clear()
            i += 1
        if assignments == None:
            assignments = dom.assignments
        for a in assignments:
            while i < len(a):
                if isinstance(t, (GdlVariable, )):
                    if not instantiation.containsKey(var):
                        newInstantiation.put(var, a.get(i))
                i += 1
            rval.addAll(self.findSatisfyingInstantiations(conditions, idx + 1, newInstantiation))
        return rval

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        description = GameRepository.getDefaultRepository().getGame("conn4").getRules()
        flattener = PropNetFlattener(description)
        flattened = flattener.flatten()
        print "Flattened description for connect four contains: \n" + len(flattened) + "\n\n"
        strings = ArrayList()
        for rule in flattened:
            strings.add(rule.__str__())
        Collections.sort(strings)
        for s in strings:
            print s


if __name__ == '__main__':
    import sys
    PropNetFlattener.main(sys.argv)

