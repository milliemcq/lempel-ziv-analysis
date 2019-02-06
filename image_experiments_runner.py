from lempel_ziv_image_decompressor import lz77_image_decompressor
from lempel_ziv_image_compression import lz77_image_compressor
import time
import sys

files = ['image_files/dogsmall.jpg', 'image_files/dogmedium.jpg']

sys.stdout = open("outputs/imagesoutput2.txt", "w")
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



