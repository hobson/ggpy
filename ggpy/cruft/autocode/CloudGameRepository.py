#!/usr/bin/env python
""" generated source for module CloudGameRepository """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

# package: org.ggp.base.util.game
import java.io.BufferedReader

import java.io.File

import java.io.FileInputStream

import java.io.FileOutputStream

import java.io.InputStreamReader

import java.io.PrintWriter

import java.security.MessageDigest

import java.util.HashMap

import java.util.HashSet

import java.util.Map

import java.util.Set

import java.util.zip.GZIPInputStream

import java.util.zip.GZIPOutputStream

import external.JSON.JSONObject

# 
#  * Cloud game repositories provide access to game resources stored on game
#  * repository servers on the web, while continuing to work while the user is
#  * offline through aggressive caching based on the immutability + versioning
#  * scheme provided by the repository servers.
#  *
#  * Essentially, each game has a version number stored in the game metadata
#  * file. Game resources are immutable until this version number changes, at
#  * which point the game needs to be reloaded. Version numbers are passed along
#  * and stored in the match descriptions, and repository servers will continue
#  * to serve old versions when specifically requested, so it is valid to use any
#  * historical game version when generating a match -- this is why we don't need
#  * to worry about our offline cache becoming stale/invalid. However, to stay up
#  * to date with the latest bugfixes, etc, we aggressively refresh the cache any
#  * time we can connect to the repository server, as a matter of policy.
#  *
#  * Cached games are stored locally, in a directory managed by this class. These
#  * files are compressed, to decrease their footprint on the local disk. GGP Base
#  * has its SVN rules set up so that these caches are ignored by SVN.
#  *
#  * @author Sam
#  
class CloudGameRepository(GameRepository):
    """ generated source for class CloudGameRepository """
    theRepoURL = str()
    theCacheDirectory = File()
    needsRefresh = True

    def __init__(self, theURL):
        """ generated source for method __init__ """
        super(CloudGameRepository, self).__init__()
        self.theRepoURL = RemoteGameRepository.properlyFormatURL(theURL)
        #  Generate a unique hash of the repository URL, to use as the
        #  local directory for files for the offline cache.
        theCacheHash = StringBuilder()
        try:
            while len(theDigest):
                theCacheHash.append(Math.abs(theDigest[i]))
                i += 1
        except Exception as e:
            theCacheHash = None
        theCachesDirectory = File(System.getProperty("user.home"), ".ggpserver-gamecache")
        theCachesDirectory.mkdir()
        self.theCacheDirectory = File(theCachesDirectory, "repoHash" + theCacheHash)
        if self.theCacheDirectory.exists():
            #  For existing caches, only force a full refresh at most once per day
            self.needsRefresh = (System.currentTimeMillis() - self.theCacheDirectory.lastModified()) > 86400000
        else:
            self.theCacheDirectory.mkdir()
            self.needsRefresh = True
        if self.needsRefresh:
            refreshThread.start()
            #  Update the game cache asynchronously if there are already games.
            #  Otherwise, force a blocking update.
            if len(length):
                try:
                    refreshThread.join()
                except InterruptedException as e:
            self.theCacheDirectory.setLastModified(System.currentTimeMillis())
            self.needsRefresh = False

    def getUncachedGameKeys(self):
        """ generated source for method getUncachedGameKeys """
        theKeys = HashSet()
        for game in theCacheDirectory.listFiles():
            theKeys.add(game.__name__.replace(".zip", ""))
        return theKeys

    def getUncachedGame(self, theKey):
        """ generated source for method getUncachedGame """
        cachedGame = loadGameFromCache(theKey)
        if cachedGame != None:
            return cachedGame
        #  Request the game directly on a cache miss.
        return RemoteGameRepository(self.theRepoURL).getGame(theKey)

    #  ================================================================
    #  Games are cached asynchronously in their own threads.
    class RefreshCacheForGameThread(Thread):
        """ generated source for class RefreshCacheForGameThread """
        theRepository = RemoteGameRepository()
        theKey = str()

        def __init__(self, a, b):
            """ generated source for method __init__ """
            super(RefreshCacheForGameThread, self).__init__()
            self.theRepository = a
            self.theKey = b

        def run(self):
            """ generated source for method run """
            try:
                if myGameVersion != None:
                    myVersionedRepoURL = myGameVersion.getRepositoryURL()
                if not versionedRepoURL == myVersionedRepoURL:
                    #  Cache miss: we don't have the current version for
                    #  this game, and so we need to load it from the web.
                    saveGameToCache(self.theKey, theGame)
            except Exception as e:
                e.printStackTrace()

    class RefreshCacheThread(Thread):
        """ generated source for class RefreshCacheThread """
        theRepoURL = str()

        def __init__(self, theRepoURL):
            """ generated source for method __init__ """
            super(RefreshCacheThread, self).__init__()
            self.theRepoURL = theRepoURL

        def run(self):
            """ generated source for method run """
            try:
                #  Sleep for the first two seconds after which the cache is loaded,
                #  so that we don't interfere with the user interface startup.
                Thread.sleep(2000)
            except InterruptedException as e:
                e.printStackTrace()
                return
            remoteRepository = RemoteGameRepository(self.theRepoURL)
            print "Updating the game cache..."
            beginTime = System.currentTimeMillis()
            #  Since games are immutable, we can guarantee that the games listed
            #  by the repository server includes the games in the local cache, so
            #  we can be happy just updating/refreshing the listed games.
            theGameKeys = remoteRepository.getGameKeys()
            if theGameKeys == None:
                return
            #  If the server offers a single combined metadata file, download that
            #  and use it to avoid checking games that haven't gotten new versions.
            bundledMetadata = remoteRepository.getBundledMetadata()
            if bundledMetadata != None:
                for theKey in theGameKeys:
                    try:
                        if myGameVersion == None:
                            continue 
                        #  Skip updating the game cache entry if the version is the same
                        #  and the cache entry was written less than a week ago.
                        if myGameVersion.getRepositoryURL() == remoteVersionedGameURL and getCacheEntryAge(theKey) < 604800000:
                            unchangedKeys.add(theKey)
                    except Exception as e:
                        continue 
                theGameKeys.removeAll(unchangedKeys)
            #  Start threads to update every entry in the cache (or at least verify
            #  that the entry doesn't need to be updated).
            theThreads = HashSet()
            for gameKey in theGameKeys:
                t.start()
                theThreads.add(t)
            #  Wait until we've updated the cache before continuing.
            for t in theThreads:
                try:
                    t.join()
                except InterruptedException as e:
            endTime = System.currentTimeMillis()
            print "Updating the game cache took: " + (endTime - beginTime) + "ms."

    #  ================================================================
    @synchronized
    def saveGameToCache(self, theKey, theGame):
        """ generated source for method saveGameToCache """
        if theGame == None:
            return
        theGameFile = File(self.theCacheDirectory, theKey + ".zip")
        try:
            theGameFile.createNewFile()
            pw.print_(theGame.serializeToJSON())
            pw.flush()
            pw.close()
            gOut.close()
            fOut.close()
        except Exception as e:
            e.printStackTrace()

    @synchronized
    def loadGameFromCache(self, theKey):
        """ generated source for method loadGameFromCache """
        theGameFile = File(self.theCacheDirectory, theKey + ".zip")
        theLine = None
        try:
            theLine = br.readLine()
            br.close()
            ir.close()
            gIn.close()
            fIn.close()
        except Exception as e:
        if theLine == None:
            return None
        return Game.loadFromJSON(theLine)

    @synchronized
    def getCacheEntryAge(self, theKey):
        """ generated source for method getCacheEntryAge """
        theGameFile = File(self.theCacheDirectory, theKey + ".zip")
        if theGameFile.exists():
            return System.currentTimeMillis() - theGameFile.lastModified()
        return System.currentTimeMillis()

    #  ================================================================
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        theRepository = CloudGameRepository("games.ggp.org/base")
        beginTime = System.currentTimeMillis()
        theGames = HashMap()
        for gameKey in theRepository.getGameKeys():
            theGames.put(gameKey, theRepository.getGame(gameKey))
        print "Games: " + len(theGames)
        endTime = System.currentTimeMillis()
        print "Time: " + (endTime - beginTime) + "ms."


if __name__ == '__main__':
    import sys
    CloudGameRepository.main(sys.argv)

