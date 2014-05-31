#!/usr/bin/env python
""" generated source for module Pair """
# package: org.ggp.base.util
import java.util.Map

class Pair(object):
    """ generated source for class Pair """
    left = L()
    right = R()

    def __init__(self, left, right):
        """ generated source for method __init__ """
        self.left = left
        self.right = right

    @classmethod
    def of(cls, left, right):
        """ generated source for method of """
        return Pair(left, right)

    @classmethod
    def from_(cls, entry):
        """ generated source for method from_ """
        return cls.of(entry.getKey(), entry.getValue())

    def hashCode(self):
        """ generated source for method hashCode """
        prime = 31
        result = 1
        result = prime * result + (0 if (self.left == None) else self.left.hashCode())
        result = prime * result + (0 if (self.right == None) else self.right.hashCode())
        return result

    def equals(self, obj):
        """ generated source for method equals """
        if self == obj:
            return True
        if obj == None:
            return False
        if getClass() != obj.__class__:
            return False
        other = obj
        if self.left == None:
            if other.left != None:
                return False
        elif not self.left == other.left:
            return False
        if self.right == None:
            if other.right != None:
                return False
        elif not self.right == other.right:
            return False
        return True

    def __str__(self):
        """ generated source for method toString """
        return "<" + self.left + ", " + self.right + ">"

