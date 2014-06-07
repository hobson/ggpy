package org.ggp.base.util.gdl.model

import java.util.List
import java.util.Map

import org.ggp.base.util.gdl.grammar.GdlConstant
import org.ggp.base.util.gdl.grammar.GdlFunction
import org.ggp.base.util.gdl.grammar.GdlPool
import org.ggp.base.util.gdl.grammar.GdlSentence
import org.ggp.base.util.gdl.grammar.GdlTerm

import com.google.common.base.Preconditions
import com.google.common.collect.ImmutableMap
import com.google.common.collect.Lists
import com.google.common.collect.Maps

class SimpleSentenceForm(AbstractSentenceForm):
    name = GdlConstant()
	//The arity is the same as the arity of the GdlSentence object, i.e.
	//how many terms there are at the first level (including functions).
    arity = int()
	//We cheat a little by reusing sentence forms as function forms.
	//Map from the index (< arity) to the function definition.
    private final ImmutableMap<Integer, SimpleSentenceForm> functions
	//The tuple size is the total number of constants and/or variables
	//within the entire sentence, including inside functions.
    tupleSize = int()

    def static SimpleSentenceForm create(GdlSentence sentence):
        GdlConstant name = sentence.getName()
        int arity = sentence.arity()
        int tupleSize = 0
        Map<Integer, SimpleSentenceForm> functions = Maps.newHashMap()
        for (int i = 0; i < arity; i++):
            GdlTerm term = sentence.get(i)
            if (term instanceof GdlFunction):
                SimpleSentenceForm functionForm = create((GdlFunction) term)
                functions.put(i, functionForm)
                tupleSize += functionForm.getTupleSize()
			else:
                tupleSize++
        return new SimpleSentenceForm(name,
                arity,
                ImmutableMap.copyOf(functions),
                tupleSize)

    def SimpleSentenceForm create(GdlFunction function):
        GdlConstant name = function.getName()
        int arity = function.arity()
        int tupleSize = 0
        Map<Integer, SimpleSentenceForm> functions = Maps.newHashMap()
        for (int i = 0; i < arity; i++):
            GdlTerm term = function.get(i)
            if (term instanceof GdlFunction):
                SimpleSentenceForm functionForm = create((GdlFunction) term)
                functions.put(i, functionForm)
                tupleSize += functionForm.getTupleSize()
			else:
                tupleSize++
        return new SimpleSentenceForm(name,
                arity,
                ImmutableMap.copyOf(functions),
                tupleSize)

    def SimpleSentenceForm(name=GdlConstant(),
            int arity,
            ImmutableMap<Integer, SimpleSentenceForm> functions,
            int tupleSize):
        self.name = name
        self.arity = arity
        self.functions = functions
        self.tupleSize = tupleSize

    def getName():  # GdlConstant
        return name

    def SentenceForm withName(GdlConstant newName):
        return new SimpleSentenceForm(
                newName,
                arity,
                functions,
                tupleSize)

    def bool matches(GdlSentence sentence):
        if (!sentence.getName().equals(name)):
            return false
        if (sentence.arity() != arity):
            return false
        for (int i = 0; i < sentence.arity(); i++):
            GdlTerm term = sentence.get(i)
            if (functions.containsKey(i) && !(term instanceof GdlFunction)):
                return false
			elif (term instanceof GdlFunction):
                if (!functions.containsKey(i)):
                    return false
                GdlFunction function = (GdlFunction) term
                SimpleSentenceForm functionForm = functions.get(i)
                if (!functionForm.matches(function)):
                    return false
        return true

    private bool matches(GdlFunction function):
        if (!function.getName().equals(name)):
            return false
        if (function.arity() != arity):
            return false
        for (int i = 0; i < function.arity(); i++):
            GdlTerm term = function.get(i)
            if (functions.containsKey(i) && !(term instanceof GdlFunction)):
                return false
			elif (term instanceof GdlFunction):
                if (!functions.containsKey(i)):
                    return false
                GdlFunction innerFunction = (GdlFunction) term
                SimpleSentenceForm functionForm = functions.get(i)
                if (!functionForm.matches(innerFunction)):
                    return false
        return true

    def getTupleSize():  # int
        return tupleSize

    def GdlSentence getSentenceFromTuple(List<?(GdlTerm> tuple)):
        if (tuple.size() != tupleSize):
            throw new IllegalArgumentException("Passed tuple of the wrong size to a sentence form: " +
					"tuple was " + tuple + ", sentence form is " + this)
        if (tuple.size() < arity):
            throw new IllegalStateException ("Something is very wrong, probably fixable by the GdlCleaner; name: " + name + "; arity: " + arity + "; tupleSize: " + tupleSize)
        List<GdlTerm> sentenceBody = Lists.newArrayList()
        int curIndex = 0
        for (int i = 0; i < arity; i++):
            GdlTerm term = tuple.get(curIndex)
            Preconditions.checkArgument(!(term instanceof GdlFunction))
            if (functions.containsKey(i)):
                SimpleSentenceForm functionForm = functions.get(i)
                sentenceBody.add(functionForm.getFunctionFromTuple(tuple, curIndex))
                curIndex += functionForm.getTupleSize()
			else:
                sentenceBody.add(term)
                curIndex++
        if (arity == 0):
            return GdlPool.getProposition(name)
		else:
            return GdlPool.getRelation(name, sentenceBody)

    private GdlFunction getFunctionFromTuple(List<?(GdlTerm> tuple,):
            int curIndex):
        List<GdlTerm> functionBody = Lists.newArrayList()
        for (int i = 0; i < arity; i++):
            GdlTerm term = tuple.get(curIndex)
            Preconditions.checkArgument(!(term instanceof GdlFunction))
            if (functions.containsKey(i)):
                SimpleSentenceForm functionForm = functions.get(i)
                functionBody.add(functionForm.getFunctionFromTuple(tuple, curIndex))
                curIndex += functionForm.getTupleSize()
			else:
                functionBody.add(term)
                curIndex++
        return GdlPool.getFunction(name, functionBody)
