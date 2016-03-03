#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

__author__ = 'Anthony GELIBERT <anthony.gelibert@me.com>'
__date__ = 'June 6, 2013'

class Request(object):
    """ Request to the cameras. """

    __date__ = 'Jun 6, 2013'
    __version__ = '2.0.0'

    @classmethod
    def getAsBytesArray(cls):
        """ Get the packet as a byte array. """
        return bytes(
            [0x4d, 0x4f, 0x5f, 0x49, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x01])


class Answer(object):
    """ Analyze the answer from the cameras. """

    __date__ = 'Jun 6, 2013'
    __version__ = '1.0.0'

    def __init__(self, devID, devName, ip1, ip2, ip3, ip4, nm1, nm2, nm3, nm4,
                 gw1, gw2, gw3, gw4, dns1, dns2, dns3, dns4, fV1, fV2, fV3, fV4,
                 wV1, wV2, wV3, wV4, port):
        """
            Create a new answer with all the required information.

            @param devID Device ID (@MAC).
            @param devName Device Name.
            @param ip1 @IPv4 (first byte).
            @param ip2 @IPv4 (second byte).
            @param ip3 @IPv4 (third byte).
            @param ip4 @IPv4 (fourth byte).
            @param nm1 NetMask (first byte).
            @param nm2 NetMask (second byte).
            @param nm3 NetMask (third byte).
            @param nm4 NetMask (fourth byte).
            @param gw1 Gateway (first byte).
            @param gw2 Gateway (second byte).
            @param gw3 Gateway (third byte).
            @param gw4 Gateway (fourth byte).
            @param dns1 DNS Server (first byte).
            @param dns2 DNS Server (second byte).
            @param dns3 DNS Server (third byte).
            @param dns4 DNS Server (fourth byte).
            @param fV1 Firmware Version (first byte).
            @param fV2 Firmware Version (second byte).
            @param fV3 Firmware Version (third byte).
            @param fV4 Firmware Version (fourth byte).
            @param wV1 WebServer Firmware Version (first byte).
            @param wV2 WebServer Firmware Version (second byte).
            @param wV3 WebServerFirmware Version (third byte).
            @param wV4 WebServerFirmware Version (fourth byte).
            @param port WebServer port number.
        """
        self.deviceID = devID.decode("utf-8")
        self.name = devName.decode("utf-8")
        self.ipAddr = '.'.join(map(str, (ip1, ip2, ip3, ip4)))
        self.mask = '.'.join(map(str, (nm1, nm2, nm3, nm4)))
        self.gateway = '.'.join(map(str, (gw1, gw2, gw3, gw4)))
        self.dns = '.'.join(map(str, (dns1, dns2, dns3, dns4)))
        self.firmwareVersion = '.'.join(map(str, (fV1, fV2, fV3, fV4)))
        self.webVersion = '.'.join(map(str, (wV1, wV2, wV3, wV4)))
        self.port = str(port)

    def __str__(self):
        """ Pretty print an answer from a camera."""
        return "Camera \"" + self.name +\
               "\":\n - General:\n    - DeviceID: " + self.deviceID +\
               "\n    - Firmware version: " + self.firmwareVersion +\
               "\n    - Web version: " + self.webVersion + \
               "\n - Network:\n    - IP Address: " + self.ipAddr +\
               "\n    - Subnet Mask: " + self.mask +\
               "\n    - Gateway: " + self.gateway +\
               "\n    - DNS Server: " + self.dns +\
               "\n    - HTTP Port: " + self.port

    @classmethod
    def frombuffer(cls, buffer):
        """ Extract answer from a buffer. """
        return cls(*struct.Struct(
            '! 23x 12s 1x 20s 1x 4B 4B 4B 4B 4x 4B 4B H x').unpack(buffer))
