#contador = 0
#while(contador <= 80):
#    print( f"8 x 0:{contador}")


#x = 0
#soma = 0
#while(x <= 10):
#    soma = soma + x
 #   x = x + 1

 #   print(soma)

#numeros = [45,8,29,27,22,39]
#position = 3
#print(numeros[position])

numeros = [2,3,4,11,5,8,9,7,1]
i = 0
#Parando/encerrando o loop, se 11 for encontrado
while i < len(numeros):
    print("Valor do contador: ", i," Item da lista: ",numeros[i])
    if numeros[i] == 11:
        print('Encontramos o número 11!')
        break 
    else:
        i = i + 1

