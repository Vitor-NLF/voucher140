# ###ex01###
# def produto (num1, num2, num3):
#      produto = num1 * num2 * num3
#      return produto
# x = produto(12,12,12)
# print(x)

# ###ex02###
# def exponenciação (num1, num2):
#      exponenciação = num1 ** num2
#      return exponenciação
# x = exponenciação(12,2)
# print(x)


# def exponenciação (num1, num2):
#      exponenciação = num1 ** num2
#      return exponenciação

# result = exponenciação (int(input("Digite um valor: ")), int(input("Digite outro valor: ")))
# print(result)

# ##ex03###
# def quantidade (num1):
#      num1 = str(num1)
#      quantidade = len(num1)
#      return quantidade
# result1 = quantidade (1000)
# result2 = quantidade (int(input("Diite um valor: ")))
# print("A quantidade de digitos no número 1000 é: ",result1)
# print("E a quantidade de digitos no número digitado é: ",result2)

# #ex04##
# def verificar (numero):
#     if numero > 0:
#         return 'P'
#     else:
#         return 'N'
# resultado1 = verificar(45)
# resultado2 = verificar(-5)
# resultado3 = verificar(0)

# print(resultado1)
# print(resultado2)
# print(resultado3)

# def somaimposto (taxa, custo):
#     taxa = taxa/100
#     imposto = taxa * custo
#     return custo + imposto
# result = somaimposto (float(input("Digite qual a taxa:")), float(input("Qual o custo: ")))
# print(result)

# ##ex05##
# def somaimposto(taxaimposto,custo):
#     taxadecimal = taxaimposto /100
#     novocusto = (custo * taxadecimal)
#     return novocusto

# taxa = 10
# custoinicial = 325
# custofinal = somaimposto(taxa, custoinicial)

# print(f"O custo inical era: R$: {custoinicial}")
# print(f"Com uma taxa de imposto de {taxa}%, o custo final: {custofinal:.2f}")

##ex06##
# def tabeladepreco(quantidade,produto):
#     tabeladepreco = quantidade * produto
#     return tabeladepreco

# x = 0
# y = 1.99
# while x < 50:
#     x = x + 1

#     resul = tabeladepreco (x,y)
#     print(f"o produto número: {x} \nO valor é: {resul:.2f}")

##ex07##
# s = int(input("Digite a quantidade de salário por hora: "))
# h = int(input("Digite as horas trabalhadas: "))

# if h <= 40:
#     def calhoras(salario,horas):
#         calhoras = salario * horas
#         return calhoras
#     result = calhoras(s,h)
#     print(result)
# else:
#     def calhoras2(salario2,base2):
#         calhoras2 = salario2 * base2 
#         porc = result * 0.5
#         porc = porc + result
#         return calhoras2
#     reesult2 = calhoras2(s,h)
#     print(reesult2)

##ex08##
# kg = float(input("Digite o peso em kg: "))
# if kg >= 50:
#     def calculo (x,multa):
#         x = kg - 50
#         calculo = x * multa
#         return calculo
#     multa = 4
#     result = calculo(kg,multa)
#     print(calculo)

##ex09##
# def calculotempo(horas,valor):
#     calculotempo = horas * valor
#     return calculotempo


# tempo = input("HORAS OU MINUTOS (DIGITE COM LETRA MAIUSCULA): ")
# if tempo == "HORAS":
#     tempo = float(input("Digite a quantidade de horas: "))
#     if tempo == 1:
#         result = calculotempo(tempo,9)
#         print(result)
#     elif tempo > 1:
#         tempo = tempo - 1
#         result2 = calculotempo(tempo,1.50) 
#         tempofinal = result2 + 9
#         print(tempofinal)

# if tempo == "MINUTOS":
#     tempo = float(input("Digite a quantidade de minutos: "))
#     if tempo < 15:
#         print("NÃO FOI COBRADO NADA!")
#     elif tempo >= 15:
#         print("O valor a ser cobrado é: ",9)

##ex10##
# def calcular_tempo (tempo_minutos):
#     valor_minimo_por_hora = 9.00
#     valor_adicional_por_hora = 1.50

#     taxa_pis = 0.0033
#     taxa_confins = 0.0020
#     taxa_icms = 0.17

#     if tempo_minutos < 15:
#         return 0.00, 0.00, 0.00, 0.00, 0.00
    
#     horas_completas = tempo_minutos// 60
#     minutos_restantes = tempo_minutos % 60
#     if minutos_restantes > 0:
#         horas_completas +=1
#     if horas_completas == 1:
#         total = valor_minimo_por_hora
#     else:
#         total = valor_minimo_por_hora + (horas_completas - 1) * valor_adicional_por_hora

#     pis = total * taxa_pis
#     confins = total * taxa_confins
#     icms = total * taxa_icms
#     imposto_total = pis + confins + icms
#     total_com_impostos = total + imposto_total
#     return total, pis, confins, icms, imposto_total, total_com_impostos, horas_completas

# tempo_utilizado = int(input("Digite o tempo utilizados em minutos: "))
# total, pis, confins, icms, impostos_total, total_com_impostos, horas_completas = calcular_tempo(tempo_utilizado)
# print(f"TEMPO: {horas_completas:.1f} HORAS")
# print(f"PIS: R${pis:.2f}")
# print(f"CONFINS: R${confins:.2f}")
# print(f"ICMS: R${icms:.2f}")
# print(f"IMPOSTO: R${impostos_total:.2f}")
# print(f"TOTAL: R${total_com_impostos:.2f}")

##ex11##
# def imprime(lista):
#     cont = 0
#     while cont < len(lista):
#         print(f"{cont+1}- {lista[cont]}")
#         cont +=1

# listadecompra = ['mamao','castanha','mel','uva','banana','detergente','salada','cebola']
# imprime(listadecompra)

##ex12##
# def calcular_media(lista):
#     soma = 0
#     for num in lista:
#         soma += num
#     media = soma / len(lista)
#     return media

# listedenumeros = [8,9,10,11,5,3,2,6,17,20]
# x = calcular_media(listedenumeros)
# print(x)

##ex13##
# def valor(quantidade_de_elementos,valor_padrao):
#     valor = quantidade_de_elementos * valor_padrao
#     return valor
# quantidade = int(input("Digite a quantidade de elementos: "))
# valor_p_lista = input("Digite o valor padrao: ")

# x = valor(quantidade,valor_p_lista)

# lista = []
# lista.append(x)
# print(lista)

##ex14##
# def calcular_valor(consumo,preco):
#     valor = consumo * preco
#     return valor
# def calcular_consumo(potencia,horas,preco):
#     consumo = potencia * horas / 1000
#     conta = calcular_valor(consumo,preco)
#     return conta
# potencia = float(input("Digite a potencia do aparelho: "))
# tempo = float(input("Quanto tempo foi utilizado no mês: "))
# preco = float(input("Valor de KWH: "))

# banho = calcular_consumo(potencia,tempo,preco)

# print("R$: ",banho)

##ex15##
# def calcular(*args):
#     return sum(args)

# resultado = calcular(12,12)
# print(resultado)

##ex16##
# def media(*args):
#     return sum(args)/len(args) 

# i = 2
# while i > 1:
#     x = (float(input("Digite um número, ou zero para parar: "))) 
#     i = i + 1                       
#     if x == 0:
        
#         break 
# result = media(x)
# print(result)

##ex17##
# def armazem_de_dados(**kwargs):
#     dados_pessoa = kwargs

    

#     for chave, valor in dados_pessoa.items():
#         print(f"{chave} is {valor}")

# armazem_de_dados(
#     firstname = 'Vitor',
#     lastname = 'Nascimento',
#     email = 'blabla@gmail.com',
#     country = 'Brasil',
#     age = 17,
#     phone = '99992222',
# )

##ex18##