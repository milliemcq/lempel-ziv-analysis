from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
import time

for i in range(1, 20000, 100):
    for j in range(1, 20000, 100):
        print("-----------------------------NEW-------------------------")
        print("Window: " + str(i))
        print("Lookahead: " + str(j))
        start = 0
        start = time.time()
        lz77_compressor("1984.txt", i, j)
        finish = time.time()
        print("Time taken = " + str(finish - start))