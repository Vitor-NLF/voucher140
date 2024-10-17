lista = [5,4,3,2,1]
print(lista)

lista.append(0.1)
lista.append(0.2)
lista.append(0.3)
lista.append(0.4)
lista.append(0.5)
print(lista)

lista.pop()
lista.pop()
print(lista)
print(len(lista))

print(sorted(lista))

print(max(lista))
print(min(lista))

lista.sort(reverse = True)
print(lista)

print(sum(lista))

print(sum(lista) / len(lista))

lista.insert(0, "4")
print(lista)

lista.insert(1,"2")
print(lista)