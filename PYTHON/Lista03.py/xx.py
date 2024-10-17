# ##1##
# pessoa_bacana = {
#     "Nome": "Vitor",
#     "Idade": "17",
#     "Cidade": "Campo Grande MS",
#     "Profissão": "Desempregado",
# }
# x1 = pessoa_bacana
# print(x1)

# ##2##
# nome = pessoa_bacana['Nome']
# print("O nome: ",nome)
# idade = pessoa_bacana['Idade']
# print("A idade é: ",idade)

# ##3##
# pessoa_bacana ['Idade'] = 18
# print(x1)
# ##4##
# pessoa_bacana ['Email'] = "vitor@gamil.com"
# print(x1)


# amigos_100 = {
#     "nome":"Jorge",
#     "idade":"13",
#     "nome2":"Augusto",
#     "idade2":"17",
#     "nome3":"Pedrinho",
#     "idade3":"14",
#     "nome4":"Felipe",
#     "idade":"16"
# }
# for item in amigos_100:
#     print(amigos_100[item])

# nome = input("Digite um nome e vamos conferir se está na lista...")

# if nome == "Jorge" or "Augusto" or "Pedrinho" or "Felipe":
#     print(f"O nome digitano: {nome}. \n Está presente na lista!!!")
# else:
#     print("O nome digitado não está na lista!!!!!!")

# tradutor_english_for_Espanish = {
#     "tank you":"gracias",
#     "hello":"tola",
#     "jovem":"tico",
#     "man":"hombre",
#     "girl":"mujer",
# }
# pala = input("Digite uma palavra: ")

# if pala in tradutor_english_for_Espanish:
#     print(tradutor_english_for_Espanish[pala])
# else:
#     print("no tienes cabron")

# estoque = {
#     "têni":{"quantidade":78, "preço":250},
#     "camiseta":{"quantidade":85, "preço":180},
#     "calça":{"quantidade":52, "preço":154},
#     "boné":{"quantidade":92,"preço":120},
# }
# prod = input("Digite o produto que gostaria de conferir: ")
# if prod in estoque:
#     print(estoque[prod])
#     print("\n O produto está na loja!!!!")
# else:
#     print("O PRODUTO DIGITADO, ESTÁ CONSTANDO NO ESTOQUE!!")
