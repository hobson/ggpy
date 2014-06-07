#!/usr/bin/env python
""" generated source for module Subject """
# package: org.ggp.base.util.observer
class Subject(object):
    """ generated source for interface Subject """
    __metaclass__ = ABCMeta
    @abstractmethod
    def addObserver(self, observer):
        """ generated source for method addObserver """

    @abstractmethod
    def notifyObservers(self, event):
        """ generated source for method notifyObservers """

