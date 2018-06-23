#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import random
import math
import operator
import matplotlib
import matplotlib.pyplot as plt


class Knn():

    def escolhe_data(self):
        """
        Menu para escolher qual conjunto de dados será utilizado pelo algoritmo
        """
        print("Escolha um conjunto de dados ")
        print("1. Iris")
        file = input()
        if file == 'iris' or file == "Iris" or file == '1':
            return 'iris.data'
        self.escolhe_data()

    def carrega_arquivo(self, split, conjunto_treinados, conjunto_teste):
        """
        Lê os dados do arquivo e separa de forma adequada, entre um conjunto de testes e um conjunto que será treinado
        :param split: porcentagem  dadosde do arquivo que serão utilizadas
        :param conjunto_treinados: conjunto de dados treinados
        :param conjunto_teste: conjunto de
        :return:
        """
        filename = self.escolhe_data()
        with open(filename, 'rt') as arquivo_csv:
            lines = csv.reader(arquivo_csv)
            conjutno_dados = list(lines)
            for x in range(len(conjutno_dados) - 1):
                for y in range(4):
                    conjutno_dados[x][y] = float(conjutno_dados[x][y])
                if random.random() < split:
                    conjunto_treinados.append(conjutno_dados[x])
                else:
                    conjunto_teste.append(conjutno_dados[x])

    def distancia_euclidiana(self, valor1, valor2, tamanho):
        """
        Essa função calcula a distância euclidiana entre dois conjuntos de dados
        """
        dist = [pow((valor1[x] - valor2[x]), 2) for x in range(tamanho)]

        return math.sqrt(sum(dist))

    # Calculate distance from training data for every test point and store it
    def separa_vizinhos(self, conjunto_treinados, instancia_teste, k):
        distancias = []
        tamanho = len(instancia_teste) - 1
        for x in range(len(conjunto_treinados)):
            dist = self.distancia_euclidiana(instancia_teste, conjunto_treinados[x], tamanho)
            distancias.append((conjunto_treinados[x], dist))
        distancias.sort(key=operator.itemgetter(1))
        vizinhos = []
        for x in range(k):
            vizinhos.append(distancias[x][0])
        return vizinhos

    def getResponse(self, vizinhos):
        classVotes = {}
        for x in range(len(vizinhos)):
            response = vizinhos[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

    def getAccuracy(self, conjunto_teste, predictions):
        correct = 0
        for x in range(len(conjunto_teste)):
            if conjunto_teste[x][-1] == predictions[x]:
                correct += 1
        return (correct / float(len(conjunto_teste))) * 100.0

    def main(self):
        conjunto_treinados = []
        conjunto_teste = []
        self.carrega_arquivo(0.67, conjunto_treinados, conjunto_teste)
        print('Conjunto treinado: ' + str(len(conjunto_treinados)))
        print('Conjutno de teste: ' + str(len(conjunto_teste)))

        predictions = []
        k = int(input("Digite um valor para K: "))
        for x in range(len(conjunto_teste)):
            vizinhos = self.separa_vizinhos(conjunto_treinados, conjunto_teste[x], k)
            result = self.getResponse(vizinhos)
            predictions.append(result)
            print('Valor obtido: {}, valor real: {}'.format(str(result), str(conjunto_teste[x][-1])))
        accuracy = self.getAccuracy(conjunto_teste, predictions)
        print('Taxa de acerto: {0:.3f}%'.format(accuracy))


if __name__ == '__main__':
    # iris.data

    # file = input("Digite o nome do arquivo: ")
    # obj = Knn(file)
    obj = Knn()
    obj.main()
