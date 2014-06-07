#!/usr/bin/env python
""" generated source for module SentenceDomainModels """
# package: org.ggp.base.util.gdl.model
import java.util.Collection

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.grammar.GdlVariable

import com.google.common.base.Function

import com.google.common.collect.ArrayListMultimap

import com.google.common.collect.ImmutableList

import com.google.common.collect.ImmutableMap

import com.google.common.collect.Iterables

import com.google.common.collect.Maps

import com.google.common.collect.Multimap

import com.google.common.collect.Sets

class SentenceDomainModels(object):
    """ generated source for class SentenceDomainModels """
    class VarDomainOpts:
        """ generated source for enum VarDomainOpts """
        INCLUDE_HEAD = u'INCLUDE_HEAD'
        BODY_ONLY = u'BODY_ONLY'

    @classmethod
    def getVarDomains(cls, rule, domainModel, includeHead):
        """ generated source for method getVarDomains """
        #  For each positive definition of sentences in the rule, intersect their
        #  domains everywhere the variables show up
        varDomainsByVar = ArrayListMultimap.create()
        for literal in getSentences(rule, includeHead):
            if isinstance(literal, (GdlSentence, )):
                while i < len(tuple_):
                    if isinstance(term, (GdlVariable, )):
                        varDomainsByVar.put(var, domain)
                    i += 1
        varDomainByVar = combineDomains(varDomainsByVar)
        return varDomainByVar

    @classmethod
    def getSentences(cls, rule, includeHead):
        """ generated source for method getSentences """
        if includeHead == cls.VarDomainOpts.INCLUDE_HEAD:
            return Iterables.concat(ImmutableList.of(rule.getHead()), rule.getBody())
        else:
            return rule.getBody()

    @classmethod
    def combineDomains(cls, varDomainsByVar):
        """ generated source for method combineDomains """
        return ImmutableMap.copyOf(Maps.transformValues(varDomainsByVar.asMap(), Function()))

    @classmethod
    def intersectSets(cls, input):
        """ generated source for method intersectSets """
        if input.isEmpty():
            raise IllegalArgumentException("Can't take an intersection of no sets")
        result = None
        for set in input:
            if result == None:
                result = Sets.newHashSet(set)
            else:
                result.retainAll(set)
        assert result != None
        return result

