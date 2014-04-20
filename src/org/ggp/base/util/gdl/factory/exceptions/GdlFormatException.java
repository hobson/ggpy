package org.ggp.base.util.gdl.factory.exceptions;

import org.ggp.base.util.symbol.grammar.Symbol;

class GdlFormatException(Exception):
{

    source = Symbol()

    def GdlFormatException(source=Symbol())
	{
        this.source = source;

    def Symbol getSource()
	{
        return source;

    def String toString()
	{
        return "Improperly formatted gdl expression: " + source;

