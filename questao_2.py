'''Soma múltiplos
Faça uma função que recebe dois valores inteiros e retorna a soma de todos os números 
múltiplos desses valores entre 0 e 10 vezes o maior dos dois números, independente da ordem de entrada. 
Exemplos:

Entrada: soma_multiplos(2, 5) Valores a serem somados: 
0, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 35, 36, 38, 
40, 42, 44, 45, 46, 48, 50 Saída (total): 775

Entrada: soma_multiplos(7, 4) Valores a serem somados: 
0, 4, 7, 8, 12, 14, 16, 20, 21, 24, 28, 32, 35, 36, 40, 42, 44, 48, 49, 52, 
56, 60, 63, 64, 68, 70 Saída (total): 913

ATENTE que cada número é somado apenas uma vez, mesmo se for múltiplo de ambos os valores de entrada.

O nome da sua função deve ser soma_multiplos'''

def soma_multiplos(a, b):
    if a < b:
        # Swap
        '''temp = b
        b = a
        a = temp'''
        a, b = b, a
    #maior = max([a, b])
    soma = 0
    i = 0
    while i <= a * 10:
        if i % a == 0 or i % b == 0:
            soma += i
        i += 1
    return soma
    

'''def soma_multiplos(a, b):
    maior = max([a, b])
    soma = 0
    i = 0
    while i <= maior * 10:
        if i % a == 0 or i % b == 0:
            soma += i
        i += 1
    #soma = sum(set(lista))
    return soma
'''
print(soma_multiplos(2, 5))
print(soma_multiplos(7, 4))

'''
def soma_multiplos(a, b):
    maior = max([a, b])
    lista = []
    i = 0
    while i <= maior * 10:
        if i % a == 0:
            lista.append(i)
        if i % b == 0:
            lista.append(i)
        i += 1
    soma = sum(set(lista))
    return soma
'''