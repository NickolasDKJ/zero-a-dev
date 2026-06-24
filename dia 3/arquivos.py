# Escrevendo num arquivo
arquivo = open('notas.txt', 'w')
arquivo.write('Nickolas - 8.5\n')
arquivo.write('Ana - 6.0\n')
arquivo.write('Carlos - 7.5\n')
arquivo.close()

print('Arquivo Salvo!')

# Lendo o arquivo
arquivo = open('notas.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

# Jeito mais seguro - with
with open('notas.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)
