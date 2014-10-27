# prints i random line segements 

import numpy as np
import matplotlib.pyplot as plt
 

class point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

i=2
data = [] 
for _ in xrange(i):
    data.append((np.random.rand(), np.random.rand()))  # x1, x2 
    data.append((np.random.rand(), np.random.rand()))  # y1, y2    
    data.append("r")                                   # the line segment connecting (x1,y1) and (x2,y2) 
print("Now plotting: \n")
plt.plot(*data)
print("Printed %s random line segments in a unit square. \n" % i) 
 
points = []

for j in range(i):
    points.append(((data[3*j][0],data[3*j+1][0]),(data[3*j][1],data[3*j+1][1])))
print(points) 

#for j in range(i):
#    def line(t):
#        x = data[j][0]  + t*(data[j][1]-data[j][0])
#        y = data[j+1][0]+t*(data[j+1][1]-data[j+1][0]) 
#        return x, y

# bottom: short-cut to finding the intersection points. 
# redo the code below using a left-skewed priority queue red-black BST algorithm. 
# from http://bryceboe.com/images/2006/10/intersect.py  

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


a = point(points[0][0][0],points[0][0][1])
b = point(points[0][1][0],points[0][1][1])
c = point(points[1][0][0],points[1][0][1])
d = point(points[1][1][0],points[1][1][1])


print intersect(a,b,c,d)
print intersect(a,c,b,d)
print intersect(a,d,b,c)  





