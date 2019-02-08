from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
import time
import sys

files_to_use = ['txt_files/', 'txt_files/1984.txt', 'txt_files/.txt']

sys.stdout = open(".txt", "w")
print("test sys.stdout")

for item in files_to_use:
    print(item)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++Window Timers+++++++++++++++++++++++++++++++++++++++++++++++++++++")

    i = 255
 
    for j in range(1, 6000, 100):

        print("-----------------------------NEW-------------------------")
        print("Window: " + str(j))
        print("Lookahead: " + str(i))
        start = 0
        bitstr = ""
        bitstr = lz77_compressor(item, j, i)
        start = time.time()
        lz77_decompressor(bitstr)
        finish = time.time()
        print("Deompression Time = " + str(finish - start))




    m = 5000
    print("++++++++++++++++++++++++++++++++++++++++++++++++++Lookahead Timers+++++++++++++++++++++++++++++++++++++++++++++++++++++")

    for k in range(1, 255, 10):

        print("-----------------------------NEW -------------------------")
        print("Window: " + str(m))
        print("Lookahead: " + str(k))
        start = 0
        bitstr = ""
        bitstr = lz77_compressor(item, m, k)
        start = time.time()
        lz77_decompressor(bitstr)
        finish = time.time()
        print("Time taken = " + str(finish - start))