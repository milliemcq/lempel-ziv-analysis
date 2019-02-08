from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
import time
import sys

files = ["txt_files/1984.txt", "txt_files/.txt"]

sys.stdout = open("outputs/.txt", "w")
print("test sys.stdout")

for item in files:
    print(item)
    print("####################################### NEW FILE ###################################")
    i = 5000

    for j in range(1, 200, 10):

        print("-----------------------------NEW-------------------------")
        print("Window: " + str(i))
        print("Lookahead: " + str(j))
        start = 0
        start = time.time()
        lz77_compressor(item, i, j)
        finish = time.time()
        print("Time taken = " + str(finish - start))