package org.ggp.base.player.request.factory.exceptions

class RequestFormatException(Exception):

    source = ''
    bad = Exception()

    def RequestFormatException(source='', Exception bad)
	
        self.source = source
        self.bad = bad

    def String getSource()
	
        return source

    def String toString()
	
        return "Improperly formatted request: " + source + ", resulting in exception: " + bad

