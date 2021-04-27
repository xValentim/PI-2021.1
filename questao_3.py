'''
Quantos caminhões?
Uma empresa de transporte recebe os produtos em sequência e os coloca em caminhões. 
A empresa possui uma política de nunca colocar mais do que 2 toneladas (2.000 kg) em cada caminhão. 
Portanto, se o novo produto for fazer o caminhão ultrapassar o peso máximo, o caminhão é despachado e o 
produto entra no próximo caminhão.

Faça uma função que recebe uma lista de pesos de produtos (em kg) e devolve a quantidade de caminhões 
necessários para enviar todos os produtos.

Exemplos:

Para a entrada
[1000, 500, 400, 200, 50, 450, 1300, 500, 1500]
sua função deve devolver o número 4 (as cores indicam os caminhões).
Para a entrada
[1900, 700]
sua função deve devolver o número 2 (as cores indicam os caminhões).
O nome da sua função deve ser quantos_caminhoes

'''

lista0 = [1000, 500, 400, 200, 50, 450, 1300, 500, 1500] # 3
lista1 = [1900, 700] # 2
lista2 = [1900, 700, 1900, 500, 1000] # 4
lista3 = [1900, 700, 1900, 500, 1500] # 4
lista4 = [1900, 700, 1900, 500, 1800] # 5
lista5 = [1900, 700, 1900, 500, 2000] # 5
lista6 = [100, 1900, 100, 100, 1800, 1, 1, 1] # 3

def quantos_caminhoes(lista):
    caminhoes = 0
    soma = 0
    i = 0
    while i < len(lista):
        soma += lista[i]
        if soma == 2000:
            caminhoes += 1
            soma = 0
        elif soma > 2000:
            caminhoes += 1
            soma = lista[i]
        if i == len(lista) - 1 and soma > 0:
            caminhoes += 1
        i += 1
    return caminhoes

# Testes
print(quantos_caminhoes(lista0))
print(quantos_caminhoes(lista1))
print(quantos_caminhoes(lista2))
print(quantos_caminhoes(lista3))
print(quantos_caminhoes(lista4))
print(quantos_caminhoes(lista5))
print(quantos_caminhoes(lista6))
