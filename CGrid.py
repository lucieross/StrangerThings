import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.set_xlim([0,150]) #Creates Line
ax.set_ylim([0,150])
ax.plot([0, 150], [100, 100])

xpoints = np.array([75]) #Creates Placeholder for cannon
ypoints = np.array([100])
plt.plot(xpoints, ypoints, 's')

ax.grid(visible=True) #Creates Grid Lines
plt.show()
