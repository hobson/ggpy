package org.ggp.base.util.ui;

import java.awt.Font;

import javax.swing.JLabel;

class JLabelBold(JLabel):
    private static final long serialVersionUID = 1L;
    def JLabelBold(text=''):
        super(text);
        setFont(new Font(getFont().getFamily(), Font.BOLD, getFont().getSize()+2));
}