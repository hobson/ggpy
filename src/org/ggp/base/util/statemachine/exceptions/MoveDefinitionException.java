package org.ggp.base.util.statemachine.exceptions;

import org.ggp.base.util.statemachine.MachineState;
import org.ggp.base.util.statemachine.Role;

class MoveDefinitionException(Exception):
{

    role = Role()
    state = MachineState()

    def MoveDefinitionException(state=MachineState(), Role role)
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
        return "There are no legal moves defined for " + role + " in " + state;

