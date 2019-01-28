import math
import time
import bitarray


def convert_to_bitarray(list_tuples, window_size):
    length = int(math.log(window_size,2)) + 1
    print('length: ' + str(length))
    big_array = ""
    big_array = big_array + "{0:b}".format(window_size).zfill(8)
    for item in list_tuples:
        mini_array = ""
        print(item)
        mini_array = mini_array + "{0:b}".format(item[0]).zfill(length)
        print(len("{0:b}".format(item[0]).zfill(length)))
        mini_array = mini_array + "{0:b}".format(item[1]).zfill(length)
        print(len("{0:b}".format(item[1]).zfill(length)))
        mini_array = mini_array + "{0:b}".format(item[2]).zfill(8)
        print(len("{0:b}".format(item[2]).zfill(8)))
        print(mini_array)
        big_array = big_array + mini_array
    return big_array

def get_window(data, val, window_size):
    n = val - window_size
    if n < 0:
        #print(val)
        return data[:val]
    return data[n:val]




def lz77_compressor(file_name, window_size, lookahead_buffer):
    try:
        input_file = open(file_name, 'rb')
        data = input_file.read()
        print(data)
    except IOError:
        print('Could not open input file ...')

    print(data)

    i = 0

    final_list = []

    while i < len(data):
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
        print(new_tuple)
        i += (1 + curr_lookahead)
    print(final_list)
    return final_list


to_transform = []
start = time.time()
to_transform = lz77_compressor("1984.txt", 150, 50)
final_bit_string = convert_to_bitarray(to_transform, 150)




print("Final String: " + str(final_bit_string))


finish = time.time()
print("Time taken = " + str(finish - start))