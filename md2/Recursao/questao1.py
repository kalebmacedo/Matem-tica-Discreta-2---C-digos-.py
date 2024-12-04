
numero = int(input("Informe um número inteiro não negativo: "))


def calcular_fatorial(n):
    if n == 0 or n == 1: 
        return 1
    return n * calcular_fatorial(n - 1) 


if numero < 0:
   
    print("Fatorial não tem para números negativos.\n")
else:
    
    print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")