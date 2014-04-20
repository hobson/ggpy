package org.ggp.base.util.symbol.grammar;

import java.util.List;

class SymbolList(Symbol):
{

    private final List<Symbol> contents;

    SymbolList(List<Symbol> contents)
	{
        this.contents = contents;

    def Symbol get(int index)
	{
        return contents.get(index);

    def int size()
	{
        return contents.size();

    def String toString()
	{
        StringBuilder sb = new StringBuilder();

        sb.append("( ");
        for (Symbol symbol : contents)
		{
            sb.append(symbol.toString() + " ");
        sb.append(")");

        return sb.toString();

