#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from random import random
import math
import operator
import matplotlib
import matplotlib.pyplot as plt


# TODO: implementar a função de gerar imagem
class Knn:

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
        """
        filename = self.escolhe_data()
        with open(filename, 'rt') as arquivo_csv:
            lines = csv.reader(arquivo_csv)
            conjunto_dados = list(lines)
            for x in range(len(conjunto_dados) - 1):
                for y in range(4):
                    conjunto_dados[x][y] = float(conjunto_dados[x][y])
                """
                Gera um valor randômico, se for menor que a porcentagem de elementos utilizados, será adicionado em um 
                conjunto de dados que serão treinados. 
                Caso o valor gerado seja maior que o split, será adicionado no cojunto de dados teste
                """
                if random() < split:
                    conjunto_treinados.append(conjunto_dados[x])
                else:
                    conjunto_teste.append(conjunto_dados[x])

    @staticmethod
    def distancia_euclidiana(valor1, valor2, tamanho):
        """
        Essa função calcula a distância euclidiana entre dois conjuntos de dados
        """
        dist = [pow((valor1[x] - valor2[x]), 2) for x in range(tamanho)]

        return math.sqrt(sum(dist))

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

    @staticmethod
    def responsavel(vizinhos):
        votos = {}
        for x in range(len(vizinhos)):
            response = vizinhos[x][-1]
            if response in votos:
                votos[response] += 1
            else:
                votos[response] = 1
        ordena_votos = sorted(votos.items(), key=operator.itemgetter(1), reverse=True)
        return ordena_votos[0][0]

    @staticmethod
    def calcula_acerto(conjunto_teste, nome_dado):
        correto = 0
        for x in range(len(conjunto_teste)):
            if conjunto_teste[x][-1] == nome_dado[x]:
                correto += 1
        return (correto / float(len(conjunto_teste))) * 100.0

    def run(self):
        k = int(input("Digite um valor para K: "))

        conjunto_treinados = []
        conjunto_teste = []
        self.carrega_arquivo(0.67, conjunto_treinados, conjunto_teste)

        print('Conjunto treinado: ' + str(len(conjunto_treinados)))
        print('Conjutno de teste: ' + str(len(conjunto_teste)))

        nome_dado = []

        for x in range(len(conjunto_teste)):
            vizinhos = self.separa_vizinhos(conjunto_treinados, conjunto_teste[x], k)
            result = self.responsavel(vizinhos)
            nome_dado.append(result)
            if result == conjunto_teste[x][-1]:
                print('Valor obtido: {}, valor real: {} -> ACERTOU'.format(str(result), str(conjunto_teste[x][-1])))
            else:
                print('Valor obtido: {}, valor real: {} -> ERROU'.format(str(result), str(conjunto_teste[x][-1])))
        acerto = self.calcula_acerto(conjunto_teste, nome_dado)
        print('Taxa de acerto: {0:.3f}%'.format(acerto))


if __name__ == '__main__':
    obj = Knn()
    obj.run()
