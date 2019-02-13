from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
from lempel_ziv_image_decompressor import lz77_image_decompressor



files = ['txt_files/poem.txt', 'txt_files/1984.txt']

for item in files:

    print(lz77_decompressor(lz77_compressor(item, 500, 255)))




bitstring = lz77_compressor("image_files/dogsmall.jpg", 500, 255)

print(lz77_decompressor(bitstring))

audioBitstring = lz77_compressor("audio/1156.mp3", 500, 255)
lz77_decompressor(audioBitstring)


print(lz77_decompressor(lz77_compressor('txt_files/poem.txt', 500, 255)))

