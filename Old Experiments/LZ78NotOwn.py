# LZ78 implementation
# Université de Fribourg, Suisse
# AUTHOR: Noé Zufferey - noe.zufferey@gmail.com
# CREATION: april 2018
# USAGE: python3 LZ78.py '<string to encode>'

import sys
import time


def compress(data):
    comp_data = []
    dictionnary = ['']
    word = ''
    i = 0
    for char in data:
        i += 1
        word += char
        if not word in dictionnary:
            dictionnary.append(word)
            comp_data.append([dictionnary.index(word[:-1]), word[-1]])
            word = ''
        elif i == len(data):
            comp_data.append([dictionnary.index(word), ''])
            word = ''
    return comp_data


def add_zeros(code, nbr):
    pre = ''
    i = 0
    while i < nbr - len(code):
        pre += '0'
        i += 1
    return pre + code


def to_bits(data, h=False):
    len_ind = 1
    result = ''
    first_round = True
    for word in data:
        if not first_round:
            pre = add_zeros(bin(word[0])[2:], len_ind)
            result += pre
            len_ind = len(pre)
            if h and (word[1] != ''): result += ','
        else:
            first_round = False

        next_char = add_zeros(bin(ord(word[1]))[2:], 8) if not (word[1] == '') else ''
        result += next_char
        if h: result += '|'
    return result


files = ['txt_files/poem.txt', 'txt_files/1984.txt', 'txt_files/alicewonder.txt']
sys.stdout = open("outputs/Lz78-output.txt", "w")
print("test sys.stdout")

for item in files:
    try:
        input_file = open(item, 'r')
        data = input_file.read()
        # print(data)
    except IOError:
        print('Could not open input file ...')
    initial_data_size = len(data) * 8

    start = time.time()
    comp_data = compress(data)
    final_string = to_bits(comp_data)
    finish = time.time()

    final_length = len(final_string)
    cr = initial_data_size/ final_length
    print("Compression Ratio: " + str(cr))
    print("COMPRESSION Time taken = " + str(finish - start))
