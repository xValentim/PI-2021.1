'''Calcula estado do aluno
Chegamos ao meio do semestre, os professores precisam de um Sistema para calcular aprovação ou reprovação dos alunos. A fim de auxiliar os professores, faça uma função, chamada calcula_estado. Essa função recebe uma lista como parâmetro, sendo que cada elemento da lista é um registro de aluno e suas notas, por exemplo:

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

def calcula_estado(lista):
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
    return lista