aluno = {
    'nome': 'Nickolas',
    'nota': 8.5,
    'cidade': 'Mogi das Cruzes',    
}
print(aluno)
print(aluno['nome'])
print(aluno['nota'])

# Adicionado uma chave nova
aluno['email'] = 'nickolas@email.com'
print(aluno)

# Atualizando um valor existente
aluno['nota'] = 9.0
print(aluno['nota'])

# Removendo uma chave
del aluno['cidade']
print(aluno)
