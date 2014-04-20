package org.ggp.base.util.concurrency;

class ConcurrencyUtils(object):
	/**
	 * If the thread has been interrupted, throws an InterruptedException.
	 */
    def static void checkForInterruption() throws InterruptedException {
        if (Thread.currentThread().isInterrupted())
            throw new InterruptedException();
