#!/usr/bin/env python
""" generated source for module ProjectSearcher """
# package: org.ggp.base.util.reflection
import java.lang.reflect.Modifier

import org.ggp.base.apps.kiosk.GameCanvas

import org.ggp.base.player.gamer.Gamer

import org.reflections.Reflections

import com.google.common.base.Objects

import com.google.common.base.Predicate

import com.google.common.collect.ImmutableSet

import com.google.common.collect.Sets

class ProjectSearcher(object):
    """ generated source for class ProjectSearcher """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        print GAMERS
        print GAME_CANVASES

    REFLECTIONS = Reflections()
    GAMERS = LoadedClasses(Gamer.__class__)
    GAME_CANVASES = LoadedClasses(GameCanvas.__class__)

    @classmethod
    def getAllClassesThatAre(cls, klass):
        """ generated source for method getAllClassesThatAre """
        return LoadedClasses(klass).getConcreteClasses()

    class LoadedClasses(object):
        """ generated source for class LoadedClasses """
        IS_CONCRETE_CLASS = Predicate()

        def apply(self, klass):
            """ generated source for method apply """
            return not Modifier.isAbstract(klass.getModifiers())

        interfaceClass = Class()
        allClasses = ImmutableSet()
        concreteClasses = ImmutableSet()

        def __init__(self, interfaceClass):
            """ generated source for method __init__ """
            self.interfaceClass = interfaceClass
            self.allClasses = ImmutableSet.copyOf(self.REFLECTIONS.getSubTypesOf(interfaceClass))
            self.concreteClasses = ImmutableSet.copyOf(Sets.filter(self.allClasses, self.IS_CONCRETE_CLASS))

        def getInterfaceClass(self):
            """ generated source for method getInterfaceClass """
            return self.interfaceClass

        def getConcreteClasses(self):
            """ generated source for method getConcreteClasses """
            return self.concreteClasses

        def getAllClasses(self):
            """ generated source for method getAllClasses """
            return self.allClasses

        def __str__(self):
            """ generated source for method toString """
            return Objects.toStringHelper(self).add("allClasses", self.allClasses).add("interfaceClass", self.interfaceClass).add("concreteClasses", self.concreteClasses).__str__()


if __name__ == '__main__':
    import sys
    ProjectSearcher.main(sys.argv)

