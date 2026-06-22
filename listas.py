notas = []

continuar = 'S'
while continuar == 'S':
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
    continuar = input('Adicionar mais? (S/N) ') .upper()
    
print('Notas registradas:', notas)
print('Total de notas:', len(notas))
print('Maior nota:', max(notas))
print('Menor nota:', min(notas))
print('Média:', sum(notas) / len(notas))

notas.sort()
print('Mediana:', notas[len(notas) // 2])
