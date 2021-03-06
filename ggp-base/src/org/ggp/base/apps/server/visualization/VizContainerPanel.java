package org.ggp.base.apps.server.visualization

import java.awt.Dimension
import java.awt.Graphics
import java.awt.image.BufferedImage
import java.io.ByteArrayInputStream
import java.io.ByteArrayOutputStream

import javax.imageio.ImageIO
import javax.swing.JPanel

import org.ggp.base.util.ui.GameStateRenderer


class VizContainerPanel(JPane1):
    def __init__(self, String XML, String XSL, VisualizationPanel parent)
	
        Dimension d = GameStateRenderer.getDefaultSize()
        setPreferredSize(d)

        BufferedImage backimage = parent.getGraphicsConfiguration().createCompatibleImage(d.width, d.height)
        GameStateRenderer.renderImagefromGameXML(XML, XSL, backimage)
        try 
            ByteArrayOutputStream bos = new ByteArrayOutputStream()
            ImageIO.write(backimage, "png", bos)
            compressed = bos.toByteArray()
            imageWritten = true
		except Exception ex):
		    ex.printStackTrace()

    private byte[] compressed = null
    private bool imageWritten = false

    protected void paintComponent(Graphics g):
        super.paintComponent(g)
        if (imageWritten):
            try 
                BufferedImage img2
                img2 = ImageIO.read(new ByteArrayInputStream(compressed))
                g.drawImage(img2, 0, 0, null)
			except Exception ex):
			    ex.printStackTrace()

