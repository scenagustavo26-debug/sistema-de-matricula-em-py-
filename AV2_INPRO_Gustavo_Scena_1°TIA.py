
def calcular_mensalidade(idade, plano):
    if plano == "mensal":
        valor = 120
    elif plano == "trimestral":
        valor = 100
    else:
        valor = 85
    if idade <= 17 or idade >= 60:
        valor = valor - (valor * 10 / 100)
    return valor

alunos = []
continuar = "s"

while continuar == "s":

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    plano = input("Digite o plano (mensal, trimestral ou anual): ")

    while plano != "mensal" and plano != "trimestral" and plano != "anual":
        print("Plano invalido")
        plano = input("Digite o plano novamente: ")

    valor = calcular_mensalidade(idade, plano)
    alunos.append([nome, idade, plano, valor])

    print("Nome:", nome)
    print("Idade:", idade)
    print("Plano:", plano)
    print("Mensalidade:", valor)
    continuar = input("Deseja cadastrar outro aluno? (s/n): ")

print("ALUNOS CADASTRADOS")
soma = 0

for aluno in alunos:

    print("Nome:", aluno[0])
    print("Idade:", aluno[1])
    print("Plano:", aluno[2])
    print("Mensalidade:", aluno[3])
    soma = soma + aluno[3]

media = soma / len(alunos)
print(f"Media das mensalidades:", (media, 2))
