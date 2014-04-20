package org.ggp.base.util.symbol.grammar;

class SymbolAtom(Symbol):
{

    value = ''

    SymbolAtom(String value)
	{
        this.value = value.intern();

    def String getValue()
	{
        return value;

    def String toString()
	{
        return value;

