
print(f"Informe as dimensões: Lado A Lado B Lado c")

valores = input().split(' ')
lado_A = float(valores[0])
lado_B = float(valores[1])
lado_C = float(valores[2])

print(f"Lado a: {lado_A}")
print(f"Lado b: {lado_B}")
print(f"Lado c: {lado_C}")
print(" ")

pi = 3.14159

triângulo_retângulo = lado_A * lado_C/2
area_do_círculo = (pi * lado_C ** 2)
area_do_trapézio = ((lado_A + lado_B) * lado_C)/2
area_do_quadrado = lado_B ** 2
area_do_retângulo = lado_A * lado_B

print(f"AREA DO TRIANGULO: {triângulo_retângulo: .3f}")
print(f"AREA DO CIRCULO: {area_do_círculo: .3f}")
print(f"AREA DO TRAPEZIO: {area_do_trapézio: .3f}")
print(f"AREA DO QUADRADO: {area_do_quadrado: .3f}")
print(f"AREA DO RETANGULO: {area_do_retângulo: .3f}")
