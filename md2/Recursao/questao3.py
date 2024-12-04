
numero = int(input("Informe um número natural: "))


def imprimir_numeros(n):
    if n > numero:  
        return
    print(n)  
    imprimir_numeros(n + 1) 


if numero < 1:
    print("Deve-se digitar um número natural (maior ou igual a 1).")
else:
    imprimir_numeros(1)