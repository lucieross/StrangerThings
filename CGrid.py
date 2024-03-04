import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlim([0,150])
ax.set_ylim([0,150])

ax.plot([0, 150], [100, 100])
ax.grid(visible=True)
plt.show()
