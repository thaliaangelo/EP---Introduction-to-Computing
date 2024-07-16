void selection(int *V, int n){
    /**
    *Ordena uma lista, comparando um elementos com todos, o que a cada comparação
    *completa o menor elemento estará próximo ao começo da lista.
    *Entradas: Uma lista desordenada e sua quantidade de elementos.
    *Saída: Vazia.
    */

    for (int i = 0; i < (n - 1); i++){
        for (int j = i + 1; j < n; j++){
            if (V[i] > V[j]){
                int sup = V[i];
                V[i] = V[j];
                V[j] = sup;
            }
        }
    }
}

void bubble(int *V, int n){
    /**
    *Ordena uma lista, comparando dois a dois elementos, o que a cada comparação
    *completa o maior elemento estará próximo ao final da lista.
    *Entradas: Uma lista desordenada e sua quantidade de elementos.
    *Saída: Vazia.
    */

    for (int i = 0; i < n; i++){
        for (int j = 0; j < (n - 1); j++){
            if (V[j] > V[j + 1]){
                int sup = V[j];
                V[j] = V[j + 1];
                V[j + 1] = sup;
            }
        }
    }
}

void insertion(int *V, int n){
    /**
    *Ordena uma lista, comparando dois a dois elementos, o que a cada dois elementos trocados
    *compara do índice atual até o índice 0, ordenando até o índice atual.
    *Entradas: Uma lista desordenada e sua quantidade de elementos.
    *Saída: Vazia.
    */

    for (int i = 0; i < (n - 1); i++){
        if (V[i] > V[i + 1]){
            int sup = V[i + 1];
            V[i + 1] = V[i];
            V[i] = sup;
            for(int t = i; t > 0; t--){
                if (V[t - 1] > V[t]){
                    int sup_menor = V[t];
                    V[t] = V[t - 1];
                    V[t - 1] = sup_menor;
                }
            }
        }
    }

}

void counting(int *V, int n){
    /**
    *Ordena uma lista, em que, a cada elemento encontrado na lista dada, incrementa
    *+1 em seu índice. Após isso, cria uma nova lista adicionando, em ordem crescente
    *a quantidade de vezes que um certo índice ocorre.
    *Entradas: Uma lista desordenada e sua quantidade de elementos.
    *Saída: Vazia.
    */

    int maior = V[0];
    for (int i = 0; i < n; i++){
        if (V[i] > maior){
            maior = V[i];
        }
    }

    int W[maior + 1];
    for (int i = 0; i < (maior + 1); i++){
        W[i] = 0;
    }

    for (int i = 0; i < n; i++){
        int x = V[i];
        W[x]++;
    }

    int t = 0;
    for (int i = 0; i < (maior + 1); i++){
        for (int j = W[i]; j > 0; j--){
            V[t] = i;
            t++;
        }
    }

}
