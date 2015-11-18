import math
def pifun(d):
  # This function will find pi to the NTH digit, so lets get started
  print "Lets round the pi number!!"
  pinum = float(math.pi)
  pinum = round(pinum, d)
  print "The pi number to the", d, "digits is", pinum

pifun(3)
