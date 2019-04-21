# Count to 20 by ones
import time
import sys
import emoji

def countNumfromX(x, y):
    print "Count from %d to %d, leave a blank between numbers" % (x, y)
    ans = sys.stdin.readline()
    ans = ans.split()
    ans = map(int, ans)
    if ans == range(x, y+1):
        print emoji.emojize(':thumbs_up: ')*3, "You got it."
    else:
        print emoji.emojize(':thumbs_down: ')*3, "The correct sequence is ", range(x, y+1)

