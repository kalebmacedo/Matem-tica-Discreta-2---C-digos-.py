
tamanho = int(input("Informe o tamanho da matriz: "))

def gerar_matriz_zn(tamanho):
    matriz = []
    for x in range(tamanho):
        linha = []
        for y in range(tamanho):
            resultado = (x * y) % tamanho
            linha.append(resultado)
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    for linha in matriz:
        print(' '.join(map(str, linha)))


matriz = gerar_matriz_zn(tamanho)


exibir_matriz(matriz)