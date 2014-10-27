
# prints i random line segements 

import numpy as np
import matplotlib.pyplot as plt

i=20
data = [] 
for _ in xrange(i):
    data.append((np.random.rand(), np.random.rand()))  # x1, x2 
    data.append((np.random.rand(), np.random.rand()))  # y1, y2    
    data.append("r")                                   # the line segment connecting (x1,y1) and (x2,y2) 
print("Now plotting: \n")
plt.plot(*data)
print("Printed %s random line segments in a unit square." % i) 

# counts the number of intersection points 



  
