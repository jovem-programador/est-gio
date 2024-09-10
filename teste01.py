"""
    Data: 09/09/2024
    Autor: Anderson Marley
    Teste 01 - Fibonacci
"""
# Sequencia de Fibonacci
fibonacci1 = 0
fibonacci2 = 1
controle = 1

numero = int(input('Digite o número que deseja a Sequencia de Fibonacci: '))

# Array da sequencia
arr = [fibonacci1, fibonacci2]

# Estrutura de repetição
while controle < numero - 1:

    # Somando para pegar o proximo número
    proximo = fibonacci1 + fibonacci2

    # Adicionando ao Array
    arr.append(proximo)

    # Atribuindo o número fibonacci2 para fibonacci1
    fibonacci1 = fibonacci2

    # Atribuindo o proximo número a fibonacci2
    fibonacci2 = proximo

    # Exibindo a Sequencia Fibonacci
    #print(fibonacci2)

    # Var de controle
    controle += 1

print(f'Sequência de Fibonacci: {arr}')

if numero in arr:
    print(f'O número informado: {numero}, pertence a sequência de Fibonacci.')
else:
    print(f'O número informado: {numero}, não pertence a sequência de Fibonacci.')