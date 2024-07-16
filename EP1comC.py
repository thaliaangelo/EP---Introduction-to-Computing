#################################################################
## AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
## DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
## TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
## DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
## DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
## OU PLÁGIO.
## DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
## DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
## SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
## DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
## DIVULGADOS NA PÁGINA DA DISCIPLINA.
## ENTENDO QUE EPS SEM ESTE CABEÇALHO NÃO SERÃO CORRIGIDOS E,
## AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.
## Nome : Thalia Angelo Gomes da Silva
## NUSP : 15489751
## Turma: 45
## Prof.: Roberto Hirata Jr.
## Referências:
#################################################################

import matplotlib.pyplot as plt
from random import randint
from sys import platform
import time as T
import math
import ctypes
libsort = ctypes.CDLL('./libsortings.so')

libsort.selection.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.bubble.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.insertion.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.counting.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]


def mediaT(T, n):
    ''' 
    Calcula a média dos valores de uma lista.
    Entradas: Uma lista e sua quantidade de elementos.
    Saída: A média dos valores da lista.
    '''

    soma = 0
    for i in range (n):
        soma = soma + T[i]
    media = soma / n
    return(media)

def varT(T, n):
    '''
    Calcula a variância populacional dos valores de uma lista.
    Entradas: Uma lista e sua quantidade de elementos.
    Saída: A variância populacional dos valores da lista.
    '''

    media_valores = mediaT(T, n)
    soma_var = 0
    for i in range(n):
        soma_var = soma_var + ((T[i] - media_valores) * (T[i] - media_valores))

    variancia_quadrado = soma_var / n
    variancia = math.sqrt(variancia_quadrado)
    return(variancia)

def selection(V, n):
    '''
    Importa a função do SelectionSort escrita em C e recebe uma lista com o seu
    respectivo tamanho e ordena a mesma.
    Entradas: Uma lista e sua quantidade de elementos.
    Saída: 0.
    '''
    pV = (ctypes.c_int *n) (*V)
    libsort.selection(pV, n)

def bubble(V, n):
    '''
    Importa a função do BubbleSort escrita em C e recebe uma lista com o seu
    respectivo tamanho e ordena a mesma.
    Entradas: Uma lista e sua quantidade de elementos.
    Saída: 0.
    '''
    pV = (ctypes.c_int *n) (*V)
    libsort.bubble(pV, n)


def insertion(V, n):
    '''
    Importa a função do InsertionSort escrita em C e recebe uma lista com o seu
    respectivo tamanho e ordena a mesma.
    Entradas: Uma lista e sua quantidade de elementos.
    Saída: 0.
    '''
    pV = (ctypes.c_int *n) (*V)
    libsort.insertion(pV, n)


def counting(V, n):
    '''
    Importa a função do CountingSort escrita em C e recebe uma lista com o seu
    respectivo tamanho e ordena a mesma.
    Entradas: Uma lista e sua quantidade de elementos.
    Saída: 0.
    '''
    pV = (ctypes.c_int *n) (*V)
    libsort.counting(pV, n)


def embaralha(V, n, p):
    '''
    Troca dois elementos de posições uma determinada quantidade de vezes.
    Entradas: Uma lista, sua quantidade de elementos e um inteiro positivo que
    esteja no intervalo [0, 100].
    Saída: 0.
    '''

    trocas = (n * p) / 100
    t = 0

    while(t < trocas):
        i = randint(0, (n - 1))
        j = randint(0, (n - 1))
        sup = V[i]
        V[i] = V[j]
        V[j] = sup
        t = t + 1

    return(0)
    
    

def timeMe(func, V, n, m, p):
    '''
    Calcula o tempo que uma função gasta para ordenar uma lista, guarda os tempos 
    encontrados e calcula a média e a variância populacional da lista de tempos de uma função.
    Entradas: Uma função, uma lista, a quantidade de elementos da lista, um inteiro positivo
    para a quantidade de vezes que a função será chamada e um inteiro positivo que esteja no 
    intervalo [0, 100].
    Saídas: A média e a variância dos tempos encontrados.
    '''

    tempos = []
    for i in range(m):
        embaralha(V, n, p)
        start = T.process_time()
        func(V, n)
        finish = T.process_time()
        Vtime = finish - start
        tempos.append(Vtime)
    
    media_tempos = mediaT(tempos, m)
    var_tempos = varT(tempos, m)
    return(media_tempos, var_tempos)


def GraficaSortings(mpontos, mediaMCMPi, desvioMCMPi):
    '''
    Usa as médias e as variâncias encontradas para desenhar um gráfico.
    Entradas: Uma lista que representa os valores do eixo x, uma lista da
    média dos tempos de uma uma função e uma lista da variância dos tempos
    de uma função.
    Saída: 0
    '''

    plt.errorbar(mpontos, mediaMCMPi, yerr=desvioMCMPi, fmt = '-o')
    return(0)


def main():
    '''
    Organiza as chamadas das funções e as criações das listas para serem usadas nos experimentos.
    Entrada: Nenhuma.
    Saída: 0.
    '''

    #Experimento com C
    media_1 = [[0 for j in range(5)] for i in range(4)]
    var_1 = [[0 for j in range(5)] for i in range(4)]

    funcs_1 = [bubble, insertion, selection, counting]
    tamanhos_1 = [1000, 5000, 10000, 50000, 100000]
    nomes_1 = ["BubbleSort", "InsertionSort", "SelectionSort", "CountingSort"]
    cores_1 = ["#069AF3", "#FF7F50", "#15B01A", "#DC143C"]

    W1 = [(randint(0, 9999)) for i in range(1000)]
    W2 = [(randint(0, 9999)) for i in range(5000)]
    W3 = [(randint(0, 9999)) for i in range(10000)]
    W4 = [(randint(0, 9999)) for i in range(50000)]
    W5 = [(randint(0, 9999)) for i in range(100000)]

    Wtmp1 = list(W1)
    Wtmp2 = list(W2)
    Wtmp3 = list(W3)
    Wtmp4 = list(W4)
    Wtmp5 = list(W5)

    Lista_total_1 = []
    Lista_total_1.append(Wtmp1)
    Lista_total_1.append(Wtmp2)
    Lista_total_1.append(Wtmp3)
    Lista_total_1.append(Wtmp4)
    Lista_total_1.append(Wtmp5)

    for i in range(4):
        for j in range(5):
            media_1[i][j], var_1[i][j] = timeMe(funcs_1[i], Lista_total_1[j], tamanhos_1[j], 5, 0)

        Lista_total_1.clear()
        Lista_total_1.append(Wtmp1)
        Lista_total_1.append(Wtmp2)
        Lista_total_1.append(Wtmp3)
        Lista_total_1.append(Wtmp4)
        Lista_total_1.append(Wtmp5)

    
    for i in range(4):
        GraficaSortings(tamanhos_1, media_1[i], var_1[i])
        plt.plot(tamanhos_1, media_1[i], label = nomes_1[i], color = cores_1[i])

    plt.xlabel("Quantidade de elementos")
    plt.ylabel("Tempo (s)")
    plt.yscale('log')
    plt.title("Experimento 1")
    plt.legend()
    plt.savefig("Experimento1_C")

    return(0)

main()