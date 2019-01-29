from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor


lz77_decompressor(lz77_compressor("1984.txt", 150, 150))
