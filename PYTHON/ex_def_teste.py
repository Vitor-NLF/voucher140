s = int(input("Digite a quantidade de salário por hora: "))
h = int(input("Digite as horas trabalhadas: "))

if h <= 40:
    def calhoras(salario,horas):
        calhoras = salario * horas
        return calhoras
    result = calhoras(s,h)
    print(result)
else:
    def calhoras2(salario2,base2):
        calhoras2 = salario2 * base2 
        porc = result * 0.5
        porc = porc + result
        return calhoras2
    reesult2 = calhoras2(s,h)
    print(reesult2)