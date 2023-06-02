import pandas as pd

# Charger le fichier xlsx
dataset = pd.read_excel('/Users/nilsonsimao/Documents/Machine_Learnig/TP5/mushrooms.xlsx')
print(dataset.head())


# Variables quantitatives (X)
x = dataset.drop('classe', axis=1)
x_quant =pd.get_dummies(x)
# Variable cible (y)
y = dataset['classe']

# Afficher les premières lignes des variables quantitatives (X)
print(x_quant.head())

# Afficher les premières lignes de la variable cible (y)
#print(y.head())
