# pip install inflect
# pip install word2number

import sys
import inflect
from word2number import w2n


def Number2Name(a):
    print ('Spell {} in Characters:'.format(a))
    line = sys.stdin.readline()[:-1]
    p = inflect.engine()
    if line == p.number_to_words(a):
        print ('Correct')
    else:
        print ('Wrong')

def Name2Number(a):
    print ('Spell {} in number:'.format(a))
    ans = int(sys.stdin.readline()[:-1])
    if ans == w2n.word_to_num(a):
        print ('Correct')
    else:
        print ('Wrong')

