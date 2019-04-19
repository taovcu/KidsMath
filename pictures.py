'''Draw a non-interactive picture, with precalculated Point locations,
using a loop.
'''

from graphics import *

def ballon():
    winWidth = 200
    winHeight = 300
    win = GraphWin('Balloons', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight) # right side up coordinates
    win.setBackground('green')

    base = Point(100, 50)

    for center in [Point(50, 200), Point(150, 220), Point(100, 225)]:
        line = Line(base, center)
        line.draw(win)
        balloon = Circle(center, 40)
        balloon.setOutline('red')
        balloon.setFill('pink')
        balloon.draw(win)

    # Wait for a click to exit
    message = Text(Point(winWidth/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()
