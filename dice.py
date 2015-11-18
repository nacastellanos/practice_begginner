import random
# A simple dice code that generates random
# numbers for a certain number of times
def dice_roll():
    print "Lets roll it up!!!"
    result = random.randrange(1,6)
    result = int(result)
    print 'Your result is %d' % (result)
    return

def dice(n):
    for x in range(1, n):
        print 'roll # %d ' % (x)
        dice_roll()
    return

dice(6)
