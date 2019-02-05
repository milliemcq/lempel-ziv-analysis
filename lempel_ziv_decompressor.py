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














#print(lz77_decompressor(string_to_decompress))

