def calculotempo(horas,valor):
    calculotempo = horas * valor
    return calculotempo


tempo = input("HORAS OU MINUTOS (DIGITE COM LETRA MAIUSCULA): ")
if tempo == "HORAS":
    tempo = float(input("Digite a quantidade de horas: "))
    if tempo == 1:
        result = calculotempo(tempo,9)
        print(result)
    elif tempo > 1:
        tempo = tempo - 1
        result2 = calculotempo(tempo,1.50) 
        tempofinal = result2 + 9
        print(tempofinal)

if tempo == "MINUTOS":
    tempo = float(input("Digite a quantidade de minutos: "))
    if tempo < 15:
        print("NÃO FOI COBRADO NADA!")
    elif tempo >= 15:
        print("O valor a ser cobrado é: ",9)