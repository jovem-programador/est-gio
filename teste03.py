"""
    Data: 09/09/2024
    Autor: Anderson Marley
    Teste 03 - Analise código

    int INDICE = 12, SOMA = 0, K = 1;
     
    enquanto K < INDICE 
        faça { K = K + 1; SOMA = SOMA + K; } 
        imprimir(SOMA); 
"""
indice = 12
soma = 0
k = 1

while k < indice:
    k += 1
    soma += k
    print(soma)