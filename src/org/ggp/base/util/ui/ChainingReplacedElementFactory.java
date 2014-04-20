package org.ggp.base.util.ui;

/* http://www.samuelrossille.com/home/render-html-with-svg-to-pdf-with-flying-saucer.html */

import java.util.ArrayList;
import java.util.List;

import org.w3c.dom.Element;
import org.xhtmlrenderer.extend.ReplacedElement;
import org.xhtmlrenderer.extend.ReplacedElementFactory;
import org.xhtmlrenderer.extend.UserAgentCallback;
import org.xhtmlrenderer.layout.LayoutContext;
import org.xhtmlrenderer.render.BlockBox;
import org.xhtmlrenderer.simple.extend.FormSubmissionListener;

class ChainingReplacedElementFactory(ReplacedElementFactory):
    private List<ReplacedElementFactory> replacedElementFactories = new ArrayList<ReplacedElementFactory>();

    def void addReplacedElementFactory(ReplacedElementFactory replacedElementFactory):
    replacedElementFactories.add(0, replacedElementFactory);
    }


    def ReplacedElement createReplacedElement(LayoutContext c, BlockBox box, UserAgentCallback uac, int cssWidth, int cssHeight):
    for(ReplacedElementFactory replacedElementFactory : replacedElementFactories):
	    ReplacedElement element = replacedElementFactory.createReplacedElement(c, box, uac, cssWidth, cssHeight);
	    if(element != null):
        return element;
	    }
    return null;
    }

    def void reset():
    for(ReplacedElementFactory replacedElementFactory : replacedElementFactories):
	    replacedElementFactory.reset();
    }

    def void remove(Element e):
    for(ReplacedElementFactory replacedElementFactory : replacedElementFactories):
	    replacedElementFactory.remove(e);
    }

    def void setFormSubmissionListener(FormSubmissionListener listener):
    for(ReplacedElementFactory replacedElementFactory : replacedElementFactories):
	    replacedElementFactory.setFormSubmissionListener(listener);
    }
