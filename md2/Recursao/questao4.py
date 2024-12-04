
numero = int(input("Informe um número inteiro positivo: "))


def calcular_soma(n):
    if n == 0:  
        return 0
    return n + calcular_soma(n - 1) 


if numero <= 0:
    print("Deve-se digitar um número inteiro positivo.")
else:
    print(f"A soma dos números de 1 até {numero} é {calcular_soma(numero)}")