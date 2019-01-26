import math
import time
from bitarray import bitarray

def lz77_decompressor(string_to_decompress):
    """try:
        input_file = open(file_name, 'rb')
        data = input_file.read()
    except IOError:
        print('Could not open input file ...')"""

    window = string_to_decompress[:8]
    window_size = int(window, 2)
    string_to_decompress = string_to_decompress[8:]
    window_bit_length = math.log(window_size, 2)

    location = 0

    while location < len(string_to_decompress):

        first = int(string_to_decompress[location:location+4], 2)
        location += 4
        second = int(string_to_decompress[location:location + 4], 2)
        location += 4
        third = int(string_to_decompress[location:location + 8], 2)
        location += 8

        first_tuple = (first, second, third)
        print(first_tuple)




    return "not finished"








string_to_decompress = "00010000000000000100000100000000010000100000000001010010001100010100001101010001010001000111010000100000"

print(lz77_decompressor(string_to_decompress))