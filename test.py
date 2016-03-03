#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from protocol import Answer

__author__ = 'Anthony GELIBERT <anthony.gelibert@me.com>'
__date__ = 'June 6, 2013'
__version__ = '1.0.1'


class TestAnswerInitialPacket(unittest.TestCase):
    """ Test the Answer class using an usual initial packet sent by cameras."""

    def setUp(self):
        """ Decode the packet."""
        self.ans = Answer.frombuffer(bytes(
            [0x4d, 0x4f, 0x5f, 0x49, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x41, 0x00, 0x00, 0x00, 0x41, 0x00, 0x00,
             0x00, 0x45, 0x38, 0x41, 0x42, 0x46, 0x41, 0x31, 0x30, 0x31, 0x33,
             0x33, 0x41, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x11, 0x25, 0x02, 0x29, 0x14, 0x08, 0x04, 0x48, 0x00, 0x50, 0x01]))

    def testDeviceID(self):
        """ Check "Device ID" field."""
        self.assertEqual(self.ans.deviceID, "E8ABFA10133A")

    def testFirmwareVerion(self):
        """ Check "Firmware version" field."""
        self.assertEqual(self.ans.firmwareVersion, "17.37.2.41")

    def testWebVerion(self):
        """ Check "Web version" field."""
        self.assertEqual(self.ans.webVersion, "20.8.4.72")

    def testIP(self):
        """ Check "IP address" field."""
        self.assertEqual(self.ans.ipAddr, "0.0.0.0")

    def testMask(self):
        """ Check "Subnet mask" field."""
        self.assertEqual(self.ans.mask, "0.0.0.0")

    def testGateway(self):
        """ Check "Gateway" field."""
        self.assertEqual(self.ans.gateway, "0.0.0.0")

    def testDNS(self):
        """ Check "DNS" field."""
        self.assertEqual(self.ans.dns, "0.0.0.0")

    def testHTTPPort(self):
        """ Check "HTTP Port" field."""
        self.assertEqual(self.ans.port, "80")


class TestAnswerConfiguredPacket1(unittest.TestCase):
    """ Test the Answer class using a configured camera."""

    def setUp(self):
        """ Decode the packet."""
        self.ans = Answer.frombuffer(bytes(
            [0x4d, 0x4f, 0x5f, 0x49, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x41, 0x00, 0x00, 0x00, 0x41, 0x00, 0x00,
             0x00, 0x45, 0x38, 0x41, 0x42, 0x46, 0x41, 0x31, 0x30, 0x31, 0x33,
             0x33, 0x41, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0xc0, 0xa8, 0x01, 0xfe, 0xff, 0xff, 0xff, 0x00, 0xc0,
             0xa8, 0x01, 0x01, 0xc0, 0xa8, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00,
             0x11, 0x25, 0x02, 0x29, 0x14, 0x08, 0x04, 0x48, 0x00, 0x50, 0x00]))

    def testDeviceID(self):
        """ Check "Device ID" field."""
        self.assertEqual(self.ans.deviceID, "E8ABFA10133A")

    def testFirmwareVerion(self):
        """ Check "Firmware version" field."""
        self.assertEqual(self.ans.firmwareVersion, "17.37.2.41")

    def testWebVerion(self):
        """ Check "Web version" field."""
        self.assertEqual(self.ans.webVersion, "20.8.4.72")

    def testIP(self):
        """ Check "IP address" field."""
        self.assertEqual(self.ans.ipAddr, "192.168.1.254")

    def testMask(self):
        """ Check "Subnet mask" field."""
        self.assertEqual(self.ans.mask, "255.255.255.0")

    def testGateway(self):
        """ Check "Gateway" field."""
        self.assertEqual(self.ans.gateway, "192.168.1.1")

    def testDNS(self):
        """ Check "DNS" field."""
        self.assertEqual(self.ans.dns, "192.168.1.1")

    def testHTTPPort(self):
        """ Check "HTTP Port" field."""
        self.assertEqual(self.ans.port, "80")
