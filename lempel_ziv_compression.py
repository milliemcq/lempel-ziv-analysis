import math
from bitarray import bitarray


def lz77_compressor(file_name):
    try:
        input_file = open(file_name, 'rb')
        data = input_file.read()
    except IOError:
        print('Could not open input file ...')

    print(data)





lz77_compressor("easy_lecture_example.txt")