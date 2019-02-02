from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
import time
import sys


sys.stdout = open("1984WindowOutputTxt.txt", "w")
print("test sys.stdout")

i = 5000

for j in range(1, 20000, 100):

    print("-----------------------------NEW-------------------------")
    print("Window: " + str(j))
    print("Lookahead: " + str(i))
    start = 0
    start = time.time()
    lz77_compressor("1984.txt", j, i)
    finish = time.time()
    print("Time taken = " + str(finish - start))


