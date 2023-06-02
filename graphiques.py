# Importation des librairies
import numpy as np
import matplotlib.pyplot as plt

# Définition du dataset
dataset = {f"Data {i}": np.random.randint(1,10,100) for i in range(6)}

# définitions des données de la courbe
def courbe(keys, dataset, i):
    plt.plot(dataset[keys], label="Tracé de la courbe: " + str(i), lw=i)
    plt.xlabel('axe x de :' + keys)
    plt.ylabel('axe y de ' +keys)
    plt.title(keys)
    plt.legend(loc='upper left')

# insctructions pour dessiner la courbe
def dessiner (dataset):
    n=len(dataset)
    plt.figure(figsize=(20,35))
    i=1
    for keys in dataset.keys():
        if n<n/2 + 1:
            plt.subplot(n,1,i)
            courbe(keys,dataset,i)
        else:
            plt.subplot(n,2,i)
            courbe(keys,dataset,i)
        i=i+1

# Affichaque de la courbe
dessiner(dataset)
plt.savefig('exo.png')
plt.show()