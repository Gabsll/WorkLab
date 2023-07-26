contatos = {
    "Gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3232-3232"},
    "Fernando@gmail.com": {"nome": "Fernando", "telefone": "2212-1973"},
    "janeiva@gmail.com": {"nome": "Janeiva", "telefone": "3010-1980"},
    "Guilherme@gmail.com": {"nome": "Guilherme", "telefone": "9884-3989"}
}


for email in contatos:
    print(email, contatos[email]) #não muito usado, vai passar linha por linha pegando email, mas não dados, necesario indicar para pegar os dados contidos em email.
    
for email, dados in contatos.items(): #melhor forma, passa indicando os dados contidos dentro de cada dicionario em contatos.
    print(email, dados)