
num1 = int(input("Informe o número 1: "))
num2 = int(input("Informe o número 2: "))

def calcular_mdc(num1, num2):
    while num2 != 0:
        resto = num1 % num2  # Calcula o resto da divisão de num1 por num2
        num1 = num2
        num2 = resto
    return num1

# Calcula e imprime o GCD dos dois números
print(f"MDC de {num1} e {num2} é {calcular_mdc(num1, num2)}")