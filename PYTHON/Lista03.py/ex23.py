n = int(input("Digite um número: "))
i = n
while i <= n:
    x = n/i
    i = i - 1
    
    if x %2 == 0:
        print(f"Os resultados exatos de: {n} / {i} = {x}")
        i = i
        print(f"E a soma dos divisores são: ")
    
    if i == 0:
        break