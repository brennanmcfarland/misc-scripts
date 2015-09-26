import matplotlib.pyplot as plt
import math

def graphfunction(xmin,xmax,xres,function, *args):
    x,y = [],[]
    i=0
    while xmin+i*xres<=xmax:
        x.append(xmin+i*xres)
        y.append(function(x[i],*args))
        i+=1
    return [x,y]

def koch_snowflake(iterations):
    x,y = [],[]
    for i in range(0,iterations):
        iterationpoints = iterate_koch_snowflake(0.0,1.0)
        x.insert(x.size/(2*math.pow(i)), iterationpoints[0][0])
    return [x,y]

def iterate_koch_snowflake(a,b):
    "a and b are points; [x,y]"
    newa = [(a[0]+(b[0]-a[0])/3),((b[1]-a[1])/(b[0]-a[1])(b[0]-a[0])/3+a[1])]
    newb = [(a[0]+2*(b[0]-a[0])/3),(2*(b[1]-a[1])/(b[0]-a[1])(b[0]-a[0])/3+a[1])]
    newapex = [newb[0]-newa[0],newb[1]-newa[1]]
    return [newa,newapex,newb]

def line_slope_intercept(x,m,b):
    return m*x+b

def line_point_slope(x,m,x1,y1):
    return m*(x-x1)+y1

points = graphfunction(0,10,.01,math.tan)
plt.plot(points[0],points[1])
plt.show()
