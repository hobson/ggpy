#!/usr/bin/env python
""" generated source for module JLabelBold """
# package: org.ggp.base.util.ui
import java.awt.Font

import javax.swing.JLabel

class JLabelBold(JLabel):
    """ generated source for class JLabelBold """
    serialVersionUID = 1L

    def __init__(self, text):
        """ generated source for method __init__ """
        super(JLabelBold, self).__init__(text)
        setFont(Font(getFont().getFamily(), Font.BOLD, getFont().getSize() + 2))

