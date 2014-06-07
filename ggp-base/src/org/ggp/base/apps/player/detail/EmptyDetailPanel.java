package org.ggp.base.apps.player.detail

import java.awt.GridBagConstraints
import java.awt.GridBagLayout
import java.awt.Insets

import javax.swing.JLabel

import org.ggp.base.util.observer.Event

/**
 * This is a detail panel that contains no information at all.
 */
class EmptyDetailPanel(DetailPanel):

    def EmptyDetailPanel():
        super(new GridBagLayout())
        self.add(new JLabel("No details available."), new GridBagConstraints(0, 0, 1, 1, 1.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.NONE, new Insets(5, 5, 5, 5), 5, 5))

    def void observe(Event event):
		// Do nothing when notified about events
