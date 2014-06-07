#!/usr/bin/env python
""" generated source for module BaseHashing """
# package: org.ggp.base.util.crypto
import java.io.BufferedInputStream

import java.io.ByteArrayInputStream

import java.security.DigestInputStream

import java.security.MessageDigest

import java.util.Formatter

class BaseHashing(object):
    """ generated source for class BaseHashing """
    #  Computes the SHA1 hash of a given input string, and represents
    #  that hash as a hexadecimal string.
    @classmethod
    def computeSHA1Hash(cls, theData):
        """ generated source for method computeSHA1Hash """
        try:
            while theDigestStream.read() != -1:
                pass
            for x in theHash:
                hexFormat.format("%02x", x)
            return hexFormat.__str__()
        except Exception as e:
            e.printStackTrace()
            return None

