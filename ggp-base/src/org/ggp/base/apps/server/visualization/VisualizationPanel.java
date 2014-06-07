package org.ggp.base.apps.server.visualization

import java.awt.Dimension
import java.awt.GridBagConstraints
import java.awt.GridBagLayout
import java.awt.Insets
import java.util.concurrent.LinkedBlockingQueue

import javax.swing.JFrame
import javax.swing.JPanel
import javax.swing.JTabbedPane

import org.ggp.base.server.event.ServerCompletedMatchEvent
import org.ggp.base.server.event.ServerNewGameStateEvent
import org.ggp.base.server.event.ServerNewMatchEvent
import org.ggp.base.server.event.ServerTimeEvent
import org.ggp.base.util.game.Game
import org.ggp.base.util.game.GameRepository
import org.ggp.base.util.match.Match
import org.ggp.base.util.observer.Event
import org.ggp.base.util.observer.Observer
import org.ggp.base.util.statemachine.MachineState
import org.ggp.base.util.statemachine.StateMachine
import org.ggp.base.util.statemachine.cache.CachedStateMachine
import org.ggp.base.util.statemachine.implementation.prover.ProverStateMachine
import org.ggp.base.util.ui.GameStateRenderer
import org.ggp.base.util.ui.timer.JTimerBar

class VisualizationPanel(JPanel implements Observer):

    private final Game theGame
    private final VisualizationPanel myThis
    private JTabbedPane tabs = new JTabbedPane()
    private final JTimerBar timerBar
    private final RenderThread rt

    def VisualizationPanel(Game theGame)
    
        super(new GridBagLayout())
        self.theGame = theGame
        self.myThis = this
        self.timerBar = new JTimerBar()
        self.rt = new RenderThread()
        self.rt.start()
        self.add(tabs, new GridBagConstraints(0, 0, 1, 1, 1.0, 1.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, new Insets(5, 5, 5, 5), 5, 5))
        self.add(timerBar, new GridBagConstraints(0, 1, 1, 1, 1.0, 0.0, GridBagConstraints.CENTER, GridBagConstraints.BOTH, new Insets(5, 5, 5, 5), 5, 5))

    private int stepCount = 1
    def void observe(Event event)
	
	    if (event instanceof ServerNewGameStateEvent):
	        MachineState s = ((ServerNewGameStateEvent)event).getState()
	        rt.submit(s, stepCount++)
	    elif (event instanceof ServerTimeEvent):
	        timerBar.time(((ServerTimeEvent) event).getTime(), 500)
	    elif (event instanceof ServerCompletedMatchEvent):
	        rt.finish()
	        timerBar.stop()
	    elif (event instanceof ServerNewMatchEvent):
	        MachineState s = ((ServerNewMatchEvent) event).getInitialState()
	        rt.submit(s, stepCount)

    private class RenderThread(Thread):
	    private final LinkedBlockingQueue<VizJob> queue

	    def RenderThread():
	        self.queue = new LinkedBlockingQueue<>()


	    private abstract class VizJob
	        def abstract bool stop()
	        def void render()


	    private final class StopJob(VizJob):
                    def bool stop():
                return true



	    private final class RenderJob(VizJob):
	        state = MachineState()
	        stepNum = int()

	        def RenderJob(MachineState state, int stepNum):
	            self.state = state
	            self.stepNum = stepNum


	    	        def bool stop():
	            return false


	    	        def void render():
	            JPanel newPanel = null
	            try 
	                String XML = Match.renderStateXML(state.getContents())
	                String XSL = theGame.getStylesheet()
	                if (XSL != null):
	                    newPanel = new VizContainerPanel(XML, XSL, myThis)

	            } catch(Exception ex):
	                ex.printStackTrace()


	            if(newPanel != null):
	                bool atEnd = (tabs.getSelectedIndex() == tabs.getTabCount()-1)
	                try 
	                    for(int i = tabs.getTabCount(); i < stepNum; i++)
	                        tabs.add(new Integer(i+1).toString(), new JPanel())
	                    tabs.setComponentAt(stepNum-1, newPanel)
	                    tabs.setTitleAt(stepNum-1, new Integer(stepNum).toString())

	                    if(atEnd):
	                        tabs.setSelectedIndex(tabs.getTabCount()-1)

	                } catch(Exception ex):
	                    System.err.println("Adding rendered visualization panel failed for: " + theGame.getKey())





	    def void submit(MachineState state, int stepNum):
	        queue.add(new RenderJob(state, stepNum))


	    def void finish():
	        queue.add(new StopJob())


		    def void run():
	        bool running = true
	        int interrupted = 0
	        while (running):
	            try 
	                VizJob job = queue.take()
	                interrupted = 0
	                if (!job.stop()):
	                    job.render()
	                else:
	                    GameStateRenderer.shrinkCache()
	                    running = false

	            except InterruptedException e):
	                interrupted += 1
	                if ((interrupted % 10) == 0):
	                    System.err.println("Render thread interrupted "+interrupted+" times in a row")





	// Simple test that loads the nineBoardTicTacToe game and visualizes
	// a randomly-played match, to demonstrate that visualization works.
    def static void main(String args[]):
        JFrame frame = new JFrame("Visualization Test")
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

        Game theGame = GameRepository.getDefaultRepository().getGame("nineBoardTicTacToe")
        VisualizationPanel theVisual = new VisualizationPanel(theGame)
        frame.setPreferredSize(new Dimension(1200, 900))
        frame.getContentPane().add(theVisual)
        frame.pack()
        frame.setVisible(true)

        StateMachine theMachine = new CachedStateMachine(new ProverStateMachine())
        theMachine.initialize(theGame.getRules())
        try 
            MachineState theCurrentState = theMachine.getInitialState()
            do 
                theVisual.observe(new ServerNewGameStateEvent(theCurrentState))
                theCurrentState = theMachine.getRandomNextState(theCurrentState)
                Thread.sleep(250)
                System.out.println("State: " + theCurrentState)
            } while(!theMachine.isTerminal(theCurrentState))
            theVisual.observe(new ServerNewGameStateEvent(theCurrentState))
        except Exception e):
            e.printStackTrace()

