import math
import time
#import bitarray


def convert_to_bitarray(list_tuples, window_size):
    length = int(math.log(window_size,2)) + 1
    print("Length = " + str(length))
    big_array = ""
    big_array = big_array + "{0:b}".format(window_size).zfill(length)
    for item in list_tuples:
        mini_array = ""
        mini_array = mini_array + "{0:b}".format(item[0]).zfill(length)
        mini_array = mini_array + "{0:b}".format(item[1]).zfill(length)
        mini_array = mini_array + "{0:b}".format(item[2]).zfill(8)
        big_array = big_array + mini_array
    return big_array

def get_window(data, val, window_size):
    n = val - window_size
    if n < 0:
        #print(val)
        return data[:val]
    return data[n:val]


def find_occurence_in_window(window, last_position, character):
    for j in range(last_position + 1, len(window)):
        if window[j] == curr:
            lookback = len(window) - j
            window_location = j
            return window_location
    return None



def lz77_compressor(file_name, window_size, lookahead_buffer):
    try:
        input_file = open(file_name, 'rb')
        data = input_file.read()
        #print(data)
    except IOError:
        print('Could not open input file ...')

    #print(data)
    print(len(data))
    initial_data_length = len(data) * 8
    print("Initial Data Length: " + str(initial_data_length))
    i = 0

    final_list = []

    while i < len(data):
        last_position = 0

        #best found values for this character
        best_lookahead_found = 0
        best_found_tuple = ()

        #saving the original current values & starting the window
        original_curr = data[i]
        window = get_window(data, i, window_size)

        curr_lookahead = 0

        while original_curr in window:
            curr_lookahead = 0

            #get a window location and reset the window to be from that location onwards
            window_location = find_occurence_in_window(window, original_curr)
            window = get_window(data, i, window_size - window_location)


            while curr_lookahead < lookahead_buffer:

                window_index = window_location + curr_lookahead
                data_index = i + curr_lookahead
                if window_index >= len(window):
                    break
                if data_index >= len(data):
                    curr = 32
                    break
                if window[window_index] == data[data_index]:
                    curr_lookahead += 1

                    continue

            if (i + curr_lookahead) < len(data):
                curr = data[i + curr_lookahead]


            if curr_lookahead > best_lookahead_found:
                best_lookahead_found = curr_lookahead
                new_tuple = (lookback, curr_lookahead, data[i + curr_lookahead])





        """if window_location is not None:
            curr_lookahead += 1
            curr = data[i + curr_lookahead]
            character = chr(curr)

            while curr_lookahead < lookahead_buffer:

                window_index = window_location + curr_lookahead
                data_index = i + curr_lookahead
                if window_index >= len(window):
                    break
                if data_index >= len(data):
                    curr = 32
                    break
                if window[window_index] == data[data_index]:
                    curr_lookahead += 1

                    continue

                found = False
                
        curr = data[i]
        lookback = 0
        curr_lookahead = 0

        window = get_window(data, i, window_size)
        window_location = 0

        for j in range(len(window)):
            if window[j] == curr:
                lookback = len(window) - j
                window_location = j
                found = True
                break

        if found:
            curr_lookahead += 1
            curr = data[i + curr_lookahead]
            character = chr(curr)

            while found and curr_lookahead < lookahead_buffer:

                window_index = window_location + curr_lookahead
                data_index = i + curr_lookahead
                if window_index >= len(window):
                    break
                if data_index >= len(data):
                    curr = 32
                    break
                if window[window_index] == data[data_index]:
                    curr_lookahead += 1

                    continue

                found = False
        if (i+curr_lookahead) < len(data):
            curr = data[i + curr_lookahead]
        new_tuple = (lookback, curr_lookahead, curr)
        final_list.append(new_tuple)
        #print(new_tuple)
        i += (1 + curr_lookahead)
    #print(final_list)
    return final_list"""


to_transform = []
start = time.time()
to_transform = lz77_compressor("easy_lecture_example.txt", 15, 14)
print(str(len(to_transform)))
final_bit_string = convert_to_bitarray(to_transform, 15)




print("Length of compressed string: " + str(len(final_bit_string)))


finish = time.time()
print("Time taken = " + str(finish - start))
