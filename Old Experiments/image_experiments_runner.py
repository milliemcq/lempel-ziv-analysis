from lempel_ziv_image_decompressor import lz77_image_decompressor
from lempel_ziv_image_compression import lz77_image_compressor
import time
import sys

files = ['image_files/dogsmall.jpg', 'image_files/dogmedium.jpg']

sys.stdout = open("outputs/IMAGE-DECOMPRESSION-TIME.txt", "w")

"""
print("test sys.stdout")

print("-------------------------------------------------------TESTING WINDOW SIZE---------------------------------------------------------------------")

for item in files:
    print("####################################### NEW FILE ###################################")
    print(item)
    i = 255

    for j in range(1, 10000, 100):

        print("-----------------------------NEW-------------------------")
        print("Window: " + str(j))
        print("Lookahead: " + str(i))
        start = 0
        start = time.time()
        lz77_image_compressor(item, j, i)
        finish = time.time()
        print("Time taken = " + str(finish - start))




print("-------------------------------------------------------TESTING LOOKAHEAD SIZE---------------------------------------------------------------------")

for item in files:

    print("####################################### NEW FILE ###################################")
    print(item)
    i = 5000

    for k in range(1, 500, 10):

        print("-----------------------------NEW-------------------------")
        print("Window: " + str(i))
        print("Lookahead: " + str(k))
        start = 0
        start = time.time()
        lz77_image_compressor(item, i, k)
        finish = time.time()
        print("Time taken = " + str(finish - start))


"""

# DECOMPRESSION EXPERIMENTS

print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{Lookahead EXPERIMENTS}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]")
for item in files:
    print("####################################### NEW FILE ###################################")
    print(item)
    i = 5000

    for k in range(1, 300, 10):
        print("-----------------------------NEW-------------------------")
        print("Window: " + str(i))
        print("Lookahead: " + str(k))
        start = 0

        compressed_string = lz77_image_compressor(item, i, k)
        start = time.time()
        decompressed_string = lz77_image_decompressor(compressed_string)
        finish = time.time()
        print("Decompression time taken = " + str(finish - start))


print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{WINDOW EXPERIMENTS}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]")
for item in files:
    print("####################################### NEW FILE ###################################")
    print(item)
    i = 300

    for j in range(1, 7000, 100):
        print("-----------------------------NEW-------------------------")
        print("Window: " + str(j))
        print("Lookahead: " + str(i))
        start = 0

        compressed_string = lz77_image_compressor(item, j, i)
        start = time.time()
        decompressed_string = lz77_image_decompressor(compressed_string)
        finish = time.time()
        print("Decompression time taken = " + str(finish - start))

