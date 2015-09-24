import matplotlib.pyplot as plt
import math

def graphcurve(xmin,xmax,xres,function, *args):
    x,y = [],[]
    i=0
    while xmin+i*xres<=xmax:
        x.append(xmin+i*xres)
        y.append(function(x[i],*args))
        i+=1
    return [x,y]

def line_slope_intercept(x,m,b):
    return m*x+b
def line_point_slope(x,m,x1,y1):
    return m*(x-x1)+y1

points = graphcurve(0,10,.01,math.tan)
plt.plot(points[0],points[1])
plt.show()
