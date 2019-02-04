from lempel_ziv_compressor import lz77_compressor
from lempel_ziv_decompressor import lz77_decompressor
import time
import sys


files = ['txt_files/introductionCDEnglish.txt', 'txt_files/introductionCDFrench.txt', 'txt_files/variabilityCDEnglish.txt', 'txt_files/variabilityCDFrench.txt', 'txt_files/natureCDEnglish.txt', 'txt_files/natureCDFrench.txt']

sys.stdout = open("outputs/FrenchEnglishOutputTxt.txt", "w")
print("test sys.stdout")

for item in files:
    print("####################################### NEW FILE ###################################")
    i = 100

    for j in range(1, 5000, 100):

        print("-----------------------------NEW-------------------------")
        print("Window: " + str(j))
        print("Lookahead: " + str(i))
        start = 0
        start = time.time()
        lz77_compressor(item, j, i)
        finish = time.time()
        print("Time taken = " + str(finish - start))


