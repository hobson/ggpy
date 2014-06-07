#!/usr/bin/env python
""" generated source for module SVGReplacedElementFactory """
# package: org.ggp.base.util.ui
import java.awt.AlphaComposite

import java.awt.Graphics2D

import java.awt.RenderingHints

import java.awt.image.BufferedImage

import java.io.File

import java.io.IOException

import javax.xml.parsers.DocumentBuilder

import javax.xml.parsers.DocumentBuilderFactory

import javax.xml.parsers.ParserConfigurationException

import org.apache.batik.dom.svg.SVGDOMImplementation

import org.apache.batik.transcoder.TranscoderException

import org.apache.batik.transcoder.TranscoderInput

import org.apache.batik.transcoder.TranscoderOutput

import org.apache.batik.transcoder.TranscodingHints

import org.apache.batik.transcoder.image.ImageTranscoder

import org.apache.batik.util.SVGConstants

import org.ggp.base.util.files.FileUtils

import org.w3c.dom.Document

import org.w3c.dom.Element

import org.xhtmlrenderer.extend.ReplacedElement

import org.xhtmlrenderer.extend.ReplacedElementFactory

import org.xhtmlrenderer.extend.UserAgentCallback

import org.xhtmlrenderer.layout.LayoutContext

import org.xhtmlrenderer.render.BlockBox

import org.xhtmlrenderer.simple.extend.FormSubmissionListener

import org.xhtmlrenderer.swing.ImageReplacedElement

class SVGReplacedElementFactory(ReplacedElementFactory):
    """ generated source for class SVGReplacedElementFactory """
    def createReplacedElement(self, c, box, uac, cssWidth, cssHeight):
        """ generated source for method createReplacedElement """
        element = box.getElement()
        if "svg" == element.getNodeName():
            try:
                documentBuilder = documentBuilderFactory.newDocumentBuilder()
            except ParserConfigurationException as e:
                raise RuntimeException(e)
            svgDocument.appendChild(svgElement)
            try:
                return ImageReplacedElement(rasterize(svgDocument, width), width, width)
            except IOException as e:
                return None
        return None

    @classmethod
    def rasterize(cls, dom, width):
        """ generated source for method rasterize """
        imagePointer = [None]*1
        #  Rendering hints can't be set programatically, so
        #  we override defaults with a temporary stylesheet.
        css = "svg {" + "shape-rendering: geometricPrecision;" + "text-rendering:  geometricPrecision;" + "color-rendering: optimizeQuality;" + "image-rendering: optimizeQuality;" + "}"
        cssFile = File.createTempFile("batik-default-override-", ".css")
        FileUtils.writeStringToFile(cssFile, css)
        transcoderHints = TranscodingHints()
        transcoderHints.put(ImageTranscoder.KEY_XML_PARSER_VALIDATING, Boolean.FALSE)
        transcoderHints.put(ImageTranscoder.KEY_DOM_IMPLEMENTATION, SVGDOMImplementation.getDOMImplementation())
        transcoderHints.put(ImageTranscoder.KEY_DOCUMENT_ELEMENT_NAMESPACE_URI, SVGConstants.SVG_NAMESPACE_URI)
        transcoderHints.put(ImageTranscoder.KEY_DOCUMENT_ELEMENT, "svg")
        transcoderHints.put(ImageTranscoder.KEY_USER_STYLESHEET_URI, cssFile.toURI().__str__())
        transcoderHints.put(ImageTranscoder.KEY_WIDTH, float(2 * width))
        transcoderHints.put(ImageTranscoder.KEY_HEIGHT, float(2 * width))
        transcoderHints.put(ImageTranscoder.KEY_MAX_HEIGHT, float(2 * width))
        transcoderHints.put(ImageTranscoder.KEY_MAX_WIDTH, float(2 * width))
        try:
            t.setTranscodingHints(transcoderHints)
            t.transcode(input, None)
        except TranscoderException as ex:
            #  Requires Java 6
            ex.printStackTrace()
            raise IOException("Couldn't convert SVG")
        finally:
            cssFile.delete()
        return imagePointer[0]

    def reset(self):
        """ generated source for method reset """

    def remove(self, e):
        """ generated source for method remove """

    def setFormSubmissionListener(self, listener):
        """ generated source for method setFormSubmissionListener """

