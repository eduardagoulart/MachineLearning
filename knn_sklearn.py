from sklearn.datasets import load_iris # carrega a base de dados
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import datasets

import numpy as np

df = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(df.data, df.target, test_size=0.5, random_state=0)

def euclidean_distance(a,b):
    dist = np.linalg.norm(a-b)
    return dist