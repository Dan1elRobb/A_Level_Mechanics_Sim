import math
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0,5*np.pi,0.1)
y = np.sin(x)
ax.plot(x,y)
ax.plot(x+np.pi/2,y,color="red")
