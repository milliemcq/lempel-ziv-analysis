from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
from lempel_ziv_image_decompressor import lz77_image_decompressor
from lempel_ziv_image_compression import lz77_image_compressor
import time
import sys



print(lz77_decompressor(lz77_compressor("txt_files/poem.txt", 500, 500)))

print(lz77_image_decompressor(lz77_image_compressor("image_files/dogsmall.jpg", 500, 500)))


