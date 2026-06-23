def verificar_aprovacao(nota, nota_corte=7.0):
        if nota >= nota_corte:
            print('Aprovado')
        else:
            print('Reprovado')

continuar = 'S'
while continuar == 'S':  
    nota = float(input('Digite a nota: '))
    resposta = input('Digite a nota de corte (Enter para usar o valor padrão de 7.0): ')

    if resposta =='':
        verificar_aprovacao(nota)
    else:
        verificar_aprovacao(nota, float(resposta))

    continuar = input('Deseja continuar? (S/N) ') .upper()
    
print('Programa encerrado.')


