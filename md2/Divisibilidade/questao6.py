
num1 = int(input("Informe o número 1: "))
num2 = int(input("Informe o número 2: "))


def calcular_mdc(num1, num2):
    while num2 != 0:
        resto = num1 % num2  
        num1 = num2
        num2 = resto
    return num1


def calcular_mmc(num1, num2):
    return num1 * num2 // calcular_mdc(num1, num2)  


print(f"O LCM de {num1} e {num2} é {calcular_mmc(num1, num2)}")