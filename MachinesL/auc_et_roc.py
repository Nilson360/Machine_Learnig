import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm
from sklearn.metrics import auc, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split

# Ensemble de données

y = np.random.randint(0,2,150)
random_state = np.random.RandomState(0)
x = random_state.randn(150,3)

# Decoupage de l'ensemble de données

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= .5, random_state=5)

#Predictions
clf = svm.SVC(kernel='linear')
y_score = clf.fit(x_train,y_train).decision_function(x_test)

#calcul de la coubre ROC

fpr,tpr,seuil = roc_curve(y_true = y_train, y_score= y_score, pos_label = 1)
auc = auc(fpr, tpr)

roc = roc_auc_score(y_test, y_score)

# Dessin de courbe ROC et AUC

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2,label = 'Courbe ROC')
plt.plot([0,1], [0,1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.0])
plt.xlabel('Taux de faux positifs')
plt.ylabel('Taux de vrais positifs')
plt.title('Courbe : Receiver Operating Charecteristic')
plt.legend(loc="lower right")
plt.show()