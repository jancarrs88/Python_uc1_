vetor = [10, 20, 30, 40, 50]
print(f"Dados do vetor: {vetor}")

print(f"Dados da 4a posição: {vetor[3]}")


for i in range(5):
    print(f"{i}")
    print(f"{vetor[i]}")
    print(f"O valor da {i+1}a posiçao é {vetor[i]}")


    indice = 1
    for elemento in vetor:
        print(f"O valor do indice {indice} é {elemento}")
        indice += 1


import random
numero = random.randint(1,190)
print(f"{numero}")

numeros = []
for i in range (20):
    numeros.append(random.randint(1, 190))
print(f"{numeros}")



soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
qt_elementos = len(numeros)

media = soma/qt_elementos

print(f"A soma dos elementos é: {soma}")
print(f"O maior é: {maior}")
print(f"O menor é: {menor}")
print(f"A qt_elementos é: {qt_elementos}")
print(f"O valor da media é: {media}")




import random
qt_elementos = random.randint(1,151)
print(f"{qt_elementos}")

numeros = []
for i in range(qt_elementos):
  numeros.append(random.randint(1,999))
print(f"{numeros}")

par =[]
impar = []

for valor in numeros :
  if valor % 2 == 0:
    par.append(valor)
  else:
    impar.append(valor)
print(f"Numeros pares : \n\t {par} \n")
print(f"Numeros impares : \n\t {impar} \n")

print(f"Qt numeros pares : {len(par):4} \n")
print(f"Qt numeros impares : {len(impar):4} \n")



produtos = (
    ("Arroz", 5.99),
    ("Feijão", 7.49),
    ("Leite", 4.89),
    ("Óleo", 9.99),
    ("Açúcar", 3.29)
)

print("LISTA DE PRODUTOS")
for nome, preco in produtos:
    print(f"{nome:.<20} R$ {preco:6.2f}")



