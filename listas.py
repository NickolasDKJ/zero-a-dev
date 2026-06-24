notas = []

continuar = 'S'
while continuar == 'S':
    try:
        nota = float(input('Digite uma nota: '))
        if nota < 0 or nota > 10:
            print('Nota inválida! Digite entre 0 e 10.')
        else:
            notas.append(nota)
    except ValueError:
        print('Digite apenas números!')
    continuar = input('Deseja continuar? (S/N): ').upper()
    
print('Notas registradas:', notas)
print('Total de notas:', len(notas))
print('Maior nota:', max(notas))
print('Menor nota:', min(notas))
print('Média:', sum(notas) / len(notas))

notas.sort()
print('Mediana:', notas[len(notas) // 2])
