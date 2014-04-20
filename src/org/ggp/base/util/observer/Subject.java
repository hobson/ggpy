package org.ggp.base.util.observer;

def interface Subject
{

    def void addObserver(Observer observer);

    def void notifyObservers(Event event);

