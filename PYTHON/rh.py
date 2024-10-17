cargo = input("Diigite seu cargo: ")
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
idade = float(input("Digite sua idade: "))

if(idade >= 18):
    print("PARABÉNS VOCÊ PASSOU PARA A PRÓXIMA FASE!!")
    curso = input("Você possui curso na área? ")
    if (curso == "sim"):
        print("PARABÉNS VOCÊ PASSOU PARA A PRÓXIMA FASE!!")
        nota = float(input("Digite sua nota: "))
        if (nota >= 7):
            print("PARABÉNS VOCÊ PASSOU PARA A PRÓXIMA FASE!!")
        else:
            print("REPROVOU NA ÚLTIMA FASE! ")
    else:
        print("OBRIGADO PELA PARTICIPAÇÃO!!")
else:
    print("OBRIGADO PELA PARTICIPAÇÃO!!")        