#################################################################
## AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
## DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
## TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
## DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕOES
## DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
## OU PLÁGIO.
## DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
## DESSE PROGRAMA E QUE EU NÃOO DISTRIBUI OU FACILITEI A
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
## - O algoritmo CountingSort foi baseado em:
## https://www.w3schools.com/dsa/dsa_algo_countingsort.php
## - O estudo para mais detalhes do InsertionSort foi baseado em:
## https://www.ime.usp.br/~vwsetzer/alg/algoritmos.html
#################################################################

import matplotlib.pyplot as plt
from random import randint
from sys import platform
import time as T
import math

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
    Ordena uma lista, comparando um elementos com todos, o que a cada comparação
    completa o menor elemento estará próximo ao começo da lista.
    Entradas: Uma lista desordenada e sua quantidade de elementos.
    Saída: 0.
    '''

    i = 0
    while (i < (n - 1)):
        j = i + 1
        while (j < n):
            if (V[i] > V[j]):
                sup = V[i]
                V[i] = V[j]
                V[j] = sup
        
            j = j + 1
    
        i = i + 1

    return(0)
    

def bubble(V, n):
    '''
    Ordena uma lista, comparando dois a dois elementos, o que a cada comparação
    completa o maior elemento estará próximo ao final da lista.
    Entradas: Uma lista desordenada e sua quantidade de elementos.
    Saída: 0.
    '''

    i = 0

    while (i < n):
        j = 0
        while (j < (n - 1)):
            if (V[j] > V[j + 1]):
                sup = V[j]
                V[j] = V[j + 1]
                V[j + 1] = sup
        
            j = j + 1
    
        i = i + 1

    return(0)


def insertion(V, n):
    '''
    Ordena uma lista, comparando dois a dois elementos, o que a cada dois elementos trocados
    compara do índice atual até o índice 0, ordenando até o índice atual.
    Entradas: Uma lista desordenada e sua quantidade de elementos.
    Saída: 0.
    '''
    i = 0
    for i in range(n -1):
        if (V[i] > V[i + 1]):
            sup = V[i + 1]
            V[i + 1] = V[i]
            V[i] = sup
            t = i
            while(t > 0):
                if (V[t - 1] > V[t]):
                    sup_menor = V[t]
                    V[t] = V[t - 1]
                    V[t - 1] = sup_menor
                    i = i - 1
                t = t - 1
    
    return(0)




def counting(V, n):
    '''
    Ordena uma lista, em que, a cada elemento encontrado na lista dada, incrementa
    +1 em seu índice. Após isso, cria uma nova lista adicionando, em ordem crescente
    a quantidade de vezes que um certo índice ocorre.
    Entradas: Uma lista desordenada e sua quantidade de elementos.
    Saída: 0.
    '''

    V_max = 10000

    w = [0 for i in range(V_max)]

    t = 0
    while(t < n):
        x = V[t]
        w[x] = w[x] + 1
        t = t + 1

    p = 0
    for u in range((V_max + 1)):
        while(w[u] > 0):
            V[p] = u
            w[u] = w[u] - 1
            p = p + 1

    return(0)


def tim(V, n):
    '''
    Ordena uma lista com o algoritmo nativo do Python.
    Entradas: Uma lista desordenada e sua quantidade de elementos.
    Saída: 0.
    '''
    
    V.sort()
    return(0)


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

    #Experimento 1
    media_1 = [[0 for j in range(5)] for i in range(5)]
    var_1 = [[0 for j in range(5)] for i in range(5)]

    funcs_1 = [tim, bubble, insertion, selection, counting]
    tamanhos_1 = [1000, 5000, 10000, 50000, 100000]
    nomes_1 = ["TimSort", "BubbleSort", "InsertionSort", "SelectionSort", "CountingSort"]
    cores_1 = ["#069AF3", "#FF7F50", "#15B01A", "#DC143C", "#9A0EEA"]

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

    for i in range(5):
        for j in range(5):
            media_1[i][j], var_1[i][j] = timeMe(funcs_1[i], Lista_total_1[j], tamanhos_1[j], 5, 0)

        Lista_total_1.clear()
        Lista_total_1.append(Wtmp1)
        Lista_total_1.append(Wtmp2)
        Lista_total_1.append(Wtmp3)
        Lista_total_1.append(Wtmp4)
        Lista_total_1.append(Wtmp5)

    
    for i in range(5):
        GraficaSortings(tamanhos_1, media_1[i], var_1[i])
        plt.plot(tamanhos_1, media_1[i], label = nomes_1[i], color = cores_1[i])

    plt.xlabel("Quantidade de elementos")
    plt.ylabel("Tempo (s)")
    plt.yscale('log')
    plt.title("Experimento 1")
    plt.legend()
    plt.savefig("Experimento1")
    plt.clf()

    Lista_total_1.clear()
    

    #Experimento 2
    media_2 = [[0 for j in range(5)] for i in range(3)]
    var_2 = [[0 for j in range(5)] for i in range(3)]

    funcs_2 = [tim, bubble, insertion]
    pontos_2 = [1, 3, 5, 10, 50]
    nomes_2 = ["TimSort", "BubbleSort", "InsertionSort"]
    cores_2 = ["#069AF3", "#FF7F50", "#15B01A"]

    U1 = [(randint(0, 9999)) for i in range(100000)]; U1.sort(); Utmp1 = list(U1)
    U2 = [(randint(0, 9999)) for i in range(100000)]; U2.sort(); Utmp2 = list(U2)
    U3 = [(randint(0, 9999)) for i in range(100000)]; U3.sort(); Utmp3 = list(U3)
    U4 = [(randint(0, 9999)) for i in range(100000)]; U4.sort(); Utmp4 = list(U4)
    U5 = [(randint(0, 9999)) for i in range(100000)]; U5.sort(); Utmp5 = list(U5)

    Lista_total_2 = []
    Lista_total_2.append(Utmp1)
    Lista_total_2.append(Utmp2)
    Lista_total_2.append(Utmp3)
    Lista_total_2.append(Utmp4)
    Lista_total_2.append(Utmp5)

    for i in range(3):
        for j in range(5):
            media_2[i][j], var_2[i][j] = timeMe(funcs_2[i], Lista_total_2[j], 100000, 5, pontos_2[j])

        Lista_total_2.append(Utmp1)
        Lista_total_2.append(Utmp2)
        Lista_total_2.append(Utmp3)
        Lista_total_2.append(Utmp4)
        Lista_total_2.append(Utmp5)

    for i in range(3):
        GraficaSortings(pontos_2, media_2[i], var_2[i])
        plt.plot(pontos_2, media_2[i], label = nomes_2[i], color = cores_2[i])

    plt.xlabel('Nivel de desordenação (%)')
    plt.ylabel('Tempo (s)')
    plt.yscale('log')
    plt.title('Experimento 2')
    plt.legend()
    plt.savefig("Experimento2")

    return(0)

main()