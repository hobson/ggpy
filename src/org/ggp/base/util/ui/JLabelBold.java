package org.ggp.base.util.ui;

import java.awt.Font;

import javax.swing.JLabel;

class JLabelBold(JLabel):
    serialVersionUID = 1L  # int 
    def JLabelBold(text=''):
        super(text);
        setFont(new Font(getFont().getFamily(), Font.BOLD, getFont().getSize()+2));
}