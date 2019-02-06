#from lempel_ziv_compressor import lz77_compressor
#from lempel_ziv_decompressor import lz77_decompressor
from lempel_ziv_image_decompressor import lz77_image_decompressor
from lempel_ziv_image_compression import lz77_image_compressor
import time
import sys



#lz77_decompressor(lz77_compressor("txt_files/1984 copy.txt", 500, 255))

#lz77_image_decompressor(lz77_image_compressor("image_files/dogsmall.jpg", 500, 255))

#print(lz77_image_decompressor(lz77_image_compressor("audio/1156.mp3", 500, 255)))

our_file = open("audio/1156.mp3", "rb")
f = our_file.read()
b = bytearray(f)

for i in range(len(f)):
    print(f[i])

print(f)

