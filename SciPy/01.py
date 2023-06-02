import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

y = np.array([8,29,40])
x = np.linspace(20,30,3)

f = interp1d(x,y, kind= 'linear')
X_new = np.linspace(20,30,100)

plt.plot(x,y,'o', label= ' Données')
plt.plot(X_new, f(X_new), label = 'Lineaire')
plt.legend(loc= 'best')
plt.show()