from sklearn.datasets import load_iris # carrega a base de dados
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np


class Knn():

    # TODO: copiar os dados para um arquivo
    def __init__(self):
        self.iris = load_iris()

    # TODO: criar uma nova funcao para gerar imagem com os valores do KNN
    def knn_iris(self):

        # Pega os valores do database
        X_train, X_test, y_train, y_test = train_test_split(self.iris['data'], self.iris['target'], random_state=0)
        fig, ax = plt.subplots(3, 3, figsize=(15, 15))

        # TODO: gerar a imagem a partir desses dados
        for i in range(3):
            for j in range(3):
                ax[i, j].scatter(X_train[:, j], X_train[:, i + 1], c=y_train, s=60)
                ax[i, j].set_xticks(())
                ax[i, j].set_yticks(())

                if i == 2:
                    ax[i, j].set_xlabel(self.iris['feature_names'][j])
                if j == 0:
                    ax[i, j].set_ylabel(self.iris['feature_names'][i + 1])
                if j > i:
                    ax[i, j].set_visible(False)

        knn = KNeighborsClassifier(n_neighbors=1) # escolha de quantos vizinhos utilizados
        print(knn.fit(X_train, y_train))
        X_new = np.array([[5, 2.9, 1, 0.2]])
        print(X_new.shape) # mostra quantas features diferentes possui
        prediction = knn.predict(X_new) # pega o provedor do dado
        print(prediction)
        print(self.iris['target_names'][prediction]) # exibe o nome do provedor
        # print(knn.score(X_test, y_test))
        return knn.score(X_test, y_test) # taxa de acerto


if __name__ == '__main__':
    obj = Knn()
    print(obj.knn_iris())
