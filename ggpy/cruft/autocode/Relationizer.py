#!/usr/bin/env python
""" generated source for module Relationizer """
# package: org.ggp.base.util.gdl.transforms
import java.util.ArrayList

import java.util.HashSet

import java.util.List

import java.util.Set

import org.ggp.base.util.gdl.GdlUtils

import org.ggp.base.util.gdl.grammar.Gdl

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlDistinct

import org.ggp.base.util.gdl.grammar.GdlLiteral

import org.ggp.base.util.gdl.grammar.GdlNot

import org.ggp.base.util.gdl.grammar.GdlOr

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlRule

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.gdl.model.SentenceForm

import org.ggp.base.util.gdl.model.SentenceFormModel

import org.ggp.base.util.gdl.model.SentenceFormModelFactory

class Relationizer(object):
    """ generated source for class Relationizer """
    # 
    # 	 * Searches the description for statements that are needlessly treated as
    # 	 * base propositions when they could be expressed as simple relations, and
    # 	 * replaces them with these simpler forms.
    # 	 *
    # 	 * Some games have been written such that unchanging facts of the game
    # 	 * are listed as base propositions. Often, this is so the fact can be
    # 	 * accessed by a visualization. Gamers usually don't need this distinction,
    # 	 * and can reduce the costs in time and memory of processing the game if
    # 	 * these statements are instead transformed into sentences.
    # 	 * @throws InterruptedException
    # 	 
    @classmethod
    def run(cls, description):
        """ generated source for method run """
        model = SentenceFormModelFactory.create(description)
        NEXT = GdlPool.getConstant("next")
        nextFormsToReplace = ArrayList()
        # Find the update rules for each "true" statement
        for nextForm in model.getSentenceForms():
            if nextForm.__name__ == NEXT:
                # See if there is exactly one update rule, and it is the persistence rule
                if len(rules) == 1:
                    # Persistence rule: Exactly one literal, the "true" form of the sentence
                    if rule.arity() == 1:
                        if isinstance(literal, (GdlRelation, )):
                            # Check that it really is the true form
                            if trueForm.matches(literal):
                                # Check that the tuples are the same, and that they
                                # consist of distinct variables
                                if headTuple == bodyTuple:
                                    # Distinct variables?
                                    if len(vars) == len(headTuple):
                                        nextFormsToReplace.add(nextForm)
        newDescription = ArrayList(description)
        # Now, replace the next forms
        for nextForm in nextFormsToReplace:
            # Go through the rules and relations, making replacements as needed
            while i < len(newDescription):
                if isinstance(gdl, (GdlRelation, )):
                    # Replace initForm
                    if initForm.matches(relation):
                        newDescription.set(i, newSentence)
                elif isinstance(gdl, (GdlRule, )):
                    # Remove persistence rule (i.e. rule with next form as head)
                    if nextForm.matches(head):
                        newDescription.remove(i)
                        i -= 1
                    else:
                        # Replace true in bodies of rules with relation-only form
                        if not body == newBody:
                            newDescription.set(i, newRule)
                i += 1
        return newDescription

    @classmethod
    def replaceRelationInBody(cls, body, trueForm):
        """ generated source for method replaceRelationInBody """
        newBody = ArrayList()
        for literal in body:
            newBody.add(replaceRelationInLiteral(literal, trueForm))
        return newBody

    @classmethod
    def replaceRelationInLiteral(cls, literal, trueForm):
        """ generated source for method replaceRelationInLiteral """
        if isinstance(literal, (GdlSentence, )):
            if trueForm.matches(sentence):
                # Replace with the sentence contained in the true sentence...
                return sentence.get(0).toSentence()
            else:
                return literal
        elif isinstance(literal, (GdlNot, )):
            return GdlPool.getNot(cls.replaceRelationInLiteral(not_.getBody(), trueForm))
        elif isinstance(literal, (GdlOr, )):
            while i < or_.arity():
                pass
                i += 1
            return GdlPool.getOr(newOrBody)
        elif isinstance(literal, (GdlDistinct, )):
            return literal
        else:
            raise RuntimeException("Unanticipated GDL literal type " + literal.__class__ + " encountered in Relationizer")

