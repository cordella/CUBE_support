#from BitVector import BitVector
from binascii import crc32
import struct

#def output_object(layer, input_pattern):
#    return (layer, input_pattern)

def output_number(input_object):
    return (input_object[0] << 16) | input_object[1]

def output_string(input_number):
    return "{0:032b}".format(input_number)

def output_bytes(input_object):
    in_data_layer = struct.pack('>B', input_object[0])
    in_data_packed = struct.pack('>H', input_object[1])
#    in_data_combined = struct.pack('>L', input_number)
    in_data_combined = struct.pack('>L', output_number(input_object))
    in_data_checked = struct.pack('>L', crc32(in_data_combined))
#    return in_data_combined + in_data_checked
    return in_data_layer + in_data_packed + in_data_checked


if __name__ == '__main__':

    test_layer = 2
    test_pattern = 0x4321

    test_object = (test_layer, test_pattern)
    test_number = output_number(test_object)

    print("{0:016b}".format(test_pattern))
    print(test_object)
    print(test_number)
    print(output_string(test_number))
    print("{0:032b}".format(crc32(struct.pack('>L', test_number))))
    print(output_bytes(test_object))
