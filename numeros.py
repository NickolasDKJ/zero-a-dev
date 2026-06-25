alunos = []

def adicionar_aluno(nome, nota):
    alunos.append({
        "nome": nome,
        "nota": nota
    })


def situacao(nota):
    if nota >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

for aluno in alunos:
        resultado = situacao(aluno["nota"])  
        print(aluno["nome"], "-", aluno["nota"], "-", resultado)     

def media_turma(alunos):
     if len(alunos) == 0:
          return "Nenhum aluno cadastrado."
     total = 0
     for aluno in alunos:
          total += aluno["nota"]
     return total / len(alunos)

def menu_adicionar():
     nome = input("Nome: ")
     nota = float(input("Nota: "))
     adicionar_aluno(nome, nota)

def menu_listar():
     if len(alunos) == 0:
          print("Nenhum aluno cadastrado.")
          return
     for aluno in alunos:
          resultado = situacao(aluno["nota"])
          print(aluno["nome"], "-", aluno["nota"], "-", resultado)

def menu_media_turma():
     print("Média da turma:", media_turma(alunos))

def menu_buscar():
     nome_procurar = input("Digite o nome do aluno: ")
     
     for aluno in alunos:
          if aluno["nome"] .strip().lower() == nome_procurar.strip().lower():
               resultado = situacao(aluno["nota"])
               print(aluno["nome"], "-", aluno["nota"], "-", resultado)
               return
     print("Aluno não encontrado.")

def menu_editar_nota():
    nome_procurado = input("Digite o nome do aluno: ")
    for aluno in alunos:
         if aluno["nome"] == nome_procurado:
              nova_nota = float(input("Digite a nova nota: "))
              aluno["nota"] = nova_nota
              print("Nota atualizada com sucesso!")
              return
    print("Aluno não encontrado. Verifique o nome digitado.")

def menu_remover():
     nome_procurado = input("Digite o nome do aluno: ")

     for aluno in alunos:
          if aluno ["nome"] == nome_procurado:
               alunos.remove(aluno)
               print("Aluno removido com sucesso!")
               return
     print("Aluno não encontrado")

opcao = ""

while opcao != "7":
     print("1 - Adicionar aluno")
     print("2 - Listar alunos")
     print("3 - Calcular média da turma")
     print("4 - Buscar aluno")
     print("5 - Editar notas")
     print("6 - Excluir aluno")
     print("7 - Sair")
     opcao = input("Escolha uma opção: ")
     if opcao == "1":
          menu_adicionar()
     elif opcao == "2":
          menu_listar()
     elif opcao == "3":
          menu_media_turma()
     elif opcao == "4":
          menu_buscar()
     elif opcao == "5":
          menu_editar_nota()
     elif opcao == "6":
          menu_remover()
     elif opcao == "7":
          print("Saindo...")