#!/usr/bin/python3
"""UTF8 Validator module"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Count of remaining bytes for the current UTF-8 character
    remaining_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if remaining_bytes > 0:
            # Check if the byte starts with '10' as required for a continuation byte
            if (byte >> 6) == 0b10:
                remaining_bytes -= 1
            else:
                return False
        else:
            # Check the number of bytes for the current UTF-8 character
            if byte >> 7 == 0:
                # Single-byte character (0xxxxxxx)
                remaining_bytes = 0
            elif byte >> 5 == 0b110:
                # Two-byte character (110xxxxx 10xxxxxx)
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte character (1110xxxx 10xxxxxx 10xxxxxx)
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
                remaining_bytes = 3
            else:
                # Invalid leading byte
                return False

    # Check if there are remaining bytes after processing all bytes
    return remaining_bytes == 0
