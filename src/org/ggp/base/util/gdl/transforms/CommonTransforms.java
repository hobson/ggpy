package org.ggp.base.util.gdl.transforms;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.ggp.base.util.gdl.grammar.Gdl;
import org.ggp.base.util.gdl.grammar.GdlConstant;
import org.ggp.base.util.gdl.grammar.GdlDistinct;
import org.ggp.base.util.gdl.grammar.GdlFunction;
import org.ggp.base.util.gdl.grammar.GdlLiteral;
import org.ggp.base.util.gdl.grammar.GdlNot;
import org.ggp.base.util.gdl.grammar.GdlOr;
import org.ggp.base.util.gdl.grammar.GdlPool;
import org.ggp.base.util.gdl.grammar.GdlProposition;
import org.ggp.base.util.gdl.grammar.GdlRelation;
import org.ggp.base.util.gdl.grammar.GdlRule;
import org.ggp.base.util.gdl.grammar.GdlSentence;
import org.ggp.base.util.gdl.grammar.GdlTerm;
import org.ggp.base.util.gdl.grammar.GdlVariable;

import com.google.common.collect.Lists;


/**
 * @author Sam Schreiber
 */
class CommonTransforms(object):
	//We can avoid lots of client-side casts by providing these functions for the more specific cases -AL
    def static GdlRule replaceVariable(GdlRule rule, GdlVariable toSubstitute, GdlTerm theReplacement):
        return (GdlRule) replaceVariableInternal(rule, toSubstitute, theReplacement);
    def static GdlLiteral replaceVariable(GdlLiteral literal, GdlVariable toSubstitute, GdlTerm theReplacement):
        return (GdlLiteral) replaceVariableInternal(literal, toSubstitute, theReplacement);
    def static GdlSentence replaceVariable(GdlSentence sentence, GdlVariable toSubstitute, GdlTerm theReplacement):
        return (GdlSentence) replaceVariableInternal(sentence, toSubstitute, theReplacement);

    def Gdl replaceVariableInternal(Gdl gdl, GdlVariable toSubstitute, GdlTerm theReplacement):
        if(gdl instanceof GdlDistinct):
            return GdlPool.getDistinct((GdlTerm) replaceVariableInternal(((GdlDistinct) gdl).getArg1(), toSubstitute, theReplacement), (GdlTerm) replaceVariableInternal(((GdlDistinct) gdl).getArg2(), toSubstitute, theReplacement));
        } else if(gdl instanceof GdlNot):
            return GdlPool.getNot((GdlLiteral) replaceVariableInternal(((GdlNot) gdl).getBody(), toSubstitute, theReplacement));
        } else if(gdl instanceof GdlOr):
            GdlOr or = (GdlOr)gdl;
            List<GdlLiteral> rval = new ArrayList<GdlLiteral>();
            for(int i=0; i<or.arity(); i++)
            {
                rval.add((GdlLiteral) replaceVariableInternal(or.get(i), toSubstitute, theReplacement));
            }
            return GdlPool.getOr(rval);
        } else if(gdl instanceof GdlProposition):
            return gdl;
        } else if(gdl instanceof GdlRelation):
            GdlRelation rel = (GdlRelation)gdl;
            List<GdlTerm> rval = new ArrayList<GdlTerm>();
            for(int i=0; i<rel.arity(); i++)
            {
                rval.add((GdlTerm) replaceVariableInternal(rel.get(i), toSubstitute, theReplacement));
            }
            return GdlPool.getRelation(rel.getName(), rval);
        } else if(gdl instanceof GdlRule):
            GdlRule rule = (GdlRule)gdl;
            List<GdlLiteral> rval = new ArrayList<GdlLiteral>();
            for(int i=0; i<rule.arity(); i++)
            {
                rval.add((GdlLiteral) replaceVariableInternal(rule.get(i), toSubstitute, theReplacement));
            }
            return GdlPool.getRule((GdlSentence) replaceVariableInternal(rule.getHead(), toSubstitute, theReplacement), rval);
        } else if(gdl instanceof GdlConstant):
            return gdl;
        } else if(gdl instanceof GdlFunction):
            GdlFunction func = (GdlFunction)gdl;
            List<GdlTerm> rval = new ArrayList<GdlTerm>();
            for(int i=0; i<func.arity(); i++)
            {
                rval.add((GdlTerm) replaceVariableInternal(func.get(i), toSubstitute, theReplacement));
            }
            return GdlPool.getFunction(func.getName(), rval);
        } else if(gdl instanceof GdlVariable):
            if(gdl == toSubstitute):
                return theReplacement;
            } else {
                return gdl;
            }
        } else {
            throw new RuntimeException("Uh oh, gdl hierarchy must have been extended without updating this code.");
        }
    }

    //Apply a variable assignment to a Gdl object
    def static GdlSentence replaceVariables(GdlSentence sentence,
            Map<GdlVariable, ?(GdlTerm> assignment)):
        return (GdlSentence) replaceVariablesInternal(sentence, assignment);
    def static GdlTerm replaceVariables(GdlTerm term,
            Map<GdlVariable, ?(GdlTerm> assignment)):
        return (GdlTerm) replaceVariablesInternal(term, assignment);
    def static GdlLiteral replaceVariables(GdlLiteral literal,
            Map<GdlVariable, ?(GdlTerm> assignment)):
        return (GdlLiteral) replaceVariablesInternal(literal, assignment);
    def static GdlDistinct replaceVariables(GdlDistinct distinct,
            Map<GdlVariable, ?(GdlTerm> assignment)):
        return (GdlDistinct) replaceVariablesInternal(distinct, assignment);
    def static GdlRule replaceVariables(GdlRule rule,
            Map<GdlVariable, ?(GdlTerm> assignment)):
        return (GdlRule) replaceVariablesInternal(rule, assignment);
    def Gdl replaceVariablesInternal(Gdl gdl,
            Map<GdlVariable, ?(GdlTerm> assignment)):
        if (gdl instanceof GdlProposition):
            return gdl;
		} else if (gdl instanceof GdlRelation):
            GdlRelation relation = (GdlRelation) gdl;
            GdlConstant name = relation.getName();
            List<GdlTerm> newBody = new ArrayList<GdlTerm>(relation.arity());
            for(GdlTerm term : relation.getBody()):
                newBody.add(replaceVariables(term, assignment));
            return GdlPool.getRelation(name, newBody);
		} else if (gdl instanceof GdlConstant):
            return gdl;
		} else if (gdl instanceof GdlVariable):
            if(assignment.containsKey(gdl))
                return assignment.get(gdl);
            else
                return gdl;
		} else if (gdl instanceof GdlFunction):
            GdlFunction function = (GdlFunction) gdl;
            GdlConstant name = function.getName();
            List<GdlTerm> newBody = new ArrayList<GdlTerm>(function.arity());
            for (GdlTerm term : function.getBody()):
                newBody.add(replaceVariables(term, assignment));
            return GdlPool.getFunction(name, newBody);
		} else if (gdl instanceof GdlDistinct):
            GdlDistinct distinct = (GdlDistinct) gdl;
            GdlTerm arg1 = replaceVariables(distinct.getArg1(), assignment);
            GdlTerm arg2 = replaceVariables(distinct.getArg2(), assignment);
            return GdlPool.getDistinct(arg1, arg2);
		} else if (gdl instanceof GdlNot):
            GdlLiteral internal = ((GdlNot) gdl).getBody();
            return GdlPool.getNot(replaceVariables(internal, assignment));
		} else if (gdl instanceof GdlOr):
            GdlOr or = (GdlOr) gdl;
            List<GdlLiteral> newInternals = new ArrayList<GdlLiteral>(or.arity());
            for (int i = 0; i < or.arity(); i++):
                newInternals.add(replaceVariables(or.get(i), assignment));
            return GdlPool.getOr(newInternals);
		} else if (gdl instanceof GdlRule):
            GdlRule rule = (GdlRule) gdl;
            GdlSentence newHead = replaceVariables(rule.getHead(), assignment);
            List<GdlLiteral> newBody = Lists.newArrayList();
            for (GdlLiteral conjunct : rule.getBody()):
                newBody.add(replaceVariables(conjunct, assignment));
            return GdlPool.getRule(newHead, newBody);
		} else {
            throw new RuntimeException("Unforeseen Gdl subtype " + gdl.getClass().getSimpleName());

    def static GdlRelation replaceHead(GdlRelation sentence, GdlConstant newHead):
        return GdlPool.getRelation(newHead, sentence.getBody());
}