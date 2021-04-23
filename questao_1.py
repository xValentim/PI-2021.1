'''Valida data
Faça uma função que recebe três números representando, nessa ordem, um dia, um mês e um ano e 
devolve True se a data for válida ou False, caso contrário. Na validação, você deve considerar a 
quantidade de meses e de dias no mês. Lembre-se de que alguns meses têm 30 enquanto outros possuem 31 dias. 
Também é importante levar em conta os casos de fevereiro e anos bissextos!

Anos bissextos
Existem algumas regras para definir se um ano é bissexto (ou seja, possui o dia 29 de fevereiro):

Se o ano não for múltiplo de 4, ele não é bissexto;
Se o ano for múltiplo de 4 e de 400, ele é bissexto;
Se o ano for múltiplo de 4 e de 100, mas não de 400, ele não é bissexto;
Caso contrário, ele é bissexto.
Um exemplo de data válida seria a chamada: valida_data(1, 1, 2021)

Enquanto exemplos de datas inválidas seriam: valida_data(30, 2, 2020), 
valida_data(31, 4, 2020) ou valida_data(32, 13, 2020).

Você pode assumir que não serão testados valores negativos.

O nome da sua função deve ser valida_data'''




















def eh_bissexto(a):
    if a % 4 == 0 and not(a % 100 == 0):
        return True
    elif a % 400 == 0:
        return True
    else:
        return False

def valida_data(dia, mes, ano):
    if mes > 12:
        return False
    if dia > 31:
        return False

    meses_normais = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    meses_bissextos = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if eh_bissexto(ano):
        if dia > meses_bissextos[mes - 1]:
            return False
    else:
        if dia > meses_normais[mes - 1]:
            return False
    return True
        