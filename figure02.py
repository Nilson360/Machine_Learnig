import numpy as np
import matplotlib.pyplot as plt


x = np.random.random(20)
y = np.random.random(20)
z = np.sin(3*x**2+y**2)

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z)

ax.plot(x, z, 'r+', zdir='y', zs=2.0)
ax.plot(y, z, 'g+', zdir='x', zs=1.0)
ax.plot(x, y, 'k+', zdir='z', zs=-2.0)

ax.set_xlim([-1.5, 2.0])
ax.set_ylim([-2.0, 2.0])
ax.set_zlim([-1.0, 2.0])

plt.show()
