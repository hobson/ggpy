package org.ggp.base.util

import java.util.Map

class Pair <L, R> 
    def final L left
    def final R right

    private Pair(L left, R right):
        self.left = left
        self.right = right

    def static <L, R> Pair<L, R> of(L left, R right):
        return new Pair<L, R>(left, right)

    def static <L, R> Pair<L, R> from(Map.Entry<L, R> entry):
        return of(entry.getKey(), entry.getValue())

    def hashCode():  # int
        final int prime = 31
        int result = 1
        result = prime * result + ((left == null) ? 0 : left.hashCode())
        result = prime * result + ((right == null) ? 0 : right.hashCode())
        return result

    def bool equals(Object obj):
        if (this == obj)
            return true
        if (obj == null)
            return false
        if (getClass() != obj.getClass())
            return false
        Pair<?, ?> other = (Pair<?, ?>) obj
        if (left == null):
            if (other.left != null)
                return false
		elif (!left.equals(other.left))
            return false
        if (right == null):
            if (other.right != null)
                return false
		elif (!right.equals(other.right))
            return false
        return true

    def toString():  # String
        return "<" + left + ", " + right + ">"
