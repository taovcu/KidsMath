# Count to 20 by ones
import time

def countNum(m):
    print "Count with me from 1 to %d" % (m)
    for i in range(1, m+1):
        print i
        # wait for 1 second
        time.sleep(1)

