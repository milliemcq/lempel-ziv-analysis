from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
import time
import sys


files = ['txt_files/poem.txt', 'txt_files/1984.txt', 'txt_files/alicewonder.txt']


sys.stdout = open("outputs/LOOKAHEAD-CR-MORE-ACCURATE.txt", "w")
print("test sys.stdout")


print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{WINDOW EXPERIMENTS}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]")
for item in files:
    print("####################################### NEW FILE ###################################")
    i = 255

    for j in range(1, 7000, 100):

        print("-----------------------------NEW-------------------------")
        print("Window: " + str(j))
        print("Lookahead: " + str(i))
        start = 0
        start = time.time()
        compressed_string = lz77_compressor(item, j, i)
        finish = time.time()
        print("COMPRESSION Time taken = " + str(finish - start))
        start_dec = time.time()
        decompressed_string = lz77_decompressor(compressed_string)
        finish_dec = time.time()
        print("DECOMPRESSION Time taken = " + str(finish_dec - start_dec))


print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{Lookahead EXPERIMENTS}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]")
for item in files:
    print(item)
    print("####################################### NEW FILE ###################################")
    i = 5000

    for j in range(1, 30, 1):

        print("-----------------------------NEW-------------------------")
        print("Window: " + str(i))
        print("Lookahead: " + str(j))
        start = 0
        start = time.time()
        compressed_string = lz77_compressor(item, i, j)
        finish = time.time()
        print("COMPRESSION Time taken = " + str(finish - start))
        start_dec = time.time()
        decompressed_string = lz77_decompressor(compressed_string)
        finish_dec = time.time()
        print("DECOMPRESSION Time taken = " + str(finish_dec - start_dec))