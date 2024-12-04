termos = int(input("Informe o número de termos da sequência de Fibonacci: "))

def calcular_fibonacci(n):
    if n == 1 or n == 2:  
        return 1
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)  

print(f"Sequência de Fibonacci até o {termos}º termo:")
for i in range(1, termos + 1):  
    print(calcular_fibonacci(i), end=" ")  
print("")  