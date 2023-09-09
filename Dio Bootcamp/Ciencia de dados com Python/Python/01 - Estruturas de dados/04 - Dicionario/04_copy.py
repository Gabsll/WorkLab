contatos = {
    "Gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3232-3232"}
}


copia = contatos.copy() # Faz uma copia dos dados armazenado.
print(contatos)
print(copia)

copia["Gabriel@gmail.com"] = {"nome": "Sousa"}

print()
print(contatos)
print(copia)