palavra = input("Digite uma palavra: ")

vogais_encontradas = []

vogais = "aeiouAEIOU"

# Laço for para verificar cada letra
for letra in palavra:
    if letra in vogais:
        vogais_encontradas.append(letra)  

print(f"Vogais encontradas na palavra: {vogais_encontradas}")
