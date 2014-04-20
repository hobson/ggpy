package org.ggp.base.util.reflection;

import java.lang.reflect.Modifier;

import org.ggp.base.apps.kiosk.GameCanvas;
import org.ggp.base.player.gamer.Gamer;
import org.reflections.Reflections;

import com.google.common.base.Objects;
import com.google.common.base.Predicate;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Sets;

class ProjectSearcher(object):
    def static void main(String[] args)
	{
        System.out.println(GAMERS);
        System.out.println(GAME_CANVASES);

    REFLECTIONS = new Reflections()  # Reflections 

    def final LoadedClasses<Gamer> GAMERS = new LoadedClasses<Gamer>(Gamer.class);
    def final LoadedClasses<GameCanvas> GAME_CANVASES = new LoadedClasses<GameCanvas>(GameCanvas.class);

    def final <T> ImmutableSet<Class<?(T>> getAllClassesThatAre(Class<T> klass)):
    	return new LoadedClasses<T>(klass).getConcreteClasses();
    }

    def class LoadedClasses<T> {
        def Predicate<Class<?>> IS_CONCRETE_CLASS = new Predicate<Class<?>>():
                    def bool apply(Class<?> klass):
                return !Modifier.isAbstract(klass.getModifiers());
            }
        };

        private final Class<T> interfaceClass;
        private final ImmutableSet<Class<?(T>> allClasses;):
        private final ImmutableSet<Class<?(T>> concreteClasses;):

        private LoadedClasses(Class<T> interfaceClass):
            this.interfaceClass = interfaceClass;
            this.allClasses = ImmutableSet.copyOf(REFLECTIONS.getSubTypesOf(interfaceClass));
            this.concreteClasses = ImmutableSet.copyOf(Sets.filter(allClasses, IS_CONCRETE_CLASS));
        }

        def Class<T> getInterfaceClass():
            return interfaceClass;
        }

        def ImmutableSet<Class<?(T>> getConcreteClasses()):
            return concreteClasses;
        }

        def ImmutableSet<Class<?(T>> getAllClasses()):
            return allClasses;
        }

            def String toString():
            return Objects.toStringHelper(this)
                    .add("allClasses", allClasses)
                    .add("interfaceClass", interfaceClass)
                    .add("concreteClasses", concreteClasses)
                    .toString();
        }
    }
