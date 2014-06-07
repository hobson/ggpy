#!/usr/bin/env python
""" generated source for module PropNet """
# package: org.ggp.base.util.propnet.architecture
import java.io.File

import java.io.FileOutputStream

import java.io.OutputStreamWriter

import java.util.HashMap

import java.util.HashSet

import java.util.List

import java.util.Map

import java.util.Set

import org.ggp.base.util.gdl.grammar.GdlConstant

import org.ggp.base.util.gdl.grammar.GdlPool

import org.ggp.base.util.gdl.grammar.GdlProposition

import org.ggp.base.util.gdl.grammar.GdlRelation

import org.ggp.base.util.gdl.grammar.GdlSentence

import org.ggp.base.util.gdl.grammar.GdlTerm

import org.ggp.base.util.logging.GamerLogger

import org.ggp.base.util.propnet.architecture.components.And

import org.ggp.base.util.propnet.architecture.components.Not

import org.ggp.base.util.propnet.architecture.components.Or

import org.ggp.base.util.propnet.architecture.components.Proposition

import org.ggp.base.util.propnet.architecture.components.Transition

import org.ggp.base.util.statemachine.Role

# 
#  * The PropNet class is designed to represent Propositional Networks.
#  *
#  * A propositional network (also known as a "propnet") is a way of representing
#  * a game as a logic circuit. States of the game are represented by assignments
#  * of TRUE or FALSE to "base" propositions, each of which represents a single
#  * fact that can be true about the state of the game. For example, in a game of
#  * Tic-Tac-Toe, the fact (cell 1 1 x) indicates that the cell (1,1) has an 'x'
#  * in it. That fact would correspond to a base proposition, which would be set
#  * to TRUE to indicate that the fact is true in the current state of the game.
#  * Likewise, the base corresponding to the fact (cell 1 1 o) would be false,
#  * because in that state of the game there isn't an 'o' in the cell (1,1).
#  *
#  * A state of the game is uniquely determined by the assignment of truth values
#  * to the base propositions in the propositional network. Every assignment of
#  * truth values to base propositions corresponds to exactly one unique state of
#  * the game.
#  *
#  * Given the values of the base propositions, you can use the connections in
#  * the network (AND gates, OR gates, NOT gates) to determine the truth values
#  * of other propositions. For example, you can determine whether the terminal
#  * proposition is true: if that proposition is true, the game is over when it
#  * reaches this state. Otherwise, if it is false, the game isn't over. You can
#  * also determine the value of the goal propositions, which represent facts
#  * like (goal xplayer 100). If that proposition is true, then that fact is true
#  * in this state of the game, which means that xplayer has 100 points.
#  *
#  * You can also use a propositional network to determine the next state of the
#  * game, given the current state and the moves for each player. First, you set
#  * the input propositions which correspond to each move to TRUE. Once that has
#  * been done, you can determine the truth value of the transitions. Each base
#  * proposition has a "transition" component going into it. This transition has
#  * the truth value that its base will take on in the next state of the game.
#  *
#  * For further information about propositional networks, see:
#  *
#  * "Decomposition of Games for Efficient Reasoning" by Eric Schkufza.
#  * "Factoring General Games using Propositional Automata" by Evan Cox et al.
#  *
#  * @author Sam Schreiber
#  
class PropNet(object):
    """ generated source for class PropNet """
    components = Set()
    propositions = Set()

    #  References to every BaseProposition in the PropNet, indexed by name. 
    basePropositions = Map()

    #  References to every InputProposition in the PropNet, indexed by name. 
    inputPropositions = Map()

    #  References to every LegalProposition in the PropNet, indexed by role. 
    legalPropositions = Map()

    #  References to every GoalProposition in the PropNet, indexed by role. 
    goalPropositions = Map()

    #  A reference to the single, unique, InitProposition. 
    initProposition = Proposition()

    #  A reference to the single, unique, TerminalProposition. 
    terminalProposition = Proposition()

    #  A helper mapping between input/legal propositions. 
    legalInputMap = Map()

    #  A helper list of all of the roles. 
    roles = List()

    def addComponent(self, c):
        """ generated source for method addComponent """
        self.components.add(c)
        if isinstance(c, (Proposition, )):
            self.propositions.add(c)

    # 
    # 	 * Creates a new PropNet from a list of Components, along with indices over
    # 	 * those components.
    # 	 *
    # 	 * @param components
    # 	 *            A list of Components.
    # 	 
    def __init__(self, roles, components):
        """ generated source for method __init__ """
        self.roles = roles
        self.components = components
        self.propositions = recordPropositions()
        self.basePropositions = recordBasePropositions()
        self.inputPropositions = recordInputPropositions()
        self.legalPropositions = recordLegalPropositions()
        self.goalPropositions = recordGoalPropositions()
        self.initProposition = recordInitProposition()
        self.terminalProposition = recordTerminalProposition()
        self.legalInputMap = makeLegalInputMap()

    def getRoles(self):
        """ generated source for method getRoles """
        return self.roles

    def getLegalInputMap(self):
        """ generated source for method getLegalInputMap """
        return self.legalInputMap

    def makeLegalInputMap(self):
        """ generated source for method makeLegalInputMap """
        legalInputMap = HashMap()
        #  Create a mapping from Body->Input.
        inputPropsByBody = HashMap()
        for inputProp in inputPropositions.values():
            inputPropsByBody.put(inputPropBody, inputProp)
        #  Use that mapping to map Input->Legal and Legal->Input
        #  based on having the same Body proposition.
        for legalProps in legalPropositions.values():
            for legalProp in legalProps:
                if inputPropsByBody.containsKey(legalPropBody):
                    legalInputMap.put(inputProp, legalProp)
                    legalInputMap.put(legalProp, inputProp)
        return legalInputMap

    # 
    # 	 * Getter method.
    # 	 *
    # 	 * @return References to every BaseProposition in the PropNet, indexed by
    # 	 *         name.
    # 	 
    def getBasePropositions(self):
        """ generated source for method getBasePropositions """
        return self.basePropositions

    # 
    # 	 * Getter method.
    # 	 *
    # 	 
    def getComponents(self):
        """ generated source for method getComponents """
        return self.components

    # 
    # 	 * Getter method.
    # 	 *
    # 	 * @return References to every GoalProposition in the PropNet, indexed by
    # 	 *         player name.
    # 	 
    def getGoalPropositions(self):
        """ generated source for method getGoalPropositions """
        return self.goalPropositions

    # 
    # 	 * Getter method. A reference to the single, unique, InitProposition.
    # 	 *
    # 	 * @return
    # 	 
    def getInitProposition(self):
        """ generated source for method getInitProposition """
        return self.initProposition

    # 
    # 	 * Getter method.
    # 	 *
    # 	 * @return References to every InputProposition in the PropNet, indexed by
    # 	 *         name.
    # 	 
    def getInputPropositions(self):
        """ generated source for method getInputPropositions """
        return self.inputPropositions

    # 
    # 	 * Getter method.
    # 	 *
    # 	 * @return References to every LegalProposition in the PropNet, indexed by
    # 	 *         player name.
    # 	 
    def getLegalPropositions(self):
        """ generated source for method getLegalPropositions """
        return self.legalPropositions

    # 
    # 	 * Getter method.
    # 	 *
    # 	 
    def getPropositions(self):
        """ generated source for method getPropositions """
        return self.propositions

    # 
    # 	 * Getter method.
    # 	 *
    # 	 * @return A reference to the single, unique, TerminalProposition.
    # 	 
    def getTerminalProposition(self):
        """ generated source for method getTerminalProposition """
        return self.terminalProposition

    # 
    # 	 * Returns a representation of the PropNet in .dot format.
    # 	 *
    # 	 * @see java.lang.Object#toString()
    # 	 
    def __str__(self):
        """ generated source for method toString """
        sb = StringBuilder()
        sb.append("digraph propNet\n{\n")
        for component in components:
            sb.append("\t" + component.__str__() + "\n")
        sb.append("}")
        return sb.__str__()

    # 
    #      * Outputs the propnet in .dot format to a particular file.
    #      * This can be viewed with tools like Graphviz and ZGRViewer.
    #      *
    #      * @param filename the name of the file to output to
    #      
    def renderToFile(self, filename):
        """ generated source for method renderToFile """
        try:
            fout.write(self.__str__())
            fout.close()
            fos.close()
        except Exception as e:
            GamerLogger.logStackTrace("StateMachine", e)

    # 
    # 	 *
    # 	 * This is done by going over every single-input proposition in the network,
    # 	 * and seeing whether or not its input is a transition, which would mean that
    # 	 * by definition the proposition is a base proposition.
    # 	 *
    # 	 
    def recordBasePropositions(self):
        """ generated source for method recordBasePropositions """
        basePropositions = HashMap()
        for proposition in propositions:
            #  Skip all propositions without exactly one input.
            if proposition.getInputs().size() != 1:
                continue 
            if isinstance(component, (Transition, )):
                basePropositions.put(proposition.__name__, proposition)
        return basePropositions

    # 
    # 	 *
    # 	 * This is done by going over every function proposition in the network
    #      * where the name of the function is "goal", and extracting the name of the
    #      * role associated with that goal proposition, and then using those role
    #      * names as keys that map to the goal propositions in the index.
    # 	 *
    # 	 
    def recordGoalPropositions(self):
        """ generated source for method recordGoalPropositions """
        goalPropositions = HashMap()
        for proposition in propositions:
            #  Skip all propositions that aren't GdlRelations.
            if not (isinstance(, (GdlRelation, ))):
                continue 
            if not relation.__name__.getValue() == "goal":
                continue 
            if not goalPropositions.containsKey(theRole):
                goalPropositions.put(theRole, HashSet())
            goalPropositions.get(theRole).add(proposition)
        return goalPropositions

    def recordInitProposition(self):
        """ generated source for method recordInitProposition """
        for proposition in propositions:
            if not (isinstance(, (GdlProposition, ))):
                continue 
            if constant.getValue().toUpperCase() == "INIT":
                return proposition
        return None

    def recordInputPropositions(self):
        """ generated source for method recordInputPropositions """
        inputPropositions = HashMap()
        for proposition in propositions:
            if not (isinstance(, (GdlRelation, ))):
                continue 
            if relation.__name__.getValue() == "does":
                inputPropositions.put(proposition.__name__, proposition)
        return inputPropositions

    def recordLegalPropositions(self):
        """ generated source for method recordLegalPropositions """
        legalPropositions = HashMap()
        for proposition in propositions:
            if not (isinstance(, (GdlRelation, ))):
                continue 
            if relation.__name__.getValue() == "legal":
                if not legalPropositions.containsKey(r):
                    legalPropositions.put(r, HashSet())
                legalPropositions.get(r).add(proposition)
        return legalPropositions

    def recordPropositions(self):
        """ generated source for method recordPropositions """
        propositions = HashSet()
        for component in components:
            if isinstance(component, (Proposition, )):
                propositions.add(component)
        return propositions

    def recordTerminalProposition(self):
        """ generated source for method recordTerminalProposition """
        for proposition in propositions:
            if isinstance(, (GdlProposition, )):
                if constant.getValue() == "terminal":
                    return proposition
        return None

    def getSize(self):
        """ generated source for method getSize """
        return len(self.components)

    def getNumAnds(self):
        """ generated source for method getNumAnds """
        andCount = 0
        for c in components:
            if isinstance(c, (And, )):
                andCount += 1
        return andCount

    def getNumOrs(self):
        """ generated source for method getNumOrs """
        orCount = 0
        for c in components:
            if isinstance(c, (Or, )):
                orCount += 1
        return orCount

    def getNumNots(self):
        """ generated source for method getNumNots """
        notCount = 0
        for c in components:
            if isinstance(c, (Not, )):
                notCount += 1
        return notCount

    def getNumLinks(self):
        """ generated source for method getNumLinks """
        linkCount = 0
        for c in components:
            linkCount += c.getOutputs().size()
        return linkCount

    def removeComponent(self, c):
        """ generated source for method removeComponent """
        if isinstance(c, (Proposition, )):
            if self.basePropositions.containsKey(name):
                self.basePropositions.remove(name)
            elif self.inputPropositions.containsKey(name):
                self.inputPropositions.remove(name)
                if partner != None:
                    self.legalInputMap.remove(partner)
                    self.legalInputMap.remove(p)
            elif name == GdlPool.getProposition(GdlPool.getConstant("INIT")):
                raise RuntimeException("The INIT component cannot be removed. Consider leaving it and ignoring it.")
            elif name == GdlPool.getProposition(GdlPool.getConstant("terminal")):
                raise RuntimeException("The terminal component cannot be removed.")
            else:
                for propositions in legalPropositions.values():
                    if self.propositions.contains(p):
                        self.propositions.remove(p)
                        if partner != None:
                            self.legalInputMap.remove(partner)
                            self.legalInputMap.remove(p)
                for propositions in goalPropositions.values():
                    self.propositions.remove(p)
            self.propositions.remove(p)
        self.components.remove(c)
        for parent in c.getInputs():
            parent.removeOutput(c)
        for child in c.getOutputs():
            child.removeInput(c)

PropNet.#  References to every component in the PropNet. 

PropNet.#  References to every Proposition in the PropNet. 

PropNet.# 	 * @return References to every Component in the PropNet.

PropNet.# 	 * @return References to every Proposition in the PropNet.

PropNet.# 	 * Builds an index over the BasePropositions in the PropNet.

PropNet.# 	 * @return An index over the BasePropositions in the PropNet.

PropNet.# 	 * Builds an index over the GoalPropositions in the PropNet.

PropNet.# 	 * @return An index over the GoalPropositions in the PropNet.

