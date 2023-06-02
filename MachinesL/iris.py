import numpy as np
import matplotlib.pyplot as plt

# importation do dataset
from sklearn.datasets import load_iris

iris = load_iris()

# Definition des axes
x = iris.data
y = iris.target

# Affichage du graphique : 1

plt.scatter(x[:,0],x[:,1], c = y)
plt.show()

# Affichage du graphique : 2

from sklearn.decomposition import PCA

pca = PCA()

projection =pca.fit_transform(x)
plt.scatter(projection[:,0], projection[:,1], c = y, cmap = "plasma")
plt.colorbar()
plt.show()
