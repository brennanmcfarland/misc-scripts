import matplotlib.pyplot as plt

def graphcurve(xmin,xmax,xres,function, *args):
    x,y = [],[]
    i=xmin
    while i<=xmax:
        x.append(i)
        y.append(function(x[i],*args))
        i+=xres
    return [x,y]

def line(x,m,b):
    return m*x+b
pointlist = graphcurve(0,10,1,line,0,1)
print(pointlist)

plt.plot(pointlist)

plt.show()
