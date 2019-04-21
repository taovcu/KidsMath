# Count to 20 by ones
import time
import random
import sys
import emoji

def countNumby10s(m, t):
    print("Count with me from 10 to {} by 10s".format(m))
    
    # if t == 1, randomly skip a number 
    if t:
        random.seed(t)
        t = random.randint(1, m/10) * 10
        
    for i in range(10, m+1, 10):
        if i == t:
            continue
        print(i)
        # wait for 1 second
        time.sleep(1)

    print 'Is there any number missing in this sequence?'
    ans = sys.stdin.readline()[0]
    while ans not in ['n', 'N', 'y', 'Y']:
        print "You can only input 'n' or 'y'"
        ans = sys.stdin.readline()[0]
    if (ans in ['y', 'Y'] and t):
        print emoji.emojize(':thumbs_up: ')*3, "You got it. %d is missing" %(t)
    elif (ans in ['n', 'N'] and not t):
        print emoji.emojize(':thumbs_up: ')*3, "You got it. All numbers are there"
    else:
        if ans in ['y', 'Y']: 
            print emoji.emojize(':thumbs_down: ')*3, "Wrong. You say there is some number missing, but actually all numbers are in the sequence"
        if ans in ['n', 'N']: 
            print emoji.emojize(':thumbs_down: ')*3, "Wrong. You say there is no number missing, but actually %d is NOT in the sequence" %(t)

    raw_input("Press Enter to continue...")
