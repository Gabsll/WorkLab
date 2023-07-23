nome = "Gabriel"
idade = 25
profissao = "Programador"
linguagem ="Python"

dados = {"nome": "Gabriel", "idade": 25}

print("Meu nome e {nome} e minha idade e {idade}".format(**dados))

print()

print("Olá meu nome %s. Eu tenho %d anos, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem)) 

print()

print("Olá meu nome {}. Eu tenho {} anos, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem)) 

print()

print("Olá meu nome {0}. Eu tenho {1} anos, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem)) 

print()

print("Olá meu nome {3}. Eu tenho {2} anos, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome)) 

print()

print("Olá meu nome {nome}. Eu tenho {idade} anos, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem)) 

print()

print(f"Olá meu nome {nome}. Eu tenho {idade} anos, trabalho como {profissao} e estou matriculado no curso de {linguagem}.") 

