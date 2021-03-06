package org.ggp.base.util.reasoner.gdl

import java.util.Collection
import java.util.Map
import java.util.Map.Entry
import java.util.Set

import org.ggp.base.util.concurrency.ConcurrencyUtils
import org.ggp.base.util.gdl.GdlUtils
import org.ggp.base.util.gdl.grammar.GdlConstant
import org.ggp.base.util.gdl.grammar.GdlDistinct
import org.ggp.base.util.gdl.grammar.GdlLiteral
import org.ggp.base.util.gdl.grammar.GdlNot
import org.ggp.base.util.gdl.grammar.GdlOr
import org.ggp.base.util.gdl.grammar.GdlRule
import org.ggp.base.util.gdl.grammar.GdlSentence
import org.ggp.base.util.gdl.grammar.GdlVariable
import org.ggp.base.util.gdl.model.SentenceDomainModel
import org.ggp.base.util.gdl.model.SentenceDomainModels
import org.ggp.base.util.gdl.model.SentenceDomainModels.VarDomainOpts
import org.ggp.base.util.gdl.model.SentenceForm
import org.ggp.base.util.gdl.model.SentenceFormModel
import org.ggp.base.util.gdl.model.assignments.AddibleFunctionInfo
import org.ggp.base.util.gdl.model.assignments.AssignmentIterator
import org.ggp.base.util.gdl.model.assignments.Assignments
import org.ggp.base.util.gdl.model.assignments.AssignmentsImpl
import org.ggp.base.util.gdl.model.assignments.FunctionInfo
import org.ggp.base.util.gdl.transforms.CommonTransforms
import org.ggp.base.util.reasoner.DifferentialForwardChainingReasoner

import com.google.common.collect.ImmutableMultimap
import com.google.common.collect.SetMultimap

/**
 * An implementation of a ForwardChainingReasoner that uses Gdl objects
 * directly and allows for differential processing of rules.
 */
class GdlChainingReasoner implements
        DifferentialForwardChainingReasoner<GdlRule, GdlSentenceSet> 
    model = SentenceFormModel()
    private final ImmutableMultimap<SentenceForm, GdlSentence> constants

    private GdlChainingReasoner(SentenceFormModel model, ImmutableMultimap<SentenceForm, GdlSentence> constants):
        self.model = model
        self.constants = constants

    def static GdlChainingReasoner create(SentenceFormModel model):
        ImmutableMultimap.Builder<SentenceForm, GdlSentence> constantsBuilder = ImmutableMultimap.builder()
        for (SentenceForm form : model.getSentenceForms()):
            constantsBuilder.putAll(form, model.getSentencesListedAsTrue(form))
        return new GdlChainingReasoner(model, constantsBuilder.build())

    def getConstantSentences():  # GdlSentenceSet
        return GdlSentenceSet.create(constants)

    def GdlSentenceSet getRuleResults(GdlRule rule,
            SentenceDomainModel domainModel,
            GdlSentenceSet sentencesSoFar) throws InterruptedException 
        ConcurrencyUtils.checkForInterruption()
        SentenceForm headForm = model.getSentenceForm(rule.getHead())
        Map<GdlVariable, Set<GdlConstant>> varDomains = SentenceDomainModels.getVarDomains(rule, domainModel, VarDomainOpts.INCLUDE_HEAD)
        Map<SentenceForm, ?(FunctionInfo> functionInfoMap = sentencesSoFar.getFunctionInfo();):
        Map<SentenceForm, ?(Collection<GdlSentence>> completedSentenceFormValues = sentencesSoFar.getSentences().asMap();):

        AssignmentsImpl assignments = new AssignmentsImpl(rule, varDomains, functionInfoMap, completedSentenceFormValues)
        AssignmentIterator asnItr = assignments.getIterator()
        GdlSentenceSet sentencesToAdd = GdlSentenceSet.create()
        while (asnItr.hasNext()):
            Map<GdlVariable, GdlConstant> assignment = asnItr.next()
            bool allSatisfied = true
            for (GdlLiteral literal : rule.getBody()):
                ConcurrencyUtils.checkForInterruption()
                if (!satisfies(assignment, literal, sentencesSoFar.getSentences())):
                    asnItr.changeOneInNext(GdlUtils.getVariables(literal), assignment)
                    allSatisfied = false
                    break
            if (allSatisfied):
                GdlSentence head = rule.getHead()
                sentencesToAdd.put(headForm, CommonTransforms.replaceVariables(head, assignment))
                asnItr.changeOneInNext(GdlUtils.getVariables(head), assignment)
        return sentencesToAdd

    private bool satisfies(Map<GdlVariable, GdlConstant> assignment,
            GdlLiteral literal, SetMultimap<SentenceForm, GdlSentence> sentencesSoFar):
        if (literal instanceof GdlSentence):
            return satisfiesSentence(assignment, (GdlSentence) literal, sentencesSoFar)
		elif (literal instanceof GdlNot):
            GdlLiteral body = ((GdlNot) literal).getBody()
            if (!(body instanceof GdlSentence)):
                throw new IllegalStateException("Negated literal should be a sentence but isn't: " + body)
            return !satisfiesSentence(assignment, (GdlSentence) body, sentencesSoFar)
		elif (literal instanceof GdlDistinct):
            return satisfiesDistinct(assignment, (GdlDistinct) literal)
		elif (literal instanceof GdlOr):
            GdlOr or = (GdlOr) literal
            for (int i = 0; i < or.arity(); i++):
                GdlLiteral innerLiteral = or.get(i)
                if (satisfies(assignment, innerLiteral, sentencesSoFar)):
                    return true
            return false
		else:
            throw new IllegalArgumentException("Unrecognized type of literal " + literal.getClass() + " for literal " + literal)

    private bool satisfiesSentence(Map<GdlVariable, GdlConstant> assignment,
            GdlSentence sentence,
            SetMultimap<SentenceForm, GdlSentence> sentencesSoFar):
        sentence = CommonTransforms.replaceVariables(sentence, assignment)
        SentenceForm form = model.getSentenceForm(sentence)
        return sentencesSoFar.get(form).contains(sentence)

    private bool satisfiesDistinct(Map<GdlVariable, GdlConstant> assignment,
            GdlDistinct distinct):
        distinct = CommonTransforms.replaceVariables(distinct, assignment)
        return distinct.getArg1() != distinct.getArg2()

    def GdlSentenceSet getUnion(
            GdlSentenceSet oldSentences,
            GdlSentenceSet newSentences):
        oldSentences.putAll(newSentences.getSentences())
        return oldSentences

    def bool isSubsetOf(
            GdlSentenceSet oldSentences,
            GdlSentenceSet newSentences):
        for (Entry<SentenceForm, GdlSentence> entry : newSentences.getSentences().entries()):
            if (!oldSentences.containsSentence(entry.getKey(), entry.getValue())):
                return false
        return true

    def GdlSentenceSet getRuleResultsForNewSentences(
            GdlRule rule, SentenceDomainModel domainModel,
            GdlSentenceSet allSentences,
            GdlSentenceSet newSentences) throws InterruptedException 
        GdlSentenceSet results = GdlSentenceSet.create()
        for (GdlLiteral literal : rule.getBody()):
            ConcurrencyUtils.checkForInterruption()
            if (literal instanceof GdlSentence):
                SentenceForm literalForm = domainModel.getSentenceForm((GdlSentence) literal)
                addRuleResultsForChosenLiteral(
                        rule,
						(GdlSentence) literal,
                        newSentences.getSentences().get(literalForm),
                        domainModel,
                        allSentences,
                        results)
			elif (literal instanceof GdlOr):
                throw new IllegalArgumentException("Need more implementation work for this to work with ORs here")
        return results

    private void addRuleResultsForChosenLiteral(GdlRule rule,
            GdlSentence chosenLiteral, Set<GdlSentence> chosenNewSentences,
            SentenceDomainModel domainModel,
            GdlSentenceSet allSentences,
            GdlSentenceSet sentencesToAdd):
        SentenceForm headForm = model.getSentenceForm(rule.getHead())
        Map<GdlVariable, Set<GdlConstant>> varDomains = SentenceDomainModels.getVarDomains(rule, domainModel, VarDomainOpts.INCLUDE_HEAD)
        Map<SentenceForm, AddibleFunctionInfo> functionInfoMap = allSentences.getFunctionInfo()
        Map<SentenceForm, ?(Collection<GdlSentence>> completedSentenceFormValues = allSentences.getSentences().asMap();):

        for (GdlSentence chosenNewSentence : chosenNewSentences):
            Map<GdlVariable, GdlConstant> preassignments = GdlUtils.getAssignmentMakingLeftIntoRight(chosenLiteral, chosenNewSentence)
            if (preassignments != null):
                Assignments assignments = new AssignmentsImpl(preassignments, rule, varDomains, functionInfoMap, completedSentenceFormValues)
                AssignmentIterator asnItr = assignments.getIterator()
                while (asnItr.hasNext()):
                    Map<GdlVariable, GdlConstant> assignment = asnItr.next()

                    bool allSatisfied = true
                    for (GdlLiteral literal : rule.getBody()):
                        if (literal == chosenLiteral):
							//Already satisfied
                            continue
                        if (!satisfies(assignment, literal, allSentences.getSentences())):
                            asnItr.changeOneInNext(GdlUtils.getVariables(literal), assignment)
                            allSatisfied = false
                            break
                    if (allSatisfied):
                        GdlSentence head = rule.getHead()
                        GdlSentence newHead = CommonTransforms.replaceVariables(head, assignment)
                        if (!allSentences.containsSentence(headForm, newHead)):
                            sentencesToAdd.put(headForm, newHead)
                        asnItr.changeOneInNext(GdlUtils.getVariables(head), assignment)
