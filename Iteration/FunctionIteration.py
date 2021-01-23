import math

def fx(x):
    return math.sin(math.pi*x) + pow(x,2)

def gx(x):
    return (1/(2*math.pi))*math.sin(math.pi*x) - (1/(2*math.pi))*pow(x,2) + x
