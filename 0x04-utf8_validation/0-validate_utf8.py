#!/usr/bin/python3
"""
Task 0:  UTF-8 Validation
"""


def validUTF8(data):
    """
    determines if a given data set
    represents a valid UTF-8 encoding
    """
    index = 0
    while index < len(data):
        byte = data[index]

        if byte < 0 or byte > 255:
            return False
        if (byte & 0b10000000) == 0b00000000:
            num_bytes = 1
        elif (byte & 0b11100000) == 0b11000000:
            num_bytes = 2
        elif (byte & 0b11110000) == 0b11100000:
            num_bytes = 3
        elif (byte & 0b11111000) == 0b11110000:
            num_bytes = 4
        else:
            return False
        for i in range(1, num_bytes):
            if index + i >= len(data):
                return False
            continuationByte = data[index + i]
            # Check if continuationByte is within valid 8-bit range
            if continuationByte < 0 or continuationByte > 255:
                return False
            if (continuationByte & 0b11000000) != 0b10000000:
                return False
        index += num_bytes
    return True
