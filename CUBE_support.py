#!/usr/bin/env python3

#from BitVector import BitVector
from binascii import crc32
import struct


def output_number(input_object):
    return (input_object[0] << 16) | input_object[1]


def output_string(input_number):
    return "{0:024b}".format(input_number)


def output_bytes(input_object):
    in_data_layer = struct.pack('>B', input_object[0])
    in_data_packed = struct.pack('>H', input_object[1])
#    in_data_combined = struct.pack('>L', input_number)
    in_data_combined = struct.pack('>L', output_number(input_object))
    in_data_checked = struct.pack('>L', crc32(in_data_combined))
#    return in_data_combined + in_data_checked
    return in_data_layer + in_data_packed + in_data_checked


def check_output_bytes(input_bytes, test_layer, test_pattern, test_crc):
    in_data_unpacked = struct.unpack('>BHL', input_bytes)
    return (in_data_unpacked[0] == test_layer, in_data_unpacked[1] == test_pattern, in_data_unpacked[2] == test_crc)


if __name__ == '__main__':

    test_layer = 2
    test_pattern = 0x4321 

    test_object = (test_layer, test_pattern)
    test_number = output_number(test_object)

    print("{0:016b}".format(test_pattern))
    print(test_object)
    print(test_number)
    print(output_string(test_number))
    test_crc = crc32(struct.pack('>L', test_number))
    print("{0:032b}".format(test_crc))
    test_output_bytes = output_bytes(test_object)
    print(test_output_bytes)
    print(check_output_bytes(test_output_bytes, test_layer, test_pattern, test_crc))
