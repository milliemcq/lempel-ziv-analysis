from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
from lempel_ziv_image_decompressor import lz77_image_decompressor
import time
import sys

'''

files = ['txt_files/poem.txt', 'txt_files/1984.txt']

for item in files:

    print(lz77_decompressor(lz77_compressor(item, 500, 255)))




bitstring = lz77_compressor("image_files/dogsmall.jpg", 500, 255)

print(lz77_decompressor(bitstring))


print(lz77_decompressor(lz77_compressor('txt_files/poem.txt', 500, 255)))'''


sys.stdout = open("outputs/AUDIO-FINAL2.txt", "w")
print("test sys.stdout")

print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{WINDOW EXPERIMENTS}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]")

print("####################################### NEW FILE ###################################")
i = 30

for j in range(1, 6501, 100):

    print("-----------------------------NEW-------------------------")
    print("Window: " + str(j))
    print("Lookahead: " + str(i))
    start = 0
    start = time.time()
    compressed_string = lz77_compressor("audio/1156.mp3", j, i)
    finish = time.time()
    print("COMPRESSION Time taken = " + str(finish - start))
    start_dec = time.time()
    decompressed_string = lz77_decompressor(compressed_string)
    finish_dec = time.time()
    print("DECOMPRESSION Time taken = " + str(finish_dec - start_dec))




