import random
import math
import statistics
import os
import glob
import numpy as np

"""
Faire 2 matrices(4,6) d’entiers pris au hasard inférieur à 10 avec numpy nommés A et B
• Faire la somme des tous les éléments de la matrice A
• Faire la somme de toutes les colonnes de la matrice A dans un tableau nommé C
• Faire la somme de toutes les lignes de la matrice A dans un tableau nommé D
• Faire la somme cumulée de toutes les valeurs de la matrice B dans un tableau nommé E
• Faire la moyenne de tous les entiers de la matrice B dans une variable nommée F
• Faire l’enregistrement des positions des valeurs minimales dans toutes les colonnes de la matrice A
 dans un tableau nommé G
"""
# QUestion 1 :
A = np.random.randint(0,10,[4,6])
B = np.random.randint(0,10,[4,6])
# Question 2:
C = A.sum(axis =0)
#Question 3:
D = A.sum(axis =1)

#Question 4
E = B.cumsum()

#Question 5
F = B.mean()

#Question 6
G = A.argmin(axis=1)

#Affichage

#print(G)

"""
Faire l’écart type des valeurs du tableau B
• Faire la variance sur les valeurs du tableau A
• Tracer une matrice de corrélation pour la matrice B
• Faire 2 tableaux nommés H et I qui donnent les valeurs et les fréquences des valeurs de la matrice A
"""

# Question1 :
ecart_Type=B.std()

# Question 2:
Variance=A.var()

#Question 3:
m_Correlation=np.corrcoef(B)

H,I = np.unique(A,return_counts=True)
for i,j in zip(H[I.argsort()], I[I.argsort()]):
    print(f'Entier {i}: fréquence {j}')

np.isnan(B)

#Affichage

print(Variance)