
numeros = [3, 8, 15, 22, 27, 34, 41, 50]
numeros_pares = []

for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)  

print("Lista apenas com números pares:")
print(numeros_pares)
