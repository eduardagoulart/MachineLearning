#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lê um arquivo CSV
from csv import reader
# Gera números aleatórios
from random import random
# Possui a operação de raíz quadrada
from math import sqrt
# Retorna o valor em uma posição
from operator import itemgetter
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
            conjunto_dados = list(reader(arquivo_csv))
            for x in range(len(conjunto_dados) - 1):
                for y in range(4):
                    conjunto_dados[x][y] = float(conjunto_dados[x][y])
                """
                Gera um valor randômico que define a quantidade de dados utilizados como treinamento e como teste,
                desta forma, com a geração aleatória, aumenta a curva de aprendizagem.
                Se o valor for menor que a porcentagem de split, será adicionado em um conjunto de dados que serão 
                treinados. Caso o valor gerado seja maior que o split, será adicionado no cojunto de dados teste
                """
                if random() < split:
                    conjunto_treinados.append(conjunto_dados[x])
                else:
                    conjunto_teste.append(conjunto_dados[x])

    @staticmethod
    def distancia_euclidiana(valor1, valor2, tamanho):
        """
        Função calcula a distância euclidiana entre dois conjuntos de dados
        Com o tamanho do dado analisado, eleva cada posição (cada dados, valor1 e valor2, são vetores) dele ao quadrado
        e adiciona em um vetor a distância será a raíz quadrada das somas dos valores do vetor
        """
        return sqrt(sum([pow((valor1[x] - valor2[x]), 2) for x in range(tamanho)]))

    def separa_vizinhos(self, conjunto_treinados, conjunto_teste, k):
        """
        Dado um conjunto de valores treinados e um conjunto de teste, é calculado sua distância eucliadiana
        A quantidade de vizinhos que serão selecionados (k), determina quantos valores dentro do raio da distância
        serão utilizados. 
        """
        tamanho = len(conjunto_teste) - 1

        """
        para um conjunto de treinamento e teste, é calculada a distância euclidiana entre eles, adicionados a um vetor
        que é ordenado de forma a pegar os primeiros k vinhos do conjunto de treinamento
        """
        distancias = [(conjunto_treinados[i], self.distancia_euclidiana(conjunto_teste, conjunto_treinados[i], tamanho))
                      for i in range(len(conjunto_treinados))]
        # ordena o vetor
        distancias.sort(key=itemgetter(1))
        # pega os primeiros k vizinhos do conjunto de treinamento
        vizinhos = [distancias[i][0] for i in range(k)]

        return vizinhos

    @staticmethod
    def votos_majoritarios(vizinhos):
        votos = {}
        for x in range(len(vizinhos)):
            if vizinhos[x][-1] not in votos:
                votos[vizinhos[x][-1]] = 1
            else:
                votos[vizinhos[x][-1]] += 1
        return (sorted(votos.items(), reverse=True, key=itemgetter(1)))[0][0]

    @staticmethod
    def calcula_acerto(conjunto_teste, nome_dado):
        correto = 0
        for i in range(len(conjunto_teste)):
            if nome_dado[i] == conjunto_teste[i][-1]:
                correto += 1
        return (correto / float(len(conjunto_teste))) * 100.0

    def run(self):
        """
        a variável k representa a quantidade de vizinhos mais próximos que será utilizada na pesquisa de
        k-vizinhos. Para classificar o conjunto de vizinhos mais próximos e tomar voto da maioria, seleciona-se um
        conjunto de tamanho ímpar, para evitar que haja empates.
        """
        while True:
            k = int(input("Digite um valor ímpar para K: "))
            if k % 2 != 0:
                break

        conjunto_treinados = []
        conjunto_teste = []
        
        # Carrega os dados do arquivo, separando nas duas listas (treino e teste) de acordo com o split
        self.carrega_arquivo(0.67, conjunto_treinados, conjunto_teste)

        print('Conjunto treinado: {}'.format(str(len(conjunto_treinados))))
        print('Conjutno de teste: {}'.format(str(len(conjunto_teste))))

        nome_dado = []

        for i in range(len(conjunto_teste)):
            vizinhos = self.separa_vizinhos(conjunto_treinados, conjunto_teste[i], k)
            result = self.votos_majoritarios(vizinhos)
            nome_dado.append(result)
            if result == conjunto_teste[i][-1]:
                print('Valor obtido: {} || valor real: {} -> ACERTOU'.format(str(result), str(conjunto_teste[i][-1])))
            else:
                print('Valor obtido: {} || valor real: {} -> ERROU'.format(str(result), str(conjunto_teste[i][-1])))
        acerto = self.calcula_acerto(conjunto_teste, nome_dado)
        print('Taxa de acerto: {0:.3f}%'.format(acerto))


if __name__ == '__main__':
    """
    Executa o problema
    """
    obj = Knn()
    obj.run()
