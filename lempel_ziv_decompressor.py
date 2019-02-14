import math
import time

"""

def get_string(current_string, back_space, length, final_char):
    return_string = ""
    start = len(current_string) - back_space
    end = len(current_string) - back_space + length
    return_string += current_string[start:end]

    return_string += str(chr(final_char))
    #print(return_string)
    return return_string



def decompress_from_tuples(list_of_tuples):
    final_string = ""
    for item in list_of_tuples:
        if item[0] == 0:
            final_string += str(chr(item[2]))
        else:
            final_string += get_string(final_string, item[0], item[1], item[2])
    return final_string

"""

def get_list(current_string, back_space, length, final_char):
    return_list = []
    start = len(current_string) - back_space
    end = len(current_string) - back_space + length
    return_list += current_string[start:end]

    return_list.append(final_char)
    #print(return_string)
    return return_list



def decompress_from_tuples(list_of_tuples):
    final_list = []
    for item in list_of_tuples:
        if item[0] == 0:
            final_list.append(item[2])
        else:
            final_list.extend(get_list(final_list, item[0], item[1], item[2]))
    return final_list



def lz77_decompressor(string_to_decompress):

    window = string_to_decompress[:16]
    window_size = int(window, 2)
    string_to_lookahead = string_to_decompress[16:]
    lookahead = string_to_lookahead[:8]
    lookahead_size = int(lookahead, 2)
    # print(lookahead_size)

    string_to_decompress = string_to_lookahead[8:]

    window_bit_length = int(math.log(window_size, 2)) + 1
    lookahead_bit_length = int(math.log(lookahead_size, 2)) + 1

    # print("window length" + str(window_bit_length))
    # print("lookahead length" + str(lookahead_bit_length))

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
        second = int(string_to_decompress[location:location + lookahead_bit_length], 2)
        # print(string_to_decompress[location:location + window_bit_length])
        location += lookahead_bit_length
        third = int(string_to_decompress[location:location + 8], 2)
        location += 8

        tuple = (first, second, third)
        list_of_tuples.append(tuple)

    final = decompress_from_tuples(list_of_tuples)

    bytes = bytearray(final)
    #bytes.decode()
    #print(bytes)

    # print(final)
    return bytes















#print(lz77_decompressor(string_to_decompress))

