# Count to 20 by ones
import time
import sys
import inflect
from word2number import w2n

def writeNum(m, n):
    print("Write number from {} to {}".format(m, n))
    for i in range(m, n+1):
        print ('Write {} in number:'.format(inflect.engine().number_to_words(i)))
        ans = int(sys.stdin.readline()[:-1])
        if ans == i:
            print ('Correct')
        else:
            print ('Wrong')

