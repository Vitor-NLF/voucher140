avaliacoes = int(input("Digite a quantidade de avaliações: "))
soma_notas = 0
for item in range(avaliacoes):
    notas = float(input("Digite a nota: "))
    soma_notas = soma_notas + notas
print("Suas notas somadas é: ",soma_notas)
mediafinal = soma_notas / avaliacoes
print("A sua média final fica: ",mediafinal)