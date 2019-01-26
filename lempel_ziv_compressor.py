import math
import time
import bitarray


def convert_to_bitarray(list_tuples, window_size):
    length = int(math.log(window_size,2))
    print("Should say 4: " + str(length))
    big_array = ""
    big_array = big_array + "{0:b}".format(16).zfill(8)
    for item in list_tuples:
        mini_array = ""
        mini_array = mini_array + "{0:b}".format(item[0]).zfill(length)
        mini_array = mini_array + "{0:b}".format(item[1]).zfill(length)
        mini_array = mini_array + "{0:b}".format(item[2]).zfill(7)
        print(mini_array)
        big_array = big_array + mini_array
    return big_array


def final_bit_length(list_tuples, window_size):
    pass

def get_window(data, val, window_size):
    n = val - window_size
    if n < 0:
        #print(val)
        return data[:val]
    return data[n:val]




def lz77_compressor(file_name, window_size):
    try:
        input_file = open(file_name, 'rb')
        data = input_file.read()
    except IOError:
        print('Could not open input file ...')

    print(data)

    i = 0

    final_list = []

    while i < len(data):
        orginal_i = i
        found = False
        curr = data[i]
        count = 0
        lookback = 0

        window = get_window(data, i, window_size)
        window_location = 0

        for j in range(len(window)):
            if window[j] == curr:
                lookback = len(window) - j
                window_location = j
                found = True
                break

        if found:
            count += 1
            curr = data[i+1]
            i += 1
            while found:
                window_index = window_location + count
                data_index = orginal_i + count
                if window_index >= len(window):

                    break
                if data_index >= len(data):

                    curr = 32
                    break
                if window[window_index] == data[data_index]:
                    count += 1
                    i += 1
                    continue

                found = False



        new_tuple = (lookback, count, curr)
        final_list.append(new_tuple)
        print(new_tuple)
        i += 1
    print(final_list)
    return final_list


to_transform = []
start = time.time()
to_transform = lz77_compressor("easy_lecture_example.txt", 16)
final_bit_string = convert_to_bitarray(to_transform, 16)
print(final_bit_string)


finish = time.time()
print("Time taken = " + str(finish - start))