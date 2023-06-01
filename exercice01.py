import random
import math
import statistics
import os
import glob


# 1 - Faire itération pour remplir manuellement un fichier nommé nom.txt avec 5 noms les en dessus des autres


with open('nom.txt','w')  as f:
    for i in range(5):
        a = input()
        f.write("{} \n".format(a))

# 2 : Faire une itération pour remplir automatiquement un fichier nommé nombre.txt de 10 nombres les uns au dessous des autres

with open('nombre.txt','w') as f:
    for i in range(10):
        f.write("{} \n".format(i))
