import math
import time
from bitarray import bitarray

def get_string(current_string, back_space, length, final_char):
    return_string = ""
    start = len(current_string) - back_space
    end = len(current_string) - back_space + length
    return_string += current_string[start:end]

    return_string += str(chr(final_char))
    #print(return_string)
    return return_string



def decompress_from_tuples(list_of_tuples, window_size):
    final_string = ""
    for item in list_of_tuples:
        #print("final string: " + str(final_string))
        #print(item)
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

    window = string_to_decompress[:16]
    window_size = int(window, 2)
    string_to_decompress = string_to_decompress[16:]
    window_bit_length = int(math.log(window_size, 2)) + 1

    location = 0

    list_of_tuples = []

    while location + window_bit_length < len(string_to_decompress):

        first = int(string_to_decompress[location:location + window_bit_length], 2)
        location += window_bit_length
        """
        print("STD: " + str(string_to_decompress[location:location + window_bit_length]))
        print("len str: " + str(len(string_to_decompress)))
        print("location: " + str(location))
        """
        second = int(string_to_decompress[location:location + window_bit_length], 2)
        #print(string_to_decompress[location:location + window_bit_length])
        location += window_bit_length
        third = int(string_to_decompress[location:location + 8], 2)
        location += 8

        tuple = (first, second, third)
        list_of_tuples.append(tuple)

    #print(list_of_tuples)
    final = decompress_from_tuples(list_of_tuples, window_size)
    print(final)
    return final


string_to_decompress = "0000000010010110000000000000000001010000000000000000000001100101000000000000000001110100000000100000000101110010000000000000000000100000000001100000000101101001000000000000000001110000000010000000000101110010000001100000000101110000000001100000000101100011000000000000000001101011000011110000000101100100000011010000000101100001000011110000000101110000000101010000000101100011000010010000000100100000000000000000000001101111000000000000000001100110000101110000000101110000000101110000000101100011000100010000000101101100001000010000000101100100000111110000001001100101000111110000000101110000001010000000000101110010000000000000000001110011000000000000000000111011000000000000000001000001001010010000000101110000001011110000000101100011001000110000000100100000000110100001001000100000010001110001001000111011000000000000000001001001010000000000001001010000010111010010101100101100000000000000000001010111000000000000000001101000100010110000001001100101000000000000000000100111000000000000000001110011011111110000000101110100000000000000000001101000100100110000000100100000011110010000001001100011000000000000000001101011100010000001001100100000000000000000000001010000011100110001000100001010"














#print(lz77_decompressor(string_to_decompress))

