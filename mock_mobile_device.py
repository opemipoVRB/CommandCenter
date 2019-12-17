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
↓↓      mock_mobile_device.py  Created by  Durodola Opemipo 2019             ↓↓
↓↓            Personal Email : <opemipodurodola@gmail.com>                   ↓↓
↓↓                 Telephone Number: +2348182104309                          ↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓


"""

import json
import random

import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time


class MobileClient:
    """

    Mobile Client Interface

    """

    def __init__(self, ):
        websocket.enableTrace(False)
        ws = websocket.WebSocketApp("ws://165.227.90.19:3233/",
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)

        # ws = websocket.WebSocketApp("ws://localhost:3233/",
        #                             on_message=self.on_message,
        #                             on_error=self.on_error,
        #                             on_close=self.on_close)
        # ws = websocket.WebSocketApp("ws://192.168.0.12:3233/",
        #                             on_message=self.on_message,
        #                             on_error=self.on_error,
        #                             on_close=self.on_close)
        self.mode = "initialize"

        self.ws = ws
        self.ws.on_open = self.on_open
        while True:
            self.ws.run_forever()

    def on_message(self, message):
        if "Connected to Command Center Network" in message:
            print(message)

            self.ws.send(json.dumps(
                {
                    "username": "Isaac",
                    "command_center_id": "vgg_occ",
                    "session_id": "VI2019CE",
                    "id": "iPhoneXS",
                    "operation": "INITIALIZATION",
                    "client": "MobileDevice"
                }
            )
            )
        else:
            print(message)

        return message

    def on_error(self, error):

        return error

    def on_close(self):
        print("### closed ###")

    def run(self, *args):
        global driver
        driver = True
        while driver:
            try:
                time.sleep(1)
                print("Get Dashboards")
                urls_one = [
                    "https://flightaware.com/live/map",
                    "https://flightaware.com/adsb/stats/user/EbenezerOg#stats-34294",
                ]

                urls_two = [
                    "http://127.0.0.1:5000/#/2",
                    "https://apply.abudlc.edu.ng/api/",
                    "http://127.0.0.1:5000/#/3/3",
                    "http://127.0.0.1:5000/#/4/3"
                ]

                screen_object = {
                    "operation": "LAUNCHING-SCREENS",
                    "client": "MobileDevice",
                    "config_screen_one":
                        [
                            {"screen": "1", "url": urls_one[0]},
                            {"screen": "2", "url": urls_one[1]},

                        ],
                    "config_screen_two":
                        [
                            {"screen": "1", "url": urls_two[0]},
                            {"screen": "2", "url": urls_two[1]},
                            {"screen": "3", "url": urls_two[2]},
                            {"screen": "4", "url": urls_two[3]}
                        ]
                }

                send = input("Type \" send\" to send dashboards.\n:::>>")
                if send == "send":
                    screen_object = json.dumps(screen_object)
                    print(type(screen_object))
                    self.ws.send(screen_object)
            except KeyboardInterrupt:
                driver = False
        time.sleep(1)
        self.ws.close()
        print("thread terminating...")

    def on_open(self):
        self.mode = "run"
        if self.mode == "run":
            thread.start_new_thread(self.run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    onyx_client = MobileClient()
