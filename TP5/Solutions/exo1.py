import numpy as np
import matplotlib.pyplot as plt


# Définition des valiables du modèle

np.random.seed(1)
a = np.array([[1.05, -0.35], [0.35, 1.05]])
b = np.array([[3.5, 0], [0, 2]])

# Définition des classes du modèle

classe1 = (np.random.randn(100,2)).dot(a).dot(b)
classe2_1 = np.random.randn(25,2)+[-10, 2]
classe2_2 = np.random.randn(25,2)+[-7, -2]
classe2_3 = np.random.randn(25,2)+[-2, -6]
classe2_4 = np.random.randn(25,2)+[5, -7]

dataSet = np.concatenate((classe1, classe2_1, classe2_2, classe2_3, classe2_4))
etiq_1 = np.ones(100, dtype=int)
etiq_2 = np.zeros(100, dtype=int)
etiquettes = np.concatenate((etiq_1, etiq_2))

# Affichage
cmp = np.array(['y','grey'])
plt.figure(figsize=(10,6))
plt.scatter(dataSet[:,0],dataSet[:,1], c=cmp[etiquettes], s=50)
#plt.show()

# Amélioration du résultat
from sklearn.model_selection import train_test_split
plt.figure(figsize=(10,6))
X_train, X_test, y_train, y_test = train_test_split(dataSet, etiquettes, test_size=0.35)
plt.scatter(X_train[:,0],X_train[:,1],c=cmp[y_train],s=50)
plt.scatter(X_test[:,0],X_test[:,1],c='none',s=50,edgecolors=cmp[y_test])
plt.show()