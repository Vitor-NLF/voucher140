n = int(input("Digite o numero de avaliações: "))
i = 0
soma = 0
while i < n:
    soma += int(input("Digite a nota: "))
    i += 1
media = soma/n
print(media)