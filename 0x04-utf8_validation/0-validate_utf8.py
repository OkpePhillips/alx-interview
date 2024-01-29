#!/usr/bin/python3
"""
Module to find out the UTF-8 status of a set of data
"""


def validUTF8(data):
    """
    Function to determine the utf-8 status of input data
    """
    def is_valid_following_byte(byte):
        """
        Function to check whether the leading bits match
        expected pattern.
        """
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        leading_ones = bin(data[i])[2:].rjust(8, '0').index('0')
        if leading_ones == 0:
            i += 1
        elif 1 <= leading_ones <= 4:
            for j in range(1, leading_ones):
                if i + j >= len(data) or not \
                        is_valid_following_byte(data[i + j]):
                    return False
            i += leading_ones
        else:
            return False

    return True
