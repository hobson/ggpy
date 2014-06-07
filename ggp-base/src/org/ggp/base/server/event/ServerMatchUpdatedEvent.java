package org.ggp.base.server.event

import org.ggp.base.util.match.Match
import org.ggp.base.util.observer.Event

class ServerMatchUpdatedEvent(Event):
    match = Match()
    externalPublicationKey = ''
    externalFilename = ''

    def ServerMatchUpdatedEvent(match=Match(), String externalPublicationKey, String externalFilename):
        self.match = match
        self.externalFilename = externalFilename
        self.externalPublicationKey = externalPublicationKey

    def getMatch():  # Match
        return match

    def getExternalFilename():  # String
        return externalFilename

    def getExternalPublicationKey():  # String
        return externalPublicationKey
