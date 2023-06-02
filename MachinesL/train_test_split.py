# Principe d'évaluation :

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()

# Definition des axes
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2,random_state=5 )

print("Data set ", x.shape)
print("Train set ", x_train.shape)
print("Test set ", x_test.shape)

# Affichage

plt.figure(figsize=(12,5))
plt.subplot(122)
plt.scatter(x_train[:,0],x_train[:,1], c = y_train)
plt.title('Train set')
plt.subplot(121)
plt.scatter(x_test[:,0],x_test[:,1],  c= y_test)
plt.title('Test set')
#plt.show()

# Apprentissage du modèle

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=1)
model.fit(x_train, y_train)

print('Train score: ', model.score(x_train, y_train))
print('Train score [Test]: ', model.score(x_test, y_test))