package org.ggp.base.util.observer;

public interface Subject
{

    def void addObserver(Observer observer);

    def void notifyObservers(Event event);

