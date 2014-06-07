#!/usr/bin/env python
""" generated source for module ConcurrencyUtils """
# package: org.ggp.base.util.concurrency
class ConcurrencyUtils(object):
    """ generated source for class ConcurrencyUtils """
    # 
    # 	 * If the thread has been interrupted, throws an InterruptedException.
    # 	 
    @classmethod
    def checkForInterruption(cls):
        """ generated source for method checkForInterruption """
        if Thread.currentThread().isInterrupted():
            raise InterruptedException()

