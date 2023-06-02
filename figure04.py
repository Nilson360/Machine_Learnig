import matplotlib.pyplot as plt
import numpy as np

x = np. linspace (-1,1,100)
y = 3*x**3

# mettre les axes au centre
fig = plt.figure ()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines ['right'].set_color('none')
ax.spines ['top'].set_color ('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.title('Courbe d\'une fonction cubique')

# Ajouter le tracé de la courbe
plt.plot(x,y)
plt.show()