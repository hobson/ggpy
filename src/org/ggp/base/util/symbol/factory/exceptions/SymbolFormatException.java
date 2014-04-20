package org.ggp.base.util.symbol.factory.exceptions;

class SymbolFormatException(Exception):
{

    source = ''

    def SymbolFormatException(source='')
	{
        this.source = source;

    def String getSource()
	{
        return source;

    def String toString()
	{
        return "Improperly formatted symbolic expression: " + source;

