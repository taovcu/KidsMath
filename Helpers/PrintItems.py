import matplotlib.pyplot as plt
import emoji

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
