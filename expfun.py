__author__ = 'HP'
import math

def expfun(x,d):
    # this function will find the nth digit of the exp function
    print "lets roud the the exponent of 1"
    d = int(d)
    enum = float(math.exp(x))
    enum = round(enum, d)
    print "the exponent of", x, "to the", d, "digits is", enum
    return

expfun(3,3)
