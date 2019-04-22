import sys

def readChar():
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        return
    while not line:
        readChar()
    return line[0]

def readInt():
    try:
        line = sys.stdin.readline()[:-1]
    except KeyboardInterrupt:
        return
    while not line.isdigit() or line == "":
        print("input is not an int")
        readInt()
    return int(line)

