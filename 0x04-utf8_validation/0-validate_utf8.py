#!/usr/bin/python3
"""UTF8 Validator module"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Count of remaining bytes for the current UTF-8 character
    num_bytes = 0
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        byte = num & 0xFF  # Get the last 8 bits

        if num_bytes == 0:
            if (byte & mask1) == 0:  # Single-byte character (0xxxxxxx)
                num_bytes = 0
            elif (byte & mask2) == 0:  # Invalid continuation byte
                return False
            else:  # Multi-byte character
                num_bytes = 1 if (byte & 0xE0) == 0xC0 else\
                    2 if (byte & 0xF0) == 0xE0 else\
                    3 if (byte & 0xF8) == 0xF0 else\
                    0  # Invalid starting byte
        else:
            if (byte & mask1) == 0 or (byte & mask2) != 0:  # Invalid continuation byte
                return False
            num_bytes -= 1

    return num_bytes == 0
