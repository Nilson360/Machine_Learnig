import matplotlib.pyplot as plt
from sklearn import datasets

diabetes = datasets.load_diabetes()
iris = datasets.load_iris()
digits = datasets.load_digits()


x = iris.data
y = iris.target

