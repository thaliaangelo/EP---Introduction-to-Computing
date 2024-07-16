O objetivo do trabalho foi analisar como alguns algoritmos de ordenação se comportam
com distintos tamanhos de elementos. Foram utilizados os algoritmos InsertionSort,
SelectionSort, BubbleSort, CountingSort e o algoritmo nativo do Python TimSort.
O primeiro experimento realizado foi observar o que acontece com cada algoritmo ao
passo que a lista de elementos aumenta. Ou seja, cada um dos algoritmos ordenou
listas com 1000, 5000, 10000, 50000 e 100000 elementos.
O segundo experimento realizado foi observar o comportamento dos algoritmos
InsertionSort, BubbleSort e TimSort quando são dadas listas com 1%, 3%, 5%, 10% e 50%
de desordenação.
No terceiro experimento realizado, foi implementado os mesmos algoritmos que
implementamos na linguagem Python para a linguagem C, então, foram observadas
diferenças na implementação dos mesmos algoritmos em linguagens diferentes.
Porém, as funções de ordenação foram chamadas na linguagem C, mas dentro da main
do código em Python, ou seja, foram usadas as duas linguagens ao mesmo tempo.
Com o resultado obtido dos experimentos, será possível perceber se, para cada
tamanho da lista, um dado algoritmo é mais eficiente para a ordenação e, se uma
porcentagem da lista já estiver ordenada, alguns algoritmos serão mais eficientes do
que outros para ordenar o restante da lista.
