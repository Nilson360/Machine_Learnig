import numpy as np
import matplotlib.pyplot as plt

nb_donnes = 50
Liste_X = np.linspace(-4.0, 5.0, nb_donnes)
Liste_Y = np.linspace(-3.0, 2.0, nb_donnes)
X,Y = np.meshgrid(Liste_X, Liste_Y)

def f(x,y):
    return 1/(2+x**2+y**2)

fig = plt.figure(figsize = (10, 5))
ax = plt.axes(projection= '3d')
ax.view_init(40,-30)
fig = ax.plot_surface(X,Y,f(X,Y), cmap = 'magma')
plt.colorbar(fig)
plt.show()