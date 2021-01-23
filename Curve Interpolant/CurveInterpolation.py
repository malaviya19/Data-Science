import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def initializeTs(xs,ys):
    tn = len(xs)
    ts = [0]*n
    for i in range(1,tn):
        v = [xs[i]-xs[i-1],ys[i]-ys[i-1]]
        ts[i] = ts[i-1] + np.linalg.norm(v,2)

    return ts

def curveLength(x,y,tsMax):
    n = 1000
    ts = np.linspace(0,tsMax,n)

    l = 0.0
    for i in range(1,n):
        l = l + np.sqrt((x(ts[i]) - x(ts[i-1]))**2 + (y(ts[i]) - y(ts[i-1]))**2)

    return l

xs = [-0.1,1.1,2.0,4.1,3.0,4.1]
ys = [-2.3,1.9,3.3,0.2,1.0,2.2]
n = len(xs)
ts = initializeTs(xs,ys)

Sx = CubicSpline(ts,xs)
Sy = CubicSpline(ts,ys)
curveLength(Sx,Sy,ts[n-1])

values = 1000
plotT = np.linspace(ts[0],ts[n-1],values)
plt.plot(Sx(plotT),Sy(plotT),'r')
plt.plot(xs,ys,'bo')
plt.show()
