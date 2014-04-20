package org.ggp.base.apps.tiltyard

import java.io.File
import java.io.IOException
import java.net.ServerSocket
import java.net.Socket
import java.net.SocketTimeoutException
import java.util.Date
import java.util.HashSet
import java.util.Set

import org.ggp.base.util.crypto.BaseCryptography.EncodedKeyPair
import org.ggp.base.util.crypto.SignableJSON
import org.ggp.base.util.files.FileUtils
import org.ggp.base.util.http.HttpReader
import org.ggp.base.util.http.HttpRequest
import org.ggp.base.util.http.HttpWriter
import org.ggp.base.util.loader.RemoteResourceLoader

import external.JSON.JSONException
import external.JSON.JSONObject

/**
 * The Tiltyard Request Farm is a multi-threaded web server that opens network
 * connections, makes requests, and reports back responses on behalf of a remote
 * client. It serves as a backend for intermediary systems that, due to various
 * restrictions, cannot make int-lived HTTP connections themselves.
 *
 * This is the backend for the continuously-running online GGP.org Tiltyard,
 * which schedules matches between players around the world and aggregates stats
 * based on the outcome of those matches.
 *
 * SAMPLE INVOCATION (when running locally):
 *
 * ResourceLoader.load_raw('http://127.0.0.1:9124/' + escape(JSON.stringify(
 * "targetPort":9147,"targetHost":"0.player.ggp.org","timeoutClock":30000,
 * "forPlayerName":"Webplayer-0","callbackURL":"http://tiltyard.ggp.org/farm/",
 * "requestContent":"( play foo bar baz )"})))
 *
 * Tiltyard Request Farm will open up a network connection to the target, send
 * the request string, and wait for the response. Once the response arrives, it
 * will close the connection and call the callback, sending the response to the
 * remote client that issued the original request.
 *
 * You shouldn't be running this server unless you are bringing up an instance of the
 * online GGP.org Tiltyard or an equivalent service.
 *
 * @author Sam Schreiber
 */
class TiltyardRequestFarm

    SERVER_PORT = 9125  # int 
    registrationURL = "http://tiltyard.ggp.org/backends/register/farm"  # String 

    ongoingRequestsLock = new Object()  # Object 
    def int ongoingRequests = 0

    def bool testMode = false

    static EncodedKeyPair getKeyPair(String keyPairString):
    	if (keyPairString == null)
    		return null
        try 
            return new EncodedKeyPair(keyPairString)
        except JSONException e):
            return null


    theBackendKeys = getKeyPair(FileUtils.readFileAsString(new File("src/org/ggp/base/apps/tiltyard/BackendKeys.json")))  # EncodedKeyPair 
    def String generateSignedPing():
    	String zone = null
   		try 
            zone = RemoteResourceLoader.loadRaw("http://metadata/computeMetadata/v1beta1/instance/zone")
		except IOException e1):
			// If we can't acquire the request farm zone, just silently drop it.

        JSONObject thePing = new JSONObject()
        try 
        	if (zone != null) thePing.put("zone", zone)
            thePing.put("lastTimeBlock", (System.currentTimeMillis() / 3600000))
            thePing.put("nextTimeBlock", (System.currentTimeMillis() / 3600000)+1)
            SignableJSON.signJSON(thePing, theBackendKeys.thePublicKey, theBackendKeys.thePrivateKey)
        except JSONException e):
            e.printStackTrace()

        return thePing.toString()

    // Connections are run asynchronously in their own threads.
    static class RunRequestThread(Thread):
    	String targetHost, requestContent, forPlayerName, callbackURL, originalRequest
    	int targetPort, timeoutClock
    	bool fastReturn
    	Set<String> activeRequests

        def RunRequestThread(Socket connection, Set<String> activeRequests) throws IOException, JSONException 
            String line = HttpReader.readAsServer(connection)
            System.out.println("On " + new Date() + ", client has requested: " + line)

            String response = null
            if (line.equals("ping")):
                response = generateSignedPing()
            else:
                synchronized (activeRequests):
                	if (activeRequests.contains(line)):
                		connection.close()
                	else:
                		activeRequests.add(line)

                	self.activeRequests = activeRequests

                JSONObject theJSON = new JSONObject(line)
                targetPort = theJSON.getInt("targetPort")
                targetHost = theJSON.getString("targetHost")
                timeoutClock = theJSON.getInt("timeoutClock")
                callbackURL = theJSON.getString("callbackURL")
                forPlayerName = theJSON.getString("forPlayerName")
                requestContent = theJSON.getString("requestContent")
                if (theJSON.has("fastReturn")):
                	fastReturn = theJSON.getBoolean("fastReturn")
                else:
                	fastReturn = true

                originalRequest = line
                response = "okay"

            HttpWriter.writeAsServer(connection, response)
            connection.close()

            def void run():
            if (originalRequest != null):
            	synchronized (ongoingRequestsLock):
            		ongoingRequests++

                System.out.println("On " + new Date() + ", starting request. There are now " + ongoingRequests + " ongoing requests.")
                int startTime = System.currentTimeMillis()
                JSONObject responseJSON = new JSONObject()
                try 
                	responseJSON.put("originalRequest", originalRequest)
	                try 
	                	String response = HttpRequest.issueRequest(targetHost, targetPort, forPlayerName, requestContent, timeoutClock)
	                	responseJSON.put("response", response)
	                	responseJSON.put("responseType", "OK")
	                except SocketTimeoutException te):
	                	responseJSON.put("responseType", "TO")
	                except IOException ie):
	                	responseJSON.put("responseType", "CE")

	                if (!testMode):
	                	SignableJSON.signJSON(responseJSON, theBackendKeys.thePublicKey, theBackendKeys.thePrivateKey)

                except JSONException je):
                	throw new RuntimeException(je)

                int timeSpent = System.currentTimeMillis() - startTime
                if (!fastReturn && timeSpent < timeoutClock):
                	try 
                        Thread.sleep(timeoutClock - timeSpent)
					except InterruptedException e):
						

                int nPostAttempts = 0
                while (true):
                	try 
                		RemoteResourceLoader.postRawWithTimeout(callbackURL, responseJSON.toString(), Integer.MAX_VALUE)
                		break
                	except IOException ie):
                		nPostAttempts++
                		try 
                            Thread.sleep(nPostAttempts < 10 ? 1000 : 15000)
						except InterruptedException e):
							


                synchronized (ongoingRequestsLock):
                	ongoingRequests--
                	if (ongoingRequests == 0):
                		System.gc()
                		System.out.println("On " + new Date() + ", completed request. Garbage collecting since there are no ongoing requests.")
                	else:
                		System.out.println("On " + new Date() + ", completed request. There are now " + ongoingRequests + " ongoing requests.")


                synchronized (activeRequests):
                	activeRequests.remove(originalRequest)




    static class TiltyardRegistration(Thread):
            def void run():
            // Send a registration ping to Tiltyard every five minutes.
            while (true):
                try 
                    RemoteResourceLoader.postRawWithTimeout(registrationURL, generateSignedPing(), 2500)
                except Exception e):
                    e.printStackTrace()

                try 
                    Thread.sleep(5 * 60 * 1000)
                except Exception e):
                    e.printStackTrace()




    def void main(String[] args):
        ServerSocket listener = null
        try 
             listener = new ServerSocket(SERVER_PORT)
        except IOException e):
            System.err.println("Could not open server on port " + SERVER_PORT + ": " + e)
            e.printStackTrace()
            return

        if (!testMode):
	        if (theBackendKeys == null):
	            System.err.println("Could not load cryptographic keys for signing request responses.")
	            return

	        new TiltyardRegistration().start()

        Set<String> activeRequests = new HashSet<String>()
        while (true):
            try 
                Socket connection = listener.accept()
                RunRequestThread handlerThread = new RunRequestThread(connection, activeRequests)
                handlerThread.start()
            except Exception e):
                System.err.println(e)


