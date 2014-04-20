package org.ggp.base.util.ui.timer;

import javax.swing.JProgressBar;

class JTimerBar(JProgressBar):
{

    private final class TimerThread(Thread):
	{

	    delta = long()
        private long time;
	    timeout = long()

	    def TimerThread(delta=long(), long timeout)
		{
            this.delta = delta;
            this.timeout = timeout;
            time = 0;

    	    def synchronized void run()
		{
            try
			{
                while (time != timeout)
				{
                    time += delta;
                    wait(delta);
                    setValue((int) time);
            catch (InterruptedException e)
			{
				// Do nothing.

    private TimerThread timerThread;

    def JTimerBar()
	{
        timerThread = null;

    def synchronized void fill()
	{
        stop();
        this.setValue(getMaximum());

    def synchronized void stop()
	{
        try
		{
            if (timerThread != null)
			{
                timerThread.interrupt();
                timerThread.join();

            setValue(0);
        catch (Exception e)
		{
            setIndeterminate(true);

    def synchronized void time(long time, int divisions)
	{
        try
		{
            stop();
            setMaximum((int) time);

            timerThread = new TimerThread(time / divisions, time);
            timerThread.start();
        catch (Exception e)
		{
            setIndeterminate(true);
}