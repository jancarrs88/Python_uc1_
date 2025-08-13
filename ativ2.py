""""
def saudacao():
   print("\n\n\tOlá, mundo!\n")


def soma(a,b):
  return a+b
resultado = soma(5, 7)
print(f"A soma é: {resultado}")



  


def somar_numeros_v3():
   num1 = float(input("Digite o primeiro número: "))
   num2 = float(input("Digite o segundo número: "))
   soma = num1 + num2
   print(f"A soma é: {soma}")

"""

def soma(a, b):
   return a + b

def subtracao(a, b):
   return a - b

def main():
   resultado_soma = soma(5, 5)
   resultado_subtracao = subtracao(25, 5)
   print(f"Soma: >>{resultado_soma}<<")
   print(f"Subtração: >>{resultado_subtracao}<<")


if __name__ == "__main__":
   main()