import sys

def readStdin():
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        return
    while not line:
        readStdin()
    return int(line)


