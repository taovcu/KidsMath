import matplotlib.pyplot as plt
import emoji


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
