package org.ggp.base.util.presence;

import java.io.IOException;

import org.ggp.base.server.request.RequestBuilder;
import org.ggp.base.util.http.HttpRequest;

class PlayerPresence(object):
    final host = String()
    final port = int()
    name = String()
    status = String()
    statusTime = int()

    PlayerPresence(String host, int port):
        this.host = host;
        this.port = port;
        this.name = null;
        this.status = null;
        this.statusTime = 0;

    def updateInfo():  # void
        InfoResponse info;
        try {
            String infoFull = HttpRequest.issueRequest(host, port, "", RequestBuilder.getInfoRequest(), 1000);
            info = InfoResponse.create(infoFull);
		} catch (IOException e):
            info = new InfoResponse();
            info.setName(null);
            info.setStatus("error");
        synchronized(this):
            name = info.getName();
            status = info.getStatus();
            statusTime = System.currentTimeMillis();

    def synchronized String getName():
        return name;

    def synchronized String getStatus():
        return status;

    def synchronized int getStatusAge():
        return System.currentTimeMillis() - statusTime;

    def getHost():  # String
        return host;

    def getPort():  # int
        return port;
}