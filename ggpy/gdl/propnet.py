#!/usr/bin/python
"""ggpy.gdl.propnet
 
Hobson Lane <hobson@totalgood.com>
(c) 2014 Hobson Lane
Open-source under MIT-license: [LICENSE.txt](github.com/hobson/ggpy/LICENSE.txt)
"""

import networkx as nx
# import pyparsing as pp
import operator

import parser 

class Node(object):
    def __init__(self, label=''):
        self.value = None
        self.label = label
    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.label)
    __str__ = __repr__

class Connective(Node):
    def __init__(self, label):
        super(Connective, self).__init__(label)
        self.ary = 1
        self.operator = bool

class AndGate(Connective):
    def __init__(self, label=''):
        super(AndGate, self).__init__(label)
        self.ary = 2
        self.operator = operator.and_

class OrGate(Connective):
    def __init__(self, label=''):
        super(OrGate, self).__init__(label)
        self.ary = 2
        self.operator = operator.or_

class Inverter(Connective):
    def __init__(self, label=''):
        super(Inverter, self).__init__(label)
        self.operator = operator.not_

class Transition(Connective):
    """Point in a network cycle that represents a transition from one state (turn) to the next, a delay of one time-step or 1/z."""
    def __init__(self, label=''):
        super(Transition, self).__init__(label)
        self.operator = lambda x: None

class Proposition(Node):
    def __init__(self, label=''):
        super(Proposition, self).__init__(label)
        self.value = None

class Input(Node):
    """Proposition Node with only outgoing arcs (edges), no incoming arcs"""
    def __init__(self, label=''):
        super(Input, self).__init__(label)

class Base(Node):
    """Proposition Node with an incoming arcs only from a Transition Nodes"""
    def __init__(self, label=''):
        super(Base, self).__init__(label)

class Terminal(Node):
    """Terminal Node for a GGP game that halts the transitions (game steps/plays) when it becomes true"""
    def __init__(self, label=''):
        super(Terminal, self).__init__(label)
    def operator(self):
        if self.value:
            raise StopIteration

class Goal(Node):
    """A non-boolean valued node which indicates the rewuard for a player as an integer from 0 to 100"""
    def __init__(self, label=''):
        super(Terminal, self).__init__(label)


class View(Node):
    """Proposition Node with incoming arcs only from Base or Input Nodes, no arcs from Transition nodes"""
    def __init__(self, label=''):
        super(View, self).__init__(label)

def network_from_parsed_gdl(parsed_gdl):
    raise NotImplementedError('Not yet implemented')
    return parsed_gdl

def test():
    propnet = nx.MultiDiGraph()
    # Example propnet from http://logic.stanford.edu/ggp/chapters/chapter_09.html
    s = Base('s')
    a = Input('a')
    b = Input('b')
    p, q, r = (View('p'), View('q'), View('r'))
    asp, pq, rs, qbr = (AndGate('asp'), Inverter('pq'), Transition('rs'), OrGate('qbr'))
    # propnet.add_node(s)
    # propnet.add_nodes_from((a, b))
    # propnet.add_nodes_from((p, q, r))
    # propnet.add_nodes_from((asp, pq, rs))

    propnet.add_edges_from([
                            (a, asp), (s, asp),
                            (asp, p),
                            (p, pq),
                            (pq, q),
                            (q, qbr),
                            (b, qbr), (qbr, r),
                            (r, rs),
                            (rs, s),
                           ])
    from matplotlib import pyplot as plt
    nx.draw(propnet, with_labels=True)
    plt.show()

    # game description from http://logic.stanford.edu/ggp/chapters/chapter_09.html
    t = 
    propnet.add_edges_from([
                            (a, asp), (s, asp),
                            (asp, p),
                            (p, pq),
                            (pq, q),
                            (q, qbr),
                            (b, qbr), (qbr, r),
                            (r, rs),
                            (rs, s),
                           ])
    gdl_example='''
        (role(white))
        (base(s))
        (input(white a))
        (input(white b))
        (legal(white a))
        (legal(white b))
        (<= p does(white a) & true(s))
        (<= q ~p)
        (<= r true(q))
        (<= r does(white b))
        (<= next(s) r)
        (<= terminal true(q))
        (<= goal(white 100) true(s))
        (<= goal(white 0) ~true(s))
        '''
    example = parser.game_description.parseString(gdl_example)

    propnet_computed =  network_from_parsed_gdl(example)
    nx.draw(propnet, with_labels=True)
    plt.show()
    return propnet

