valores = input().split(' ')
codigo_1 = int(valores[0])
numero_peça_1 = int(valores[1])
preco_peca_1 = float(valores[2])

valores_2 = input().split(' ')
codigo_2 = int(valores_2[0])
numero_peça_2 = int(valores_2[1])
preco_peca_2 = float(valores_2[2])

preco_total = ((numero_peça_1*preco_peca_1) + (numero_peça_2*preco_peca_2))

print(f"VALOR A PAGAR: R$ {preco_total:.2f}")