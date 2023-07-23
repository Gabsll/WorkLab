linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens)
print(linguagens.sort())
print(linguagens)

print()

linguagens_1 = ["python", "js", "c"]
print(linguagens_1)
linguagens_1.sort(reverse=True)
print(linguagens_1)

print()

linguagens_2 = ["python", "js", "c"]
print(linguagens_2)
print(linguagens_2.sort(key=lambda x: len(x)))
print(linguagens_2)

print()

linguagens_3 = ["python", "js", "c"]
print(linguagens_3)
print(linguagens_3.sort(key=lambda x: len(x), reverse=True))
print(linguagens_3)