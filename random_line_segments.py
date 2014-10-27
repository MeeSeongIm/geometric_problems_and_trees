
# prints 20 random line segements 

import numpy as np
import matplotlib.pyplot as plt

data = []
for _ in xrange(20):
    data.append((np.random.rand(), np.random.rand()))
    data.append((np.random.rand(), np.random.rand()))
    data.append("r")
print("Now plotting: \n")
plt.plot(*data)
print("Printed 20 random line segments in a unit square.") 



