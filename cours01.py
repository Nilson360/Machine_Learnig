import random
import math
import statistics
import os
import glob

# Déclaration des listes
Liste_1 = [i*2 for i in range(100)]
Liste_2 = ['Anne','Alain','Amid','Karim','Lina','Malisa','Nora','Patrick']

# Aléatoire des listes

r1= random.choice(Liste_1)
r2=random.choice(Liste_2)
r3=random.uniform(0,11)
r4=random.randint(1,20)
r5=random.randrange(50)
r6=random.sample(range(200),20)
r7=random.sample(range(50),random.randrange(20))
r8=random.sample(Liste_2,5)
r9=random.shuffle(Liste_2)

# affichage des randoms :

print(r1,'\n',r2,'\n',r3,'\n',r4,'\n')