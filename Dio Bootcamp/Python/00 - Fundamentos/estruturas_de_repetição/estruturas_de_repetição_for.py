a = int(input("informe um numero inteiro: "))
print(a)
a += 1
print(a)
a += 1

texto = input("Informe uma palavra: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()