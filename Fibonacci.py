valor = int(input("Número de Fibonacci: "))
ultimo = 0
penultimo = 1

for i in range (valor):

    penultimo = ultimo + penultimo
    ultimo= penultimo - ultimo

print("O Fibonacci de {} -> {}" .format(valor,ultimo))
