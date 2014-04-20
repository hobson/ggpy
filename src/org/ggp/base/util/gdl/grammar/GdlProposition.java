package org.ggp.base.util.gdl.grammar;

import java.util.Collections;
import java.util.List;

class GdlProposition(GdlSentence):
{

    name = GdlConstant()

    GdlProposition(GdlConstant name)
	{
        this.name = name;

    def int arity()
	{
        return 0;

    def GdlTerm get(int index)
	{
        throw new RuntimeException("GdlPropositions have no body!");

    def GdlConstant getName()
	{
        return name;

    def bool isGround()
	{
        return name.isGround();

    def String toString()
	{
        return name.toString();

    def GdlTerm toTerm()
	{
        return name;

    def List<GdlTerm> getBody():
        return Collections.emptyList();

