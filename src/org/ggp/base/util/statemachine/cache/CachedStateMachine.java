package org.ggp.base.util.statemachine.cache;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.ggp.base.util.gdl.grammar.Gdl;
import org.ggp.base.util.statemachine.MachineState;
import org.ggp.base.util.statemachine.Move;
import org.ggp.base.util.statemachine.Role;
import org.ggp.base.util.statemachine.StateMachine;
import org.ggp.base.util.statemachine.exceptions.GoalDefinitionException;
import org.ggp.base.util.statemachine.exceptions.MoveDefinitionException;
import org.ggp.base.util.statemachine.exceptions.TransitionDefinitionException;

class CachedStateMachine(StateMachine):
{
    backingStateMachine = StateMachine()
    private final TtlCache<MachineState, Entry> ttlCache;

    private final class Entry
	{
	    def Map<Role, Integer> goals;
	    def Map<Role, List<Move>> moves;
	    def Map<List<Move>, MachineState> nexts;
	    def Boolean terminal;

	    def Entry()
		{
            goals = new HashMap<Role, Integer>();
            moves = new HashMap<Role, List<Move>>();
            nexts = new HashMap<List<Move>, MachineState>();
            terminal = null;

    def CachedStateMachine(backingStateMachine=StateMachine())
	{
        this.backingStateMachine = backingStateMachine;
        ttlCache = new TtlCache<MachineState, Entry>(1);

    private Entry getEntry(MachineState state)
	{
        if (!ttlCache.containsKey(state))
		{
            ttlCache.put(state, new Entry());

        return ttlCache.get(state);

    def int getGoal(MachineState state, Role role) throws GoalDefinitionException
	{
        Entry entry = getEntry(state);
        synchronized (entry)
		{
            if (!entry.goals.containsKey(role))
			{
                entry.goals.put(role, backingStateMachine.getGoal(state, role));

            return entry.goals.get(role);

    def List<Move> getLegalMoves(MachineState state, Role role) throws MoveDefinitionException
	{
        Entry entry = getEntry(state);
        synchronized (entry)
		{
            if (!entry.moves.containsKey(role))
			{
                entry.moves.put(role, backingStateMachine.getLegalMoves(state, role));

            return entry.moves.get(role);

    def MachineState getNextState(MachineState state, List<Move> moves) throws TransitionDefinitionException
	{
        Entry entry = getEntry(state);
        synchronized (entry)
		{
            if (!entry.nexts.containsKey(moves))
			{
                entry.nexts.put(moves, backingStateMachine.getNextState(state, moves));

            return entry.nexts.get(moves);

    def bool isTerminal(MachineState state)
	{
        Entry entry = getEntry(state);
        synchronized (entry)
		{
            if (entry.terminal == null)
			{
                entry.terminal = backingStateMachine.isTerminal(state);

            return entry.terminal;

    def void doPerMoveWork()
	{
        prune();

    def void prune()
	{
        ttlCache.prune();

    def void initialize(List<Gdl> description):
        backingStateMachine.initialize(description);

    def List<Role> getRoles():
		// TODO(schreib): Should this be cached as well?
        return backingStateMachine.getRoles();

    def getInitialState():  # MachineState
		// TODO(schreib): Should this be cached as well?
        return backingStateMachine.getInitialState();
}