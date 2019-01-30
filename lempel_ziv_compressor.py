import math
import time
#import bitarray


def convert_to_bitarray(list_tuples, window_size):
    length = int(math.log(window_size,2)) + 1
    #print("Length = " + str(length))
    big_array = ""
    big_array = big_array + "{0:b}".format(window_size).zfill(16)
    for item in list_tuples:
        mini_array = ""
        mini_array = mini_array + "{0:b}".format(item[0]).zfill(length)
        mini_array = mini_array + "{0:b}".format(item[1]).zfill(length)
        mini_array = mini_array + "{0:b}".format(item[2]).zfill(8)
        big_array = big_array + mini_array
    return big_array

def get_init_window(data, val, window_size):
    n = val - window_size
    if n < 0:
        #print(val)
        return data[:val]
    return data[n:val]

def get_new_window(old_window, diff):
    return old_window[diff:]



def find_occurence_in_window(window, character):
    for j in range(len(window)):
        if window[j] == character:
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
    #print(len(data))
    initial_data_length = len(data) * 8
    print("Initial Data Length: " + str(initial_data_length))
    i = 0

    final_list = []

    while i < len(data):

        # saving the original current values & starting the window
        original_curr = data[i]
        curr = data[i]

        window = get_init_window(data, i, window_size)
        curr_lookahead = 0

        #best found values for this character
        best_lookahead_found = 0
        best_found_tuple = (0, 0, original_curr)

        new_window_size = window_size

        while original_curr in window:
            curr_lookahead = 0
            lookback = 0


            #get a window location and reset the window to be from that location onwards
            window_location = find_occurence_in_window(window, original_curr)
            #print(window_location)
            lookback = len(window) - window_location



            while curr_lookahead < lookahead_buffer:
                #print(curr_lookahead)
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
                break



            if curr_lookahead > best_lookahead_found:
                if (i + curr_lookahead) < len(data):
                    curr = data[i + curr_lookahead]
                best_lookahead_found = curr_lookahead
                best_found_tuple = (lookback, curr_lookahead, curr)
            window = get_new_window(window, (window_location + 1))

        final_list.append(best_found_tuple)
        i+= (1 + best_lookahead_found)

    final_bit_string = convert_to_bitarray(final_list, window_size)
    #print(final_bit_string)
    print("Final Data Length: " + str(len(final_bit_string)))
    print("Compression Ratio = " + str(initial_data_length/len(final_bit_string)))
    return final_bit_string






to_transform = []
start = time.time()
final = lz77_compressor("1984.txt", 20000, 1000)
print("Compressed length: " + str(len(final)))



finish = time.time()
print("Time taken = " + str(finish - start))
