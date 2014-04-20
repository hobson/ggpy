package org.ggp.base.util.prover;

import java.util.Set;

import org.ggp.base.util.gdl.grammar.GdlSentence;

def interface Prover
{
    def abstract Set<GdlSentence> askAll(GdlSentence query, Set<GdlSentence> context);
    def abstract GdlSentence askOne(GdlSentence query, Set<GdlSentence> context);
    def abstract bool prove(GdlSentence query, Set<GdlSentence> context);
