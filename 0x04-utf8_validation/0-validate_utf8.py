#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""


def validUTF8(data):
    """
    Validate if a list of integers represents valid UTF-8 encoding.
    Args:
        data (list[int]): A list of integers representing bytes.
    Returns:
        bool: True if data represents valid UTF-8 encoding, else False.
    """
    byte_count = 0

    for byte in data:
        if byte_count == 0:
            # Determine how many bytes are in the current UTF-8 character
            if (byte >> 5) == 0b110:
                byte_count = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                byte_count = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                byte_count = 3  # 4-byte character
            elif (byte >> 7):
                return False  # If a byte starts with 10xxxxxx, it's invalid here
        else:
            # Check if the next byte starts with 10 (0b10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            byte_count -= 1


    return byte_count == 0
