import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = load_iris()

x = iris.data
y = iris.target

x,y = make_classification(random_state=0)
x_train,x_test,y_train,y_test = train_test_split(x,y, random_state=0)

model = SVC(random_state=0)
model.fit(x_train,y_train)
SVC(random_state=0)

confusion_matrix(y_test, model.predict(x_test))
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test,model.predict(x_test)))
disp = disp.plot(cmap="magma")
plt.show()

