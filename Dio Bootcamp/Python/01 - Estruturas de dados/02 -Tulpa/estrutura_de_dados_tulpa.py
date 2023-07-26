#Tupla é um tipo de estrutura de dados do Python que tem como principal característica ser imutável. Ou seja, ao criar uma tupla você não consegue alterar nenhum elemento que faça parte dela. Normalmente, as tuplas são utilizadas para armazenar sequências de códigos que não serão modificadas.

frutas = ("laranja", "abacate", "limão",)
print(frutas[0])
letras = tuple("python")
print(letras[0])
numeros_1 = (1, 2, 3, 4, 5,)
print(numeros_1[2])
pais = ("Brasil",)
print(pais[0])


matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print(matriz[-2][-2])

numeros = ("p","y","t","h","o","n",)
print(numeros[0:3:])
print(numeros[1:3:])
print(numeros[2:3:])
print(numeros[3:3:])
print(numeros[1:10:1])
print(numeros[0:3:2])
print(numeros[0:10:])
print(numeros[0:10:2])
print(numeros[0:10:3])
print(numeros[0:10:4])
print(numeros[:3:])