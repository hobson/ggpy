#!/usr/bin/env python
""" generated source for module ConfigurableDetailPanel """
# package: org.ggp.base.player.gamer.statemachine.configurable
import java.awt.Dimension

import java.awt.GridBagConstraints

import java.awt.GridBagLayout

import java.awt.Insets

import java.awt.event.ActionEvent

import java.util.Date

import java.util.HashSet

import java.util.Set

import javax.swing.AbstractAction

import javax.swing.JButton

import javax.swing.JPanel

import javax.swing.JScrollPane

import javax.swing.ScrollPaneConstants

import javax.swing.table.DefaultTableModel

import org.ggp.base.apps.player.detail.DetailPanel

import org.ggp.base.player.gamer.event.GamerNewMatchEvent

import org.ggp.base.util.observer.Event

import org.ggp.base.util.statemachine.Move

import org.ggp.base.util.ui.table.JZebraTable

import org.jfree.chart.ChartFactory

import org.jfree.chart.ChartPanel

import org.jfree.chart.JFreeChart

import org.jfree.chart.axis.LogarithmicAxis

import org.jfree.data.time.Millisecond

import org.jfree.data.time.TimeSeries

import org.jfree.data.time.TimeSeriesCollection

@SuppressWarnings("serial")
class ConfigurableDetailPanel(DetailPanel):
    """ generated source for class ConfigurableDetailPanel """
    moveTable = JZebraTable()
    memUsage = TimeSeries()
    memTotal = TimeSeries()
    counters = Set()
    countersCollection = TimeSeriesCollection()
    scoreCountersCollection = TimeSeriesCollection()

    def __init__(self):
        """ generated source for method __init__ """
        super(ConfigurableDetailPanel, self).__init__(GridBagLayout())
        model = DefaultTableModel()
        model.addColumn("Step")
        model.addColumn("My Move")
        model.addColumn("Time spent")
        model.addColumn("Out of time?")
        self.moveTable = JZebraTable(model)
        self.moveTable.setShowHorizontalLines(True)
        self.moveTable.setShowVerticalLines(True)
        sidePanel = JPanel()
        self.memUsage = TimeSeries("Used Memory")
        self.memTotal = TimeSeries("Total Memory")
        self.memUsage.setMaximumItemCount(36000)
        self.memTotal.setMaximumItemCount(36000)
        memory = TimeSeriesCollection()
        memory.addSeries(self.memUsage)
        memory.addSeries(self.memTotal)
        memChart = ChartFactory.createTimeSeriesChart(None, None, "Megabytes", memory, True, True, False)
        memChart.setBackgroundPaint(getBackground())
        memChartPanel = ChartPanel(memChart)
        memChartPanel.setPreferredSize(Dimension(500, 175))
        sidePanel.add(memChartPanel)
        self.counters = HashSet()
        self.countersCollection = TimeSeriesCollection()
        counterChart = ChartFactory.createTimeSeriesChart(None, None, None, self.countersCollection, True, True, False)
        counterChart.getXYPlot().setRangeAxis(LogarithmicAxis("Count per 100ms"))
        counterChart.getXYPlot().getRangeAxis().setAutoRangeMinimumSize(1.0)
        counterChart.setBackgroundPaint(getBackground())
        counterChartPanel = ChartPanel(counterChart)
        counterChartPanel.setPreferredSize(Dimension(500, 175))
        sidePanel.add(counterChartPanel)
        self.scoreCountersCollection = TimeSeriesCollection()
        scoreCounterChart = ChartFactory.createTimeSeriesChart(None, None, "Score", self.scoreCountersCollection, True, True, False)
        scoreCounterChart.getXYPlot().getRangeAxis().setRange(0, 100)
        scoreCounterChart.setBackgroundPaint(getBackground())
        scoreCounterChartPanel = ChartPanel(scoreCounterChart)
        scoreCounterChartPanel.setPreferredSize(Dimension(500, 175))
        sidePanel.add(scoreCounterChartPanel)
        self.add(JScrollPane(self.moveTable, ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED, ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED), GridBagConstraints(0, 0, 1, 2, 1.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, Insets(0, 0, 0, 0), 0, 0))
        self.add(sidePanel, GridBagConstraints(1, 0, 1, 1, 1.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, Insets(0, 0, 0, 0), 0, 0))
        self.add(JButton(resetButtonMethod()), GridBagConstraints(1, 1, 1, 1, 0.0, 0.0, GridBagConstraints.SOUTHEAST, GridBagConstraints.NONE, Insets(0, 0, 0, 0), 0, 0))

    startedAdding = False

    def beginAddingDataPoints(self):
        """ generated source for method beginAddingDataPoints """
        if not self.startedAdding:
            AddDataPointThread().start()
            self.startedAdding = True

    @overloaded
    def observe(self, event):
        """ generated source for method observe """
        if isinstance(event, (GamerNewMatchEvent, )):
            self.observe(event)

    @observe.register(object, GamerNewMatchEvent)
    def observe_0(self, event):
        """ generated source for method observe_0 """
        model = self.moveTable.getModel()
        model.setRowCount(0)

    def addObservation(self, step, move, timeSpent, ranOut):
        """ generated source for method addObservation """
        model = self.moveTable.getModel()
        model.addRow([None]*)

    class Counter(object):
        """ generated source for class Counter """
        series = TimeSeries()

        def __init__(self, name, forScore):
            """ generated source for method __init__ """
            self.series = TimeSeries(name)
            self.series.setMaximumItemCount(36000)
            self.counters.add(self)
            if forScore:
                self.scoreCountersCollection.addSeries(self.series)
            else:
                self.countersCollection.addSeries(self.series)

        def getTimeSeries(self):
            """ generated source for method getTimeSeries """
            return self.series

        def consolidate(self):
            """ generated source for method consolidate """
            self.series.add(Millisecond(Date()), getValue())

        def getValue(self):
            """ generated source for method getValue """

        def clear(self):
            """ generated source for method clear """
            self.series.clear()

    class AggregatingCounter(Counter):
        """ generated source for class AggregatingCounter """
        value = float()

        def __init__(self, name, forScore):
            """ generated source for method __init__ """
            super(AggregatingCounter, self).__init__(forScore)
            self.value = 0

        def increment(self, by):
            """ generated source for method increment """
            self.value += by

        def getValue(self):
            """ generated source for method getValue """
            theValue = self.value
            self.value = 0
            return theValue if (theValue > 0) else None

    class FixedCounter(Counter):
        """ generated source for class FixedCounter """
        value = float()

        def __init__(self, name, forScore):
            """ generated source for method __init__ """
            super(FixedCounter, self).__init__(forScore)
            self.value = None

        def set(self, to):
            """ generated source for method set """
            self.value = to

        def getValue(self):
            """ generated source for method getValue """
            return self.value

    class AddDataPointThread(Thread):
        """ generated source for class AddDataPointThread """
        def run(self):
            """ generated source for method run """
            while True:
                self.memUsage.add(Millisecond(Date()), Runtime.getRuntime().totalMemory() / (1024 * 1024))
                self.memTotal.add(Millisecond(Date()), Runtime.getRuntime().maxMemory() / (1024 * 1024))
                for c in counters:
                    c.consolidate()
                repaint()
                try:
                    Thread.sleep(100)
                except InterruptedException as e:
                    e.printStackTrace()

    def resetButtonMethod(self):
        """ generated source for method resetButtonMethod """
        return AbstractAction("Reset Time Series")

