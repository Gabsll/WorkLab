deposito = input("Inforeme valor de deposito: ")
saldo_em_caixa = 500
saldo_total = int(deposito) + saldo_em_caixa
print(deposito is saldo_em_caixa)
print(saldo_em_caixa is deposito)
print(saldo_total is saldo_em_caixa)
print(saldo_total is deposito)
print( saldo_total is saldo_em_caixa is deposito)

saldo_em_caixa = saldo_total

print(saldo_total)
print(saldo_total is saldo_em_caixa)
print(deposito is saldo_em_caixa)
print(saldo_em_caixa is deposito)
print(saldo_total is saldo_em_caixa)
print(saldo_total is deposito)
print( saldo_total is saldo_em_caixa is deposito)

saldo_total = saldo_em_caixa = deposito

print(saldo_total)
print(saldo_total is saldo_em_caixa)
print(deposito is saldo_em_caixa)
print(saldo_em_caixa is deposito)
print(saldo_total is saldo_em_caixa)
print(saldo_total is deposito)
print( saldo_total is saldo_em_caixa is deposito)
