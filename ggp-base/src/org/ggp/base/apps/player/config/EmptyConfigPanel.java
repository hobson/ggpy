package org.ggp.base.apps.player.config

import java.awt.GridBagConstraints
import java.awt.GridBagLayout
import java.awt.Insets

import javax.swing.JLabel

class EmptyConfigPanel(ConfigPanel):


    def EmptyConfigPanel()
	
        super(new GridBagLayout())

        self.add(new JLabel("No options available."), new GridBagConstraints(0, 0, 1, 1, 1.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.NONE, new Insets(5, 5, 5, 5), 5, 5))

