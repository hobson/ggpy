package org.ggp.base.util.gdl

import java.util.ArrayList
import java.util.Collection
import java.util.Collections
import java.util.HashMap
import java.util.HashSet
import java.util.List
import java.util.Map
import java.util.Set

import org.ggp.base.util.gdl.grammar.Gdl
import org.ggp.base.util.gdl.grammar.GdlConstant
import org.ggp.base.util.gdl.grammar.GdlDistinct
import org.ggp.base.util.gdl.grammar.GdlFunction
import org.ggp.base.util.gdl.grammar.GdlLiteral
import org.ggp.base.util.gdl.grammar.GdlNot
import org.ggp.base.util.gdl.grammar.GdlOr
import org.ggp.base.util.gdl.grammar.GdlProposition
import org.ggp.base.util.gdl.grammar.GdlRule
import org.ggp.base.util.gdl.grammar.GdlSentence
import org.ggp.base.util.gdl.grammar.GdlTerm
import org.ggp.base.util.gdl.grammar.GdlVariable


class GdlUtils(object):
	//TODO (AL): Check if we can switch over to just having this return a set.
    def static List<GdlVariable> getVariables(Gdl gdl):
        final List<GdlVariable> variablesList = new ArrayList<GdlVariable>()
        final Set<GdlVariable> variables = new HashSet<GdlVariable>()
        GdlVisitors.visitAll(gdl, new GdlVisitor():
        		    def void visitVariable(GdlVariable variable):
                if (!variables.contains(variable)):
                    variablesList.add(variable)
                    variables.add(variable)
		})
        return variablesList

    def static List<String> getVariableNames(Gdl gdl):
        List<GdlVariable> variables = getVariables(gdl)
        List<String> variableNames = new ArrayList<String>()
        for (GdlVariable variable : variables):
            variableNames.add(variable.getName())
        return variableNames

    def static List<GdlSentence> getSentencesInRuleBody(GdlRule rule):
        List<GdlSentence> result = new ArrayList<GdlSentence>()
        for(GdlLiteral literal : rule.getBody()):
            addSentencesInLiteral(literal, result)
        return result

    def void addSentencesInLiteral(GdlLiteral literal,
            Collection<GdlSentence> sentences):
        if(literal instanceof GdlSentence):
            sentences.add((GdlSentence) literal)
		elif(literal instanceof GdlNot):
            GdlNot not = (GdlNot) literal
            addSentencesInLiteral(not.getBody(), sentences)
		elif(literal instanceof GdlOr):
            GdlOr or = (GdlOr) literal
            for(int i = 0; i < or.arity(); i++)
                addSentencesInLiteral(or.get(i), sentences)
		elif(!(literal instanceof GdlDistinct)):
            throw new RuntimeException("Unexpected GdlLiteral type encountered: " + literal.getClass().getSimpleName())

    def static List<GdlTerm> getTupleFromSentence(
            GdlSentence sentence):
        if(sentence instanceof GdlProposition)
            return Collections.emptyList()

		//A simple crawl through the sentence.
        List<GdlTerm> tuple = new ArrayList<GdlTerm>()
        try 
            addBodyToTuple(sentence.getBody(), tuple)
		} catch(RuntimeException e):
            throw new RuntimeException(e.getMessage() + "\nSentence was " + sentence)
        return tuple
    def void addBodyToTuple(List<GdlTerm> body, List<GdlTerm> tuple):
        for(GdlTerm term : body):
            if(term instanceof GdlConstant):
                tuple.add(term)
			elif(term instanceof GdlVariable):
                tuple.add(term)
			elif(term instanceof GdlFunction)
                GdlFunction function = (GdlFunction) term
                addBodyToTuple(function.getBody(), tuple)
			else:
                throw new RuntimeException("Unforeseen Gdl tupe in SentenceModel.addBodyToTuple()")

    def static List<GdlConstant> getTupleFromGroundSentence(
            GdlSentence sentence):
        if(sentence instanceof GdlProposition)
            return Collections.emptyList()

		//A simple crawl through the sentence.
        List<GdlConstant> tuple = new ArrayList<GdlConstant>()
        try 
            addBodyToGroundTuple(sentence.getBody(), tuple)
		} catch(RuntimeException e):
            throw new RuntimeException(e.getMessage() + "\nSentence was " + sentence)
        return tuple
    def void addBodyToGroundTuple(List<GdlTerm> body, List<GdlConstant> tuple):
        for(GdlTerm term : body):
            if(term instanceof GdlConstant):
                tuple.add((GdlConstant) term)
			elif(term instanceof GdlVariable):
                throw new RuntimeException("Asking for a ground tuple of a non-ground sentence")
			elif(term instanceof GdlFunction)
                GdlFunction function = (GdlFunction) term
                addBodyToGroundTuple(function.getBody(), tuple)
			else:
                throw new RuntimeException("Unforeseen Gdl tupe in SentenceModel.addBodyToTuple()")

    def static Map<GdlVariable, GdlConstant> getAssignmentMakingLeftIntoRight(
            GdlSentence left, GdlSentence right):
        Map<GdlVariable, GdlConstant> assignment = new HashMap<GdlVariable, GdlConstant>()
        if(!left.getName().equals(right.getName()))
            return null
        if(left.arity() != right.arity())
            return null
        if(left.arity() == 0)
            return Collections.emptyMap()
        if(!fillAssignmentBody(assignment, left.getBody(), right.getBody()))
            return null
        return assignment

    def bool fillAssignmentBody(
            Map<GdlVariable, GdlConstant> assignment, List<GdlTerm> leftBody,
            List<GdlTerm> rightBody):
		//left body contains variables; right body shouldn't
        if(leftBody.size() != rightBody.size()):
            return false
        for(int i = 0; i < leftBody.size(); i++):
            GdlTerm leftTerm = leftBody.get(i)
            GdlTerm rightTerm = rightBody.get(i)
            if(leftTerm instanceof GdlConstant):
                if(!leftTerm.equals(rightTerm)):
                    return false
			elif(leftTerm instanceof GdlVariable):
                if(assignment.containsKey(leftTerm)):
                    if(!assignment.get(leftTerm).equals(rightTerm)):
                        return false
				else:
                    if(!(rightTerm instanceof GdlConstant)):
                        return false
                    assignment.put((GdlVariable)leftTerm, (GdlConstant)rightTerm)
			elif(leftTerm instanceof GdlFunction):
                if(!(rightTerm instanceof GdlFunction))
                    return false
                GdlFunction leftFunction = (GdlFunction) leftTerm
                GdlFunction rightFunction = (GdlFunction) rightTerm
                if(!leftFunction.getName().equals(rightFunction.getName()))
                    return false
                if(!fillAssignmentBody(assignment, leftFunction.getBody(), rightFunction.getBody()))
                    return false
        return true

    def static bool containsTerm(GdlSentence sentence, GdlTerm term):
        if(sentence instanceof GdlProposition)
            return false
        return containsTerm(sentence.getBody(), term)

    def bool containsTerm(List<GdlTerm> body, GdlTerm term):
        for(GdlTerm curTerm : body):
            if(curTerm.equals(term))
                return true
            if(curTerm instanceof GdlFunction):
                if(containsTerm(((GdlFunction) curTerm).getBody(), term))
                    return true
        return false

