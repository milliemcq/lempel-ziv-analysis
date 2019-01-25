import math
import time
#from bitarray import bitarray


def convert_to_bitarray(list_tuples, window_size):
    length = math.log(window_size)
    array = []
    for item in list_tuples:
        array.append(bin(item[0]))
        array.append(bin(item[1]))
        array.append(bin(item[2]))




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

                    curr = ''
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


start = time.time()
lz77_compressor("easy_lecture_example.txt", 12)
finish = time.time()
print("Time taken = " + str(finish - start))