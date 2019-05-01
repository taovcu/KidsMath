import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import emoji


# squares, circles, triangles, rectangles, hexagons
# cubes, cones, cylinders, and spheres
def plot2D(s):
    plt.axes()

    if s == 'circle':
        #circle = plt.Circle((0, 0), radius=0.75, fc='c')
        shape = plt.Circle((0, 0), fc='c')
    if s == 'rectangle':
        shape = plt.Rectangle((10, 10), 100, 60, fc='c')
    if s == 'square':
        shape = plt.Rectangle((10, 10), 100, 100, fc='c')
    if s == 'triangle':
        points = [[2, 1], [8, 1], [8, 4]]
        shape = plt.Polygon(points)
    if s == 'hexagon':
        points = [[2, 4], [4, 6], [6, 6], [8, 4], [6, 2], [4, 2]]
        shape = plt.Polygon(points)

    plt.gca().add_patch(shape)
    plt.axis('scaled')
    plt.show()


# cubes, cones, cylinders, and spheres
def plot3D(s):
    fig = plt.figure()

    if s == 'cube':
        # prepare some coordinates
        x, y, z = np.indices((1, 1, 1))
        # draw cuboids in the top left and bottom right corners, and a link between them
        cube1 = (x < 1) & (y < 1) & (z < 1)
        # combine the objects into a single boolean array
        # set the colors of each object
        colors = np.empty(cube1.shape, dtype=object)
        colors[cube1] = 'c'
        # and plot everything
        ax = fig.gca(projection='3d')
        ax.voxels(cube1, facecolors=colors, edgecolor='k')

    if s == 'cone':
        ax = fig.add_subplot(111, projection='3d')
        a = np.arange(-1,2,0.25)
        x =  np.outer(np.ones(len(a)),a)
        y =  np.outer(a,np.ones(len(a)))
        def cone(x,y):
            r = np.hypot(x,y)
            return (1-r) * (r <= 1)
        z = cone
        ax.plot_surface(x, y, z(x,y),  rstride=1, cstride=1, color='c')
        elev = 20
        azim = -75
        ax.view_init(elev, azim)

    if s == 'cylinder':
        def data_for_cylinder_along_z(center_x,center_y,radius,height_z):
            z = np.linspace(0, height_z, 50)
            theta = np.linspace(0, 2*np.pi, 50)
            theta_grid, z_grid=np.meshgrid(theta, z)
            x_grid = radius*np.cos(theta_grid) + center_x
            y_grid = radius*np.sin(theta_grid) + center_y
            return x_grid,y_grid,z_grid
        
        ax = fig.add_subplot(111, projection='3d')
        Xc,Yc,Zc = data_for_cylinder_along_z(0.2,0.2,0.05,0.1)
        ax.plot_surface(Xc, Yc, Zc, alpha=0.5, color='c')

    if s == 'sphere':
        ax = fig.add_subplot(111, projection='3d')
        # Make data
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = 10 * np.outer(np.cos(u), np.sin(v))
        y = 10 * np.outer(np.sin(u), np.sin(v))
        z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
        # Plot the surface
        ax.plot_surface(x, y, z, color='c')

    plt.show()


def arrange(n, s):
    r = []
    if s == 'line':
        r = [n]
        return r
    if s == 'rect':
        f = int(math.sqrt(s)) + 1
        r.append(f)
        s -= f
        while s > f:
            r.append(2)
            s -= 2
        r.append(s)
        return r
    if s == 'circle':
        h = s / 2
        r = [1]
        while h >= 2:
            r.append(2)
            h -= 2
        if h:
            r.append(1)
        return r


def donutprint():
    # create data
    size_of_groups=[1]

    # Create a pieplot
    plt.pie(size_of_groups, colors = ['orange'])
    #plt.show()

    # add a circle at the center
    my_circle=plt.Circle( (0,0), 0.4, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)

    plt.show()

# print heart template
def printHeart():
    t = np.arange(0,2*np.pi, 0.1)
    x = 16*np.sin(t)**3
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    plt.plot(x,y)
    plt.show()

def emojiPrint(m, n):
    print(emoji.emojize(':{}: '.format(m) * n))


def emojiPrintList(m):
    for i in m:
        print(emoji.emojize(':{}: '.format(i)), end='')


def emojiPrintWidth(m, n, w):
    for i in range(w):
        if i < n/2 or i >= (w-n/2) :
            print(emoji.emojize(':{}: '.format(m)), end=" ")
        else:
            print(" ", end=" ")

# function to print circle pattern 
def emojiPrintCircle(m, radius): 
      
    # dist represents distance to the center 
    # for horizontal movement 
    for i in range((2 * radius)+1): 
   
        # for vertical movement 
        for j in range((2 * radius)+1): 
              
            dist = math.sqrt((i - radius) * (i - radius) + 
                  (j - radius) * (j - radius)) 
   
            # dist should be in the 
            # range (radius - 0.5) 
            # and (radius + 0.5) to print stars(*) 
            if (dist > radius - 0.5 and dist < radius + 0.5):  
                print(emoji.emojize(':{}: '.format(m)), end="") 
            else: 
                print(" ",end="")       
        print() 

'''
def emojiPrintShapes(m, n, s):
    if s == 'line':
        emojiPrint(m, n)
    elif s == 'rect':
        r = arrange(n, s)
        for i in r:
            emojiPrintWidth(m, i, r[0])

'''
