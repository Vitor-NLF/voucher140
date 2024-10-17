nota_alunos={
    "nota1": float(input("Digita a primeria nota: ")),
    "nota2": float(input("Digite a segunda nota: ")),
    "nota3": float(input("Digite a terceina nota: ")),
    "nota4": float(input("Difgite a quarta nota: ")),
}
n1 = nota_alunos["nota1"]
n2 = nota_alunos["nota2"]
n3 = nota_alunos["nota3"]
n4 = nota_alunos["nota4"]
media = (n1 + n2 + n3 + n4) / 4
print(f"A média é : ",media)    
