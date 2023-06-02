import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger le fichier

dataset= pd.read_csv('/Users/nilsonsimao/Documents/Machine_Learnig/TP5/diamonds.csv')
print(dataset.head())

#Description du dataset : La description ce sont les statistiques du dataset tel que la moyenne, le min, max, etc

description = dataset.describe()
print(description)

# Affichage de la relaction carat et price

plt.scatter(dataset['carat'], dataset['price'])
plt.xlabel('Caract')
plt.ylabel('Price')
plt.title('Correlaction entre Carat et Price')
plt.show()