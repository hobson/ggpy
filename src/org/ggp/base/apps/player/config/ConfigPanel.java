package org.ggp.base.apps.player.config;

import java.awt.LayoutManager;

import javax.swing.JPanel;

def abstract class ConfigPanel(JPanel):
{

    def ConfigPanel(layoutManager=LayoutManager())
	{
        super(layoutManager);

