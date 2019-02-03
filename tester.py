from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
import time
import sys


print(lz77_decompressor(lz77_compressor("dogsmall.jpg", 500, 500)))

print(lz77_decompressor(lz77_compressor("longer_lecture_example.txt", 500, 500)))