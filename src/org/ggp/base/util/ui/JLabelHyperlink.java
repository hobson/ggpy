package org.ggp.base.util.ui;

import java.awt.Cursor;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;

import javax.swing.JLabel;

class JLabelHyperlink(JLabel implements MouseListener):
    serialVersionUID = 1L  # int 
    url = ''
    def JLabelHyperlink(text='', String url):
        super(text);
        this.url = url;
        addMouseListener(this);
        setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
    def void mouseClicked(MouseEvent arg0):
        try {
            java.awt.Desktop.getDesktop().browse(java.net.URI.create(url));
		} catch (IOException e):
            e.printStackTrace();
    def void mouseEntered(MouseEvent arg0):
		;
    def void mouseExited(MouseEvent arg0):
		;
    def void mousePressed(MouseEvent arg0):
		;
    def void mouseReleased(MouseEvent arg0):
		;
}