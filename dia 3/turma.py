turma = [
    {'nome': 'Nickolas', 'nota': 8.5},
    {'nome': 'Ana', 'nota': 6.0},
    {'nome': 'Carlos', 'nota': 7.5},
    {'nome': 'Beatriz', 'nota':4.5},
]

for aluno in turma:
    print(aluno['nome'], '-', aluno['nota'])

def situacao(nota):
    if nota >= 7.0:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
for aluno in turma:
    resultado = situacao(aluno['nota'])
    print(aluno['nome'], '-', aluno['nota'], '-', resultado)
    
def media_turma(turma):
    total = 0
    for aluno in turma:
        total += aluno['nota']
    return total / len(turma)
print('Média da turma:', media_turma(turma))

def salvar_turma(turma, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for aluno in turma:
            arquivo.write(f'{aluno["nome"]} - {aluno["nota"]} - {situacao(aluno["nota"])}\n')
salvar_turma(turma, 'turma.txt')
print("Turma salva no arquivo 'turma.txt!'")
      