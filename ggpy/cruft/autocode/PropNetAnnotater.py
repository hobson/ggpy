#!/usr/bin/env python
""" generated source for module PropNetAnnotater """
# package: org.ggp.base.util.propnet.factory.annotater
import java.math.BigInteger

import java.text.Collator

import java.util.ArrayList

import java.util.Collections

import java.util.Comparator

import java.util.HashMap

import java.util.HashSet

import java.util.List

import java.util.Objects

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

# 
#  * Annotater generates ( base ?x ) annotations that explicitly specify the
#  * domains of the propositions in a game. This only works on some relatively
#  * simple games, unfortunately.
#  *
#  * @author Ethan Dreyfuss
#  
class PropNetAnnotater(object):
    """ generated source for class PropNetAnnotater """
    description = List()

    #   private List<GdlRelation> relations = new ArrayList<GdlRelation>();
    baseRelations = HashSet()
    universe = HashSet()
    universalDom = None

    class Domain(object):
        """ generated source for class Domain """
        def __init__(self, loc):
            """ generated source for method __init__ """
            self.loc = loc

        values = HashSet()
        functionRefs = HashSet()
        loc = Location()

        def __str__(self):
            """ generated source for method toString """
            return "Name: " + self.loc.name + " index: " + self.loc.idx + "\nvalues: " + self.values + "\nfunctionRefs: " + self.functionRefs

    class Location(object):
        """ generated source for class Location """
        name = GdlConstant()
        idx = int()

        @overloaded
        def __init__(self):
            """ generated source for method __init__ """

        @SuppressWarnings("unused")
        @__init__.register(object, self.Location)
        def __init___0(self, other):
            """ generated source for method __init___0 """
            self.name = other.name
            self.idx = other.idx

        def equals(self, other):
            """ generated source for method equals """
            if not (isinstance(other, (self.Location, ))):
                return False
            rhs = other
            return Objects == self.idx, rhs.idx and self.name.__str__() == rhs.name.__str__()

        def hashCode(self):
            """ generated source for method hashCode """
            bytes = self.name.__str__().getBytes()
            bigInt = BigInteger(bytes)
            val = bigInt.bitCount() + bigInt.intValue()
            return val + self.idx

        def __str__(self):
            """ generated source for method toString """
            return self.name.__str__() + "(" + self.idx + ")"

    domains = HashMap()

    def __init__(self, description):
        """ generated source for method __init__ """
        self.description = description

    def getAnnotations(self):
        """ generated source for method getAnnotations """
        # Find universe and initial domains
        for gdl in description:
            processGdl(gdl, None)
            processDomain(gdl)
        # Compute the actual domains of everything
        updateDomains()
        # printDomains();
        # printDomainRefs();
        # Compute function corresponding to universal set for insertion in baseprops
        body = ArrayList()
        body.addAll(self.universe)
        self.universalDom = GdlPool.getFunction(GdlPool.getConstant("thing"), body)
        # Find next/init things and use them to instantiate base props
        for gdl in description:
            findAndInstantiateBaseProps(gdl)
        self.baseRelations = mergeBaseRelations(self.baseRelations)
        # Return the results
        rval = ArrayList()
        rval.addAll(self.baseRelations)
        return rval

    def mergeBaseRelations(self, rels):
        """ generated source for method mergeBaseRelations """
        merges = HashMap()
        for rel in rels:
            if not merges.containsKey(name):
                merges.put(name, ArrayList())
            addRelToMerge(rel, merge)
        rval = HashSet()
        valConst = GdlPool.getConstant("val")
        for c in merges.keySet():
            body.add(c)
            for mergeSet in merge:
                Collections.sort(ms2, SortTerms())
                body.add(GdlPool.getFunction(valConst, ms2))
            rval.add(toAdd)
        return rval

    class SortTerms(Comparator, GdlTerm):
        """ generated source for class SortTerms """
        def compare(self, arg0, arg1):
            """ generated source for method compare """
            a1 = arg0
            a2 = arg1
            s1 = a1.__str__()
            s2 = a2.__str__()
            num1 = -1
            num2 = -1
            try:
                num1 = Integer.parseInt(s1)
            except Exception as ex:
                pass
            try:
                num2 = Integer.parseInt(s2)
            except Exception as ex:
                pass
            if num1 == -1 and num2 == -1:
                return Collator.getInstance().compare(s1, s2)
            if num1 == -1:
                return 1
            if num2 == -1:
                return -1
            return num1 - num2

    def addRelToMerge(self, rel, merge):
        """ generated source for method addRelToMerge """
        i = 1
        while i < rel.arity():
            if not (isinstance(t, (GdlFunction, ))):
                raise RuntimeException("Incorrectly constructed base props")
            if len(merge) < i:
                merge.add(HashSet())
            for t2 in f.getBody():
                if not (isinstance(t2, (GdlConstant, ))):
                    raise RuntimeException("Incorrectly constructed base props: something other than a constant")
                dom.add(t2)
            i += 1

    def printDomains(self):
        """ generated source for method printDomains """
        print "Domains: "
        for loc in domains.keySet():
            print "\t" + loc
            for val in d.values:
                print "\t\t" + val

    def printDomainRefs(self):
        """ generated source for method printDomainRefs """
        print "Domains refs: "
        for loc in domains.keySet():
            print "\t" + loc
            for domSet in d.functionRefs:
                print "\t\t|"
                for d2 in domSet:
                    if d2 != None:
                        print "\t\t+" + d2.loc

    def processGdl(self, gdl, parent):
        """ generated source for method processGdl """
        if isinstance(gdl, (GdlRelation, )):
            if not name == "base":
                for gdl2 in relation.getBody():
                    self.processGdl(gdl2, relation.__name__)
        elif isinstance(gdl, (GdlRule, )):
            for gdl2 in rule.getBody():
                self.processGdl(gdl2, None)
        elif isinstance(gdl, (GdlConstant, )):
            self.universe.add(gdl)
        elif isinstance(gdl, (GdlFunction, )):
            for gdl2 in func.getBody():
                self.processGdl(gdl2, func.__name__)
        elif isinstance(gdl, (GdlDistinct, )):
            self.processGdl(distinct.getArg1(), None)
            self.processGdl(distinct.getArg2(), None)
        elif isinstance(gdl, (GdlNot, )):
            self.processGdl(not_.getBody(), None)
        elif isinstance(gdl, (GdlOr, )):
            while i < or_.arity():
                pass
                i += 1
        elif isinstance(gdl, (GdlProposition, )):
            # IGNORE
        elif isinstance(gdl, (GdlVariable, )):
            # IGNORE

    baseConstant = GdlPool.getConstant("base")

    def findAndInstantiateBaseProps(self, gdl):
        """ generated source for method findAndInstantiateBaseProps """
        if isinstance(gdl, (GdlRelation, )):
            if name == "init":
                if relation.arity() != 1:
                    raise RuntimeException("Can't init more than one thing as far as I know.")
                if isinstance(template, (GdlConstant, )):
                    body.add(template)
                    self.baseRelations.add(toAdd)
                    System.err.println("Weird init of constant")
                elif isinstance(template, (GdlVariable, )):
                    System.err.println("Weird init of constant")
                    body.add(self.universalDom)
                    self.baseRelations.add(toAdd)
                    System.err.println("Weird init of variable")
                elif isinstance(template, (GdlFunction, )):
                    instantiateBaseProps(func.toSentence())
        elif isinstance(gdl, (GdlRule, )):
            if name == "next":
                if head.arity() != 1:
                    raise RuntimeException("Can't next more than one thing as far as I know.")
                if isinstance(, (GdlVariable, )):
                    # weird case where you have rule like (next ?q)
                    l.idx = 0
                    l.name = head.__name__
                    for c in dom.values:
                        body.add(c)
                        self.baseRelations.add(GdlPool.getRelation(self.baseConstant, body))
                else:
                    instantiateBasePropsWithRHS(head.get(0).toSentence(), rule.getBody())

    def instantiateBaseProps(self, template):
        """ generated source for method instantiateBaseProps """
        body = ArrayList()
        body.add(template.__name__)
        i = 0
        while i < template.arity():
            if isinstance(arg, (GdlConstant, )):
                domBody.add(arg)
                body.add(dom)
            elif isinstance(arg, (GdlVariable, )):
                loc.idx = i
                loc.name = template.__name__
                if varDom == None:
                    raise RuntimeException("Unexpected domain: " + loc + " encountered.")
                domBody.addAll(varDom.values)
                body.add(dom)
            elif isinstance(arg, (GdlFunction, )):
                raise RuntimeException("Don't know how to deal with functions within next/init.")
            i += 1
        toAdd = GdlPool.getRelation(self.baseConstant, body)
        self.baseRelations.add(toAdd)

    def processDomain(self, gdl):
        """ generated source for method processDomain """
        if isinstance(gdl, (GdlRelation, )):
            if not name == "base":
                addDomain(relation)
        elif isinstance(gdl, (GdlRule, )):
            if isinstance(head, (GdlRelation, )):
                for term in rel.getBody():
                    addDomain2(term, rel.__name__, i, rule.getBody())
                    i += 1
            elif isinstance(head, (GdlProposition, )):
                #               GdlProposition prop = (GdlProposition)head;
                # addDomain2(prop.toTerm(), prop.__name__, 0, rule.getBody());
            else:
                raise RuntimeException("Don't know how to deal with this.")

    def addDomain2(self, term, name, idx, RHS):
        """ generated source for method addDomain2 """
        loc = self.Location()
        loc.name = name
        loc.idx = idx
        if not self.domains.containsKey(loc):
            self.domains.put(loc, self.Domain(loc))
        dom = self.domains.get(loc)
        if isinstance(term, (GdlConstant, )):
            dom.values.add(constant)
        elif isinstance(term, (GdlFunction, )):
            for t2 in func.getBody():
                self.addDomain2(t2, func.__name__, i, RHS)
                i += 1
        elif isinstance(term, (GdlVariable, )):
            dom.functionRefs.add(occuranceList)

    @overloaded
    def findAllInstancesOf(self, var, RHS):
        """ generated source for method findAllInstancesOf """
        rval = HashSet()
        for literal in RHS:
            rval.addAll(self.findAllInstancesOf(var, literal))
        return rval

    @findAllInstancesOf.register(object, GdlVariable, GdlLiteral)
    def findAllInstancesOf_0(self, var, literal):
        """ generated source for method findAllInstancesOf_0 """
        return self.findAllInstancesOf(var, literal, None)

    @findAllInstancesOf.register(object, GdlVariable, Gdl, self.Location)
    def findAllInstancesOf_1(self, var, gdl, loc):
        """ generated source for method findAllInstancesOf_1 """
        if not self.domains.containsKey(loc):
            self.domains.put(loc, self.Domain(loc))
        rval = HashSet()
        if isinstance(gdl, (GdlRelation, )):
            while i < relation.arity():
                parent.name = relation.__name__
                parent.idx = i
                rval.addAll(self.findAllInstancesOf(var, relation.get(i), parent))
                i += 1
        elif isinstance(gdl, (GdlDistinct, )):
            #           GdlDistinct distinct = (GdlDistinct)gdl;
            # Negative context, ignore it for now
        elif isinstance(gdl, (GdlNot, )):
            #           GdlNot not = (GdlNot)gdl;
            # Negative context, ignore it for now
        elif isinstance(gdl, (GdlOr, )):
            # TODO: check that this is right, I think it may not be
            while i < or_.arity():
                pass
                i += 1
        elif isinstance(gdl, (GdlProposition, )):
            #           GdlProposition prop = (GdlProposition)gdl;
            # I think these can safely be ignored, they have no body
        elif isinstance(gdl, (GdlConstant, )):
            #           GdlConstant constant = (GdlConstant)gdl;
            # Just a constant
        elif isinstance(gdl, (GdlFunction, )):
            while i < func.arity():
                parent.name = func.__name__
                parent.idx = i
                rval.addAll(self.findAllInstancesOf(var, func.get(i), parent))
                i += 1
        elif isinstance(gdl, (GdlVariable, )):
            # This is the interesting one
            if variable == var:
                # Found what we're looking for (base case of recursion)
                if loc == None:
                    raise RuntimeException("Parent missing for a variable.")
                rval.add(self.domains.get(loc))
        elif isinstance(gdl, (GdlRule, )):
            raise RuntimeException("Shouldn't nest rules.")
        return rval

    @overloaded
    def addDomain(self, relation):
        """ generated source for method addDomain """
        i = 0
        for term in relation.getBody():
            loc.idx = i
            loc.name = relation.__name__
            self.addDomain(term, loc)
            i += 1

    @addDomain.register(object, GdlTerm, self.Location)
    def addDomain_0(self, term, loc):
        """ generated source for method addDomain_0 """
        if not self.domains.containsKey(loc):
            self.domains.put(loc, self.Domain(loc))
        doms = self.domains.get(loc)
        if isinstance(term, (GdlConstant, )):
            doms.values.add(term)
        elif isinstance(term, (GdlFunction, )):
            for newTerm in func.getBody():
                loc2.idx = j
                loc2.name = func.__name__
                self.addDomain(newTerm, loc2)
                j += 1
        elif isinstance(term, (GdlVariable, )):
            raise RuntimeException("Uh oh, unbound variable which I don't know how to deal with.")

    def updateDomains(self):
        """ generated source for method updateDomains """
        changedSomething = True
        while changedSomething:
            changedSomething = False
            for d in domains.values():
                for intSet in d.functionRefs:
                    for d2 in intSet:
                        if d2 != None:
                            if domain == None:
                                domain = HashSet(d2.values)
                            else:
                                domain.retainAll(d2.values)
                    if domain != None:
                        d.values.addAll(domain)
                if d.loc != None:
                    if name == "does":
                        newLoc.name = GdlPool.getConstant("legal")
                        newLoc.idx = d.loc.idx
                        if otherDom == None:
                            raise RuntimeException("Uh oh, missed a legal")
                        d.values.addAll(otherDom.values)
                    elif name == "true":
                        newLoc.name = GdlPool.getConstant("next")
                        newLoc.idx = d.loc.idx
                        if otherDom == None:
                            raise RuntimeException("Uh oh, missed a next")
                        d.values.addAll(otherDom.values)
                if len(d.values) != before:
                    changedSomething = True

    def instantiateBasePropsWithRHS(self, template, RHS):
        """ generated source for method instantiateBasePropsWithRHS """
        self.instantiateBaseProps(template)

    def getAugmentedDescription(self):
        """ generated source for method getAugmentedDescription """
        rval = ArrayList()
        for gdl in description:
            if isinstance(gdl, (GdlRelation, )):
                if rel.__name__.__str__() == "base":
                    notBase = False
            if notBase:
                rval.add(gdl)
        rval.addAll(self.getAnnotations())
        return rval

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        description = GameRepository.getDefaultRepository().getGame("conn4").getRules()
        aa = PropNetAnnotater(description)
        print "Annotations for connect four are: \n" + aa.getAnnotations()


if __name__ == '__main__':
    import sys
    PropNetAnnotater.main(sys.argv)

