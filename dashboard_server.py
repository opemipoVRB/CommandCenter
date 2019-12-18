#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
↓↓...........................................................................↓↓
↓↓..........................↓↓↓↓↓↓↓↓↓↓↓↓↓....................................↓↓
↓↓.......................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.................................↓↓
↓↓.....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓...............................↓↓
↓↓....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.↓↓...............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓...↓↓..............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.↓↓...↓↓↓.............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..............................↓↓
↓↓....................↓↓↓↓↓↓↓↓↓↓↓↓↓.....↓↓↓↓↓↓↓↓↓............................↓↓
↓↓......................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..↓↓↓↓↓↓↓............................↓↓
↓↓...................................↓↓↓.....................................↓↓
↓↓.................↓↓................↓↓↓↓ ↓↓↓↓↓↓↓........↓...................↓↓
↓↓...............↓↓↓↓↓↓..............↓↓↓↓↓↓↓↓↓↓↓↓↓...↓↓↓↓↓↓..................↓↓
↓↓............↓↓↓↓..↓↓↓↓↓.........................↓↓↓↓↓↓↓↓↓..................↓↓
↓↓............↓↓↓↓...↓↓↓↓↓↓↓....................↓↓↓↓↓↓.↓↓.↓↓.................↓↓
↓↓...............↓↓↓↓↓↓↓↓↓↓↓↓↓↓............↓↓↓↓↓↓↓↓..........................↓↓
↓↓.........................↓↓↓↓↓↓↓↓↓...↓↓↓↓↓↓↓...............................↓↓
↓↓..............................↓↓↓↓↓↓↓↓↓↓...................................↓↓
↓↓..........................↓↓↓↓↓....↓↓↓↓↓↓↓↓↓...............................↓↓
↓↓............↓↓.↓↓↓↓↓↓↓↓↓↓↓↓↓............↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..................↓↓
↓↓............↓↓.↓↓..↓↓↓↓.....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓.................↓↓
↓↓..............↓↓↓↓↓↓............................↓↓.↓↓↓↓↓↓↓.................↓↓
↓↓..................                                   ......................↓↓
↓↓.................. ↑↑↑  ↑↑↑  ↑↑↑↑↑↑↑        ↑↑↑↑↑↑↑ .......................↓↓
↓↓.................. ↑↑↑  ↑↑↑  ↑↑↑   ↑↑↑↑     ↑↑↑   ↑↑↑↑.....................↓↓
↓↓.................. ↑↑↨  ↑↑↑  ↑↑↨   ↨↑↑      ↑↑↨   ↨↑↑......................↓↓
↓↓.................. ↨↑↨  ↑↨↑  ↨↑↨   ↨↑↨      ↨↑↨   ↨↑↨......................↓↓
↓↓.................. ↑↨↑  ↨↑↨  ↨↨↑↨↑↨↨↑↑↨     ↨↨↑↨↑↨↨↑↑↨.....................↓↓
↓↓.................. ↨↑↨  ↨↨↨  ↨↨↨      ↨↨↨   ↨↨↨     ↨↨↨....................↓↓
↓↓.................. :↨:  ↨↨:  ↨↨:      :↨↨   ↨↨:     :::....................↓↓
↓↓................... ::↨↨:↨   :↨:      :↨:   :↨:     :::....................↓↓
↓↓.................... ::::    :::      :::   :::     :::....................↓↓
↓↓...................... :      :        :      :::::::  ....................↓↓
↓↓...........................................................................↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓      dashboard_server.py  Created by  Durodola Opemipo 2019               ↓↓
↓↓            Personal Email : <opemipodurodola@gmail.com>                   ↓↓
↓↓                 Telephone Number: +2348182104309                          ↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓

"""
import json
from json import JSONDecodeError

from autobahn.twisted.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory

import sys
from twisted.python import log
from twisted.internet import reactor


class CommandCenterServerProtocol(WebSocketServerProtocol):
    connected_clients = []
    available_dashboards = {}

    def __init__(self):
        super(CommandCenterServerProtocol, self).__init__()
        self.processes = {
            "VERIFY-OPERATION": self.verify_operation,
            "INITIALIZATION": self.initialization,
            "LAUNCHING-SCREENS": self.launch_screen,
            "LAUNCHING-SCREENS-RESPONSE": self.launch_screen_response
        }
        self.process = "initialization"
        self.previous_process = None

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):

        """
          Callback fired when the initial WebSocket opening handshake was completed.
          You now can send and receive WebSocket messages.

          :return:

        """
        print("WebSocket connection open.")
        self.factory.register(self)
        print("Client connected: {0}".format(self.peer))
        print("Client connected: {0}".format(self))
        self.factory.communicate(self, "Connected to Command Center Network", True)
        print("Sent a message already...")

    def onMessage(self, payload, isBinary):
        """
       Callback fired when a message was received.
       :param payload:
       :param isBinary:
       :return:

        """
        # client is also self
        client = self
        # Send Response to every one

        print("First Message   ", payload)

        try:
            payload = payload.decode("utf-8")
            payload = json.loads(payload)

            try:
                self.process = payload["operation"]
            except KeyError:
                pass

            self.verify_operation(client, payload)

        except JSONDecodeError:
            self.send_private_message(client, {"warning": "Invalid message type, expected a message with protocol to "
                                                          "be initiated."})
        # print("Client {0} sending message: {1}".format(self.peer, payload))

    def verify_operation(self, client, data):

        """

        Verify Operation to be carried out and fire method from.

        :param client:
        :param data:
        :return:

        """
        response = "Verifying initiated operation by " + data["client"] + " client."

        if data["operation"] in self.processes:
            self.processes[data["operation"]](client, data)
        else:
            self.send_private_message(client, {"warning": "Invalid Operation, an unrecognised protocol was initiated"})
        return

    def initialization(self, client, data):
        """
        Initialization of clients.

        :param client:
        :param data:
        :return:

        """

        message = "This are the connected clients"
        print("Initialization of client {} ".format(client), data)

        client.__dict__.update({"module": data["client"]})

        if "dashboards" in data:
            self.get_dashboards(data)

        print("Available Dashboards ", self.available_dashboards)

        print("Connected clients", self.get_connected_clients())

        for c in self.factory.clients:
            print(str(client.__dict__) in str(c["client"].__dict__))
            if str(c["client"].__dict__) in str(client.__dict__):
                online_client = {
                    "client": c["client"].__dict__["module"],
                }
                print(online_client["client"], " just connected")
                self.update_connected_client(online_client)

        # Sent to Mobile device

        for c in self.factory.clients:
            response = {
                "message": message,
                "clients": self.get_connected_clients(),
                "dashboards": self.available_dashboards
            }
            self.send_private_message(c["client"], response)
            print("Private Message sent")

        print("This Clients are now Online ", self.connected_clients)
        self.initalized = True

        return

    @classmethod
    def get_dashboards(cls, data):
        cls.available_dashboards.update(data["dashboards"])
        return cls.available_dashboards

    @classmethod
    def update_connected_client(cls, clients):
        return cls.connected_clients.append(clients)

    @classmethod
    def update_disconnected_client(cls, clients):
        if not cls.connected_clients:
            cls.available_dashboards.clear()
        return cls.connected_clients.remove(clients)

    @classmethod
    def get_connected_clients(cls):
        return cls.connected_clients

    def launch_screen(self, client, data):
        print("Launch Screen")
        for c in self.factory.clients:
            if "CommandCenterScreenClient" in c["client"].__dict__["module"] and \
                    "LAUNCHING-SCREENS" in data["operation"]:
                self.send_private_message(c["client"], json.dumps(data))
        return

    def launch_screen_response(self, client, data):
        print("Launch Screen")
        self.send_broadcast_message(client, "Done")

        return

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))

    def connectionLost(self, reason):
        """
        Callback fired when the WebSocket connection has been closed
        (WebSocket closing handshake has been finished or the connection was closed uncleanly).
        :param reason:
        :return:

        """
        self.update_disconnected_client({"client": self.__dict__["module"]})
        print(self.__dict__["module"], "with IP address", self.peer, " disconnected ")
        self.factory.unregister(self)
        print(self.connected_clients)

    def send_private_message(self, client, message):
        """
        Response to a single client
        :param client:
        :param message:
        :return:

        """

        self.factory.communicate(client=client, payload=message, isBinary=True)

    def send_broadcast_message(self, client, message):
        """
        Broad cast a message

        :param client:
        :param message:
        :return:
        """
        self.factory.broadcast_communicate(client=client, payload=message, isBinary=True)


class CommandCenterFactory(WebSocketServerFactory):

    def __init__(self, *args, **kwargs):
        super(CommandCenterFactory, self).__init__(*args, **kwargs)
        self.clients = []

    def register(self, client):
        self.clients.append({"client-peer": client.peer, "client": client})

    def unregister(self, client):
        for c in self.clients:
            if c["client-peer"] == client.peer:
                self.clients.remove(c)

    def broadcast_communicate(self, client, payload, isBinary):
        for i, c in enumerate(self.clients):
            if c["client"] == client:
                id = i
                break
        for c in self.clients:
            try:
                msg = "{0}".format(payload.decode("utf-8"))
            except AttributeError:
                msg = "{0}".format(payload)
            c["client"].sendMessage(str.encode(msg))

    def communicate(self, client, payload, isBinary):
        for i, c in enumerate(self.clients):
            if c["client"] == client:
                id = i
                break
        for c in self.clients:
            # print("This are the present clients   -->", c)
            if c["client"] == client:
                # print("Sending message to ", client)
                try:
                    msg = "{0}".format(payload.decode("utf-8"))
                except AttributeError:
                    msg = "{0}".format(payload)
                c["client"].sendMessage(str.encode(msg))


if __name__ == "__main__":

    # log.startLogging(sys.stdout)

    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        log.startLogging(sys.stdout)
        debug = True
    else:
        debug = False

    factory = CommandCenterFactory(u"ws://0.0.0.0:3233")
    factory.protocol = CommandCenterServerProtocol
    # factory.setProtocolOptions(maxConnections=2)

    # note to self: if using putChild, the child must be bytes...

    reactor.listenTCP(3233, factory)
    print("Command Center Server started on port %s" % (3233,))
reactor.run()
