def desposito():
    desposito = float(input("valor a ser depositado: R$"))
    LIMIT_DIARIO_DE_DEPOSITO = 1000
    
    if float(desposito) >= LIMIT_DIARIO_DE_DEPOSITO:
        print(f"Deposito negado: R${desposito} acima do limite diario de deposito")
        print(f"Limiti Diario: R${LIMIT_DIARIO_DE_DEPOSITO}")
    else:
        print(f"Valor depositado: R${desposito}")

def sacar(valor):
    valor = float(input("Isira o valor do saque: R$"))
    saldo = 101
    if saldo >= valor:
        saldo -= valor
        print("valor sacado!")
        print(f"Saldo disponivel: R${saldo}")
  
        
        
desposito()
sacar(100)