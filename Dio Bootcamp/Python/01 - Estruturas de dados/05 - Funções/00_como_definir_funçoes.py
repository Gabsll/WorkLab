def exibir_mensagem():
    print("Hello World!")
    
def  exbir_mensagem_2(nome):
    print(f"Seja bem vindo  {nome}!")
    
def exbir_mensagem_3(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exbir_mensagem_2(nome= "Gabriel")
exbir_mensagem_3()
exbir_mensagem_3(nome= "chappie")