"""
    Data: 09/09/2024
    Autor: Anderson Marley
    Teste 02 - String
"""
from time import sleep

def quantidade(a):
    if a == 1:
        return 'vez'
    else:
        return 'vezes'

def espera(t):
    sleep(t)

def manipulacao():
    txt = str(input('Digite a palavra: '))

    maiusculo = txt.count('A')
    minuscula = txt.count('a')

    print('Analisando a frase...')
    espera(1)

    if maiusculo > 0:
        print(f'No texto digitado "{txt}", contem a letra Maiúscula "A": {maiusculo} {quantidade(maiusculo)}!')

    else:
        print(f'No texto digitado "{txt}", não contem a letra Maiúscula "A".')

    espera(3)

    if minuscula > 0:
        print(f'No texto digitado "{txt}", contem a letra Minúscula "a": {minuscula} {quantidade(minuscula)}!')
    else:
        print(f'No texto digitado "{txt}", contem a letra Minúscula "a".')

manipulacao()