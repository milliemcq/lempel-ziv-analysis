import math
import time
from bitarray import bitarray

def get_string(current_string, back_space, length, final_char):

    return_string = ""
    start = len(current_string) - back_space
    end = len(current_string) - back_space + length
    return_string += current_string[start:end]
    return_string += str(chr(final_char))
    return return_string



def decompress_from_tuples(list_of_tuples, window_size):
    final_string = ""
    for item in list_of_tuples:
        if item[0] == 0:
            final_string += str(chr(item[2]))
        else:
            final_string += get_string(final_string, item[0], item[1], item[2])
    return final_string



def lz77_decompressor(string_to_decompress):
    """try:
        input_file = open(file_name, 'rb')
        data = input_file.read()
    except IOError:
        print('Could not open input file ...')"""

    window = string_to_decompress[:8]
    window_size = int(window, 2)
    string_to_decompress = string_to_decompress[8:]
    window_bit_length = int(math.log(window_size, 2))

    location = 0

    list_of_tuples = []

    while location + window_bit_length < len(string_to_decompress):

        first = int(string_to_decompress[location:location + window_bit_length], 2)
        location += window_bit_length
        print("STD: " + str(string_to_decompress[location:location + window_bit_length]))
        print("len str: " + str(len(string_to_decompress)))
        print("location: " + str(location))
        second = int(string_to_decompress[location:location + window_bit_length], 2)
        print(string_to_decompress[location:location + window_bit_length])
        location += window_bit_length
        third = int(string_to_decompress[location:location + 8], 2)
        location += 8

        tuple = (first, second, third)
        list_of_tuples.append(tuple)

    print(list_of_tuples)
    final = decompress_from_tuples(list_of_tuples, window_size)

    return final


string_to_decompress = "1001011000000000000000010100000000000000000001100101000000000000000111010000000100000001011100100000000000000000100000000011000000010110100100000000000000011100000001000000000101110010000011000000010111000000001100000001011000110000000000000001101011000111100000010110010000011010000001011000010001111000000101110000001010100000010110001100010010000001001000000000000000000001101111000000000000000110011000101110000001011100000010111000000101100011001000100000010110110001000010000001011001000011111000000101110000010010100000010111000001000000000011011001010000000000000000111011000000000000000100000101010010000001011100000101111000000101100011010001100000010010000000110100010010011001101000111001001001100101000000000000000100100110000000000010001000001011101010101101110100000000000000000101011100000000000000011010001000101100000010111001010001101000000100100111110010100000010010000010010000000000101101000100100110000001001000001000111000000100110010110001010000000100100000100000010010010011001101100111001001000100000"
print(lz77_decompressor(string_to_decompress))