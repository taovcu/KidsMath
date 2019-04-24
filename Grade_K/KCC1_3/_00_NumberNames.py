# pip install inflect
# pip install word2number

import sys
sys.path.append('../../')

import inflect
from word2number import w2n
import Helpers.IO as io
import Helpers.CheckAns as CA

def Number2Name(a):
    io.printTTS('Spell {} in Characters:'.format(a))
    line = io.readLine()
    p = inflect.engine()
    CA.checkEqual(line, p.number_to_words(a))

def Name2Number(a):
    print ('Write {} in number:'.format(a))
    ans = io.readInt()
    CA.checkEqual(ans, w2n.word_to_num(a))
