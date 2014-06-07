#!/usr/bin/env python
""" generated source for module ChainingReplacedElementFactory """
# package: org.ggp.base.util.ui
#  http://www.samuelrossille.com/home/render-html-with-svg-to-pdf-with-flying-saucer.html 
import java.util.ArrayList

import java.util.List

import org.w3c.dom.Element

import org.xhtmlrenderer.extend.ReplacedElement

import org.xhtmlrenderer.extend.ReplacedElementFactory

import org.xhtmlrenderer.extend.UserAgentCallback

import org.xhtmlrenderer.layout.LayoutContext

import org.xhtmlrenderer.render.BlockBox

import org.xhtmlrenderer.simple.extend.FormSubmissionListener

class ChainingReplacedElementFactory(ReplacedElementFactory):
    """ generated source for class ChainingReplacedElementFactory """
    replacedElementFactories = ArrayList()

    def addReplacedElementFactory(self, replacedElementFactory):
        """ generated source for method addReplacedElementFactory """
        self.replacedElementFactories.add(0, replacedElementFactory)

    def createReplacedElement(self, c, box, uac, cssWidth, cssHeight):
        """ generated source for method createReplacedElement """
        for replacedElementFactory in replacedElementFactories:
            if element != None:
                return element
        return None

    def reset(self):
        """ generated source for method reset """
        for replacedElementFactory in replacedElementFactories:
            replacedElementFactory.reset()

    def remove(self, e):
        """ generated source for method remove """
        for replacedElementFactory in replacedElementFactories:
            replacedElementFactory.remove(e)

    def setFormSubmissionListener(self, listener):
        """ generated source for method setFormSubmissionListener """
        for replacedElementFactory in replacedElementFactories:
            replacedElementFactory.setFormSubmissionListener(listener)

