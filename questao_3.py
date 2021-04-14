'''
Quantos caminhões?
Uma empresa de transporte recebe os produtos em sequência e os coloca em caminhões. A empresa possui uma política de nunca colocar mais do que 2 toneladas (2.000 kg) em cada caminhão. Portanto, se o novo produto for fazer o caminhão ultrapassar o peso máximo, o caminhão é despachado e o produto entra no próximo caminhão.

Faça uma função que recebe uma lista de pesos de produtos (em kg) e devolve a quantidade de caminhões necessários para enviar todos os produtos.

Exemplos:

Para a entrada
[1000, 500, 400, 200, 50, 450, 1300, 500, 1450, 100]
sua função deve devolver o número 4 (as cores indicam os caminhões).
Para a entrada
[1900, 700]
sua função deve devolver o número 2 (as cores indicam os caminhões).
O nome da sua função deve ser quantos_caminhoes

'''

import math
def quantos_caminhoes(lista):
    soma = 0
    cont = 0
    for i in range(len(lista)):
        soma += lista[i]
        if soma > 2000:
            cont += 1
            soma = lista[i]
    return cont + 1