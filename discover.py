#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import struct
import sys

from protocol import Answer, Request

__author__ = 'Anthony GELIBERT <anthony.gelibert@me.com>'
__date__ = 'June 6, 2013'
__version__ = '1.0.1'

def main():
    """ Start the listener and send periodically broadcast messages """
    print("\x1b[38;1mFosCam Revealer v" + __version__)
    print("======================\x1b[0m")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", 10000))
    print("\x1b[33;1m[INFO] Send a broadcast message")
    sock.sendto(Request.getAsBytesArray(), ("255.255.255.255", 10000))
    print("\x1b[33;1m[INFO] Wait for answers\x1b[0m")
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print("\x1b[33;1m[INFO] Message received…\x1b[0m")
            try:
                print("\x1b[32;1m" + Answer.frombuffer(data).__str__()
                      + "\x1b[0m")
            except struct.error:
                print("\x1b[31;1m[ERROR] Not a camera...\x1b[0m")
                pass
        except KeyboardInterrupt:
            print("\x1b[31;1m[WARNING] Exit requested…\x1b[0m")
            break


if __name__ == "__main__":
    sys.exit(main())
