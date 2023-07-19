nome = "Gabriel"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "    Opções      "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")
print(texto.center(10) + ".")


menu = " Menu de opçoes "

print("#### " + menu + " ####")
print(menu.center(26))
print(menu.center(26, "#"))
print("-M-e-n-u- -d-e- -o-p-ç-o-e-s-")
print("-".join(menu))
