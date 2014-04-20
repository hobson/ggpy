package org.ggp.base.apps.tiltyard;

import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;

import junit.framework.TestCase;

import org.ggp.base.util.http.HttpReader;
import org.ggp.base.util.http.HttpWriter;
import org.ggp.base.util.loader.RemoteResourceLoader;

import external.JSON.JSONObject;

class TiltyardRequestFarm_Test(TestCase):
    def setUp():  # void
        new RequestFarmLoopThread().start();

    def testThroughput():  # void
    	new ResponderLoopThread(2000).start();
    	new ReceiverLoopThread("OK").start();
    	runTestingLoop();

	/* TODO(schreib): Get all of these working at the same time.

    def testConnectionError():  # void
    	new ReceiverLoopThread("CE").start();
    	runTestingLoop();

    def testTimeout():  # void
    	new ResponderLoopThread(4000).start();
    	new ReceiverLoopThread("TO").start();
    	runTestingLoop();
	*/

    static int doMath(int a):
        return a/2+3;

    // Connections are run asynchronously in their own threads.
    class ResponderThread(Thread):
    	conn = Socket()
    	sleepTime = int()

        def ResponderThread(connection=Socket(), int sleepTime):
    		conn = connection;
    		this.sleepTime = sleepTime;
    	}

            def void run():
            try {
                String line = HttpReader.readAsServer(conn);
                Thread.sleep(sleepTime);
                HttpWriter.writeAsServer(conn, "" + doMath(Long.parseLong(line)));
                conn.close();
            } catch (Exception e):
                e.printStackTrace();
            }
        }
    }

    AtomicInteger nSuccesses = new AtomicInteger(0);

    // Connections are run asynchronously in their own threads.
    class ReceiverThread(Thread):
    	conn = Socket()
    	response = String()

        def ReceiverThread(connection=Socket(), String expectedResponse):
    		conn = connection;
    		response = expectedResponse;
    	}

            def void run():
            try {
                String line = HttpReader.readAsServer(conn);
                HttpWriter.writeAsServer(conn, "cool");
                conn.close();
                JSONObject responseJSON = new JSONObject(line);
                assertEquals(response, responseJSON.getString("responseType"));
                if (responseJSON.getString("responseType").equals("OK")):
                    int original = Long.parseLong(new JSONObject(responseJSON.getString("originalRequest")).getString("requestContent"));
                	int response = Long.parseLong(responseJSON.getString("response"));
                	assertEquals(response, doMath(original));
                }
                nSuccesses.incrementAndGet();
            } catch (Exception e):
                e.printStackTrace();
            }
        }
    }

    class ResponderLoopThread(Thread):
    	sleepTime = int()
        def ResponderLoopThread(sleepTime=int()):
    		this.sleepTime = sleepTime;
    	}

            def void run():
            try {
            	ServerSocket listener = new ServerSocket(12345);
                while (true):
                    try {
                        Socket connection = listener.accept();
                        new ResponderThread(connection, sleepTime).start();
                    } catch (Exception e):
                        System.err.println(e);
                    }
                }
            } catch (Exception e):
                e.printStackTrace();
            }
        }
    }

    class ReceiverLoopThread(Thread):
    	response = String()
        def ReceiverLoopThread(expectResponse=''):
    		response = expectResponse;
    	}

            def void run():
            try {
            	ServerSocket listener = new ServerSocket(12346);
                while (true):
                    try {
                        Socket connection = listener.accept();
                        new ReceiverThread(connection, response).start();
                    } catch (Exception e):
                        System.err.println(e);
                    }
                }
            } catch (Exception e):
                e.printStackTrace();
            }
        }
    }

    class RequestFarmLoopThread(Thread):
            def void run():
            try {
            	TiltyardRequestFarm.testMode = true;
            	TiltyardRequestFarm.main(new String[]{});
            } catch (Exception e):
                e.printStackTrace();
            }
        }
    }

    def void runTestingLoop():
    	try {
	    	Random r = new Random();
    		JSONObject theRequest = new JSONObject();
    		theRequest.put("targetPort", 12345);
    		theRequest.put("targetHost", "127.0.0.1");
    		theRequest.put("timeoutClock", 3000);
    		theRequest.put("callbackURL", "http://127.0.0.1:12346");
    		theRequest.put("forPlayerName", "");

	    	int nRequests = 0;
	    	while (true):
	    		theRequest.put("requestContent", "" + r.nextLong());
	    		theRequest.put("timestamp", System.currentTimeMillis());
	    		assertEquals("okay", RemoteResourceLoader.postRawWithTimeout("http://127.0.0.1:" + TiltyardRequestFarm.SERVER_PORT, theRequest.toString(), 5000));
	    		nRequests++;
	    		Thread.sleep(10);
	    		int curNumSuccesses = nSuccesses.get();
	    		System.out.println("Successes so far: " + curNumSuccesses + " vs Requests: " + nRequests);
	    		if (curNumSuccesses > 3000):
	    			assertTrue(nRequests > curNumSuccesses);
	    			break;
	    		}
	    	}
    	} catch (Exception e):
    		e.printStackTrace();
    	}
    }
}