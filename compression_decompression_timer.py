from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
import time
import sys

files_to_use = ['txt_files/poem.txt', 'txt_files/1984.txt', 'txt_files/alicewonder.txt']

sys.stdout = open("compressionDecompressionTimers", "w")
print("test sys.stdout")

for item in files_to_use:
    print(item)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++Window Timers+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    i = 5000

    for j in range(1, 100, 6000):

        print("-----------------------------NEW-------------------------")
        print("Window: " + str(i))
        print("Lookahead: " + str(j))
        start = 0
        bitstr = ""
        bitstr = lz77_compressor(item, j, i)
        start = time.time()
        lz77_decompressor(bitstr)
        finish = time.time()
        print("Deompression Time = " + str(finish - start))




    m = 5000
    print("++++++++++++++++++++++++++++++++++++++++++++++++++Lookahead Timers+++++++++++++++++++++++++++++++++++++++++++++++++++++")

    for j in range(1, 300, 10):

        print("-----------------------------NEW -------------------------")
        print("Window: " + str(m))
        print("Lookahead: " + str(j))
        start = 0
        bitstr = ""
        bitstr = lz77_compressor(item, m, j)
        start = time.time()
        lz77_decompressor(bitstr)
        finish = time.time()
        print("Time taken = " + str(finish - start))