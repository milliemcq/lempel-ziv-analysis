import math
import time
from bitarray import bitarray

def lz77_decompressor(string_to_decompress):
    """try:
        input_file = open(file_name, 'rb')
        data = input_file.read()
    except IOError:
        print('Could not open input file ...')"""
    print(string_to_decompress)
    window = string_to_decompress[:8]
    window_size = int(window, 2)

    print(string_to_decompress)
    print(window)
    return "not finished"








string_to_decompress = "00010000000000001000001000000001000010000000001010010001100011000011010100011000100011101000100000"

print(lz77_decompressor(string_to_decompress))