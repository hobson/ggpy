#!/usr/bin/env python
""" generated source for module Component """
# package: org.ggp.base.util.propnet.architecture
import java.io.Serializable

import java.util.HashSet

import java.util.Set

# 
#  * The root class of the Component hierarchy, which is designed to represent
#  * nodes in a PropNet. The general contract of derived classes is to override
#  * all methods.
#  
class Component(Serializable):
    """ generated source for class Component """
    serialVersionUID = 352524175700224447L

    #  The inputs to the component. 
    inputs = Set()

    #  The outputs of the component. 
    outputs = Set()

    # 
    #      * Creates a new Component with no inputs or outputs.
    #      
    def __init__(self):
        """ generated source for method __init__ """
        super(Component, self).__init__()
        self.inputs = HashSet()
        self.outputs = HashSet()

    # 
    #      * Adds a new input.
    #      *
    #      * @param input
    #      *            A new input.
    #      
    def addInput(self, input):
        """ generated source for method addInput """
        self.inputs.add(input)

    def removeInput(self, input):
        """ generated source for method removeInput """
        self.inputs.remove(input)

    def removeOutput(self, output):
        """ generated source for method removeOutput """
        self.outputs.remove(output)

    def removeAllInputs(self):
        """ generated source for method removeAllInputs """
        self.inputs.clear()

    def removeAllOutputs(self):
        """ generated source for method removeAllOutputs """
        self.outputs.clear()

    # 
    #      * Adds a new output.
    #      *
    #      * @param output
    #      *            A new output.
    #      
    def addOutput(self, output):
        """ generated source for method addOutput """
        self.outputs.add(output)

    # 
    #      * Getter method.
    #      *
    #      * @return The inputs to the component.
    #      
    def getInputs(self):
        """ generated source for method getInputs """
        return self.inputs

    # 
    #      * A convenience method, to get a single input.
    #      * To be used only when the component is known to have
    #      * exactly one input.
    #      *
    #      * @return The single input to the component.
    #      
    def getSingleInput(self):
        """ generated source for method getSingleInput """
        assert len(self.inputs) == 1
        return self.inputs.iterator().next()

    # 
    #      * Getter method.
    #      *
    #      * @return The outputs of the component.
    #      
    def getOutputs(self):
        """ generated source for method getOutputs """
        return self.outputs

    # 
    #      * A convenience method, to get a single output.
    #      * To be used only when the component is known to have
    #      * exactly one output.
    #      *
    #      * @return The single output to the component.
    #      
    def getSingleOutput(self):
        """ generated source for method getSingleOutput """
        assert len(self.outputs) == 1
        return self.outputs.iterator().next()

    # 
    #      *
    #      
    def getValue(self):
        """ generated source for method getValue """

    # 
    #      * Returns a representation of the Component in .dot format.
    #      *
    #      * @see java.lang.Object#toString()
    #      
    def __str__(self):
        """ generated source for method toString """

    # 
    #      * Returns a configurable representation of the Component in .dot format.
    #      *
    #      * @param shape
    #      *            The value to use as the <tt>shape</tt> attribute.
    #      * @param fillcolor
    #      *            The value to use as the <tt>fillcolor</tt> attribute.
    #      * @param label
    #      *            The value to use as the <tt>label</tt> attribute.
    #      * @return A representation of the Component in .dot format.
    #      
    def toDot(self, shape, fillcolor, label):
        """ generated source for method toDot """
        sb = StringBuilder()
        sb.append("\"@" + Integer.toHexString(hashCode()) + "\"[shape=" + shape + ", style= filled, fillcolor=" + fillcolor + ", label=\"" + label + "\"]; ")
        for component in getOutputs():
            sb.append("\"@" + Integer.toHexString(hashCode()) + "\"->" + "\"@" + Integer.toHexString(component.hashCode()) + "\"; ")
        return sb.__str__()

Component.#      * Returns the value of the Component.

Component.#      * @return The value of the Component.

