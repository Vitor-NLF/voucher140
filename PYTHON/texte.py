numeros = [24,12,33,99,7,8.12,10.5,54]
##Contar alrgarismos da liista##
print(len(numeros))

##printar números da lista##
print(numeros[5])

##Somar números da lista##
print(numeros[3]+numeros[4])

##Soma de todos os números da llista##
print(sum(numeros))

##Numero maior da lista##
print(min(numeros))

##Ordenação da lista##
lista_ordenada = sorted(numeros)
print(lista_ordenada)

##indice##
indice = numeros.index(99)
print(indice)

##remoção de numeros da lista##
numeros.pop()
numeros.pop()
print(numeros)
print(len(numeros))

##Inserção de coisas na lista##
numeros.insert(0,"Vitão")
numeros.insert(21,2006)
print(numeros)

##Inserir##
numeros.append("BRASIL CAMINHONERIO")
print(numeros)


##Inserir outra lista dentro da lista##
numeros.append([1,2,3,4,5,5])
print(numeros)
print(numeros[9])


##For##
fruits = ['apple','kiwi','mango','tomato','banana','cherry']

for item in fruits:
    print(item)