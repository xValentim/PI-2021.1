'''Calcula estado do aluno
Chegamos ao meio do semestre, os professores precisam de um Sistema para calcular aprovação ou
reprovação dos alunos. A fim de auxiliar os professores, faça uma função, chamada calcula_estado.
Essa função recebe uma lista como parâmetro, sendo que cada elemento da lista é um registro de aluno
e suas notas, por exemplo:

Parâmetro de entrada:

[
    ['Maria', [5.0, 10.0, 0.0, 10.0, 10.0], [6.7, 8.0]],
    ['Joao', [0.0, 10.0, 10.0, 10.0, 0.0], [6.7, 2.0]],
    ['Joana', [10.0, 0.0, 10.0, 0.0, 10.0], [6.7, 8.0]]
]
No formato: [ [Nome do aluno, [notas dos quizzes], [AI, AF]] ]

Saída esperada:

[
    ['Maria', 'A'],
    ['Joao', 'R'],
    ['Joana', 'A']
]
Onde: A é aprovado e R é reprovado. Lembre-se que as notas são definidas por:

Quizzes: 10% (média dos quizzes descartada a pior nota)
AI: 40%
AF: 50%
Aprovação (A) é dada se, e somente se, a média for maior ou igual a 5. Caso contrário é reprovado (R).

O nome da sua função deve ser calcula_estado'''

lista = [
    ['Maria', [5.0, 10.0, 0.0, 10.0, 10.0], [6.7, 8.0]],
    ['Joao', [0.0, 10.0, 10.0, 10.0, 0.0], [6.7, 2.0]],
    ['Joana', [10.0, 0.0, 10.0, 0.0, 10.0], [6.7, 8.0]]
]


def soma(lista):
    soma_v = 0
    for valor in lista:
        soma_v += valor
    return soma_v

def media(lista):
    return soma(lista) / len(lista)

def minimo(lista):
    referencia = lista[0]
    for elemento in lista:
        if elemento < referencia:
            referencia = elemento
    minimo = referencia
    return minimo

def calcula_estado(lista):
    aux = []
    for aluno in lista:
        nome = aluno[0]
        notas_quizzes = aluno[1]
        notas_AI_AF = aluno[2]
        AI = notas_AI_AF[0]
        AF = notas_AI_AF[1]
        menor_nota_quizz = minimo(notas_quizzes)
        notas_quizzes.remove(menor_nota_quizz)
        media_quizzes = media(notas_quizzes)
        media_final = 0.1 * media_quizzes + 0.4 * AI + 0.5 * AF
        if media_final < 5:
            estado = 'R'
        else:
            estado = 'A'
        aux.append([nome, estado])
    return aux

'''
def soma(lista):
    soma_v = 0
    for valor in lista:
        soma_v += valor
    return soma_v

def media(lista):
    return soma(lista) / len(lista)

def calcula_estado(lista):
    for aluno in lista:
        nome = aluno[0]
        notas_quizzes = aluno[1]
        notas_AI_AF = aluno[2]
        AI = notas_AI_AF[0]
        AF = notas_AI_AF[1]
        menor_nota_quizz = min(notas_quizzes)
        notas_quizzes.remove(menor_nota_quizz)
        media_quizzes = media(notas_quizzes)
        media_final = 0.1 * media_quizzes + 0.4 * AI + 0.5 * AF
        aluno.remove(aluno[2])
        aluno.remove(aluno[1])
        if media_final < 5:
            aluno.append('R')
        else:
            aluno.append('A')    
    return lista'''

'''def calcula_estado(lista):
    for aluno in lista:
        # Precisa descarta a menor nota
        aluno[1].remove(min(aluno[1]))
        # Toma a media dos quizzes
        nota_quizz = (sum(aluno[1]) / len(aluno[1]))
        nota_AI = aluno[2][0]
        nota_AF = aluno[2][1]
        # Media ponderada de todas as notas
        nota_final = nota_quizz * 0.1 + nota_AI * 0.4 + nota_AF * 0.5
        if nota_final >= 5:
            aluno[1] = 'A'
        else:
            aluno[1] = 'R'
        aluno.remove(aluno[2])
    return lista'''

# Teste
print(calcula_estado(lista))