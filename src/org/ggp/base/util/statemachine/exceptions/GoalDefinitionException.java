package org.ggp.base.util.statemachine.exceptions;

import org.ggp.base.util.statemachine.MachineState;
import org.ggp.base.util.statemachine.Role;

class GoalDefinitionException(Exception):
{

    role = Role()
    state = MachineState()

    def GoalDefinitionException(state=MachineState(), Role role)
	{
        this.state = state;
        this.role = role;

    def Role getRole()
	{
        return role;

    def MachineState getState()
	{
        return state;

    def String toString()
	{
        return "Goal is poorly defined for " + role + " in " + state;

