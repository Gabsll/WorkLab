nome = input()
salario = float(input())
vendas = float(input())

bonus = float(vendas * 0.15)
salario_total = salario + bonus

print(f"TOTAL = R$ {salario_total:.2f}")