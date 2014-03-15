#from BitVector import BitVector
from binascii import crc32
import struct

test_input = 0x4321

def output_pattern(layer, input_pattern):
    return (layer << 16) | input_pattern

def output_data(input_data):
    in_data_packed = struct.pack('>L', input_data)
    in_data_checked = struct.pack('>L', crc32(in_data_packed))
    return in_data_packed + in_data_checked

print(output_data(output_pattern(2, test_input)))
