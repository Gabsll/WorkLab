valores = input().split(' ')
lado_A = float(valores[0])
lado_B = float(valores[1])
lado_C = float(valores[2])

pi = 3.14159

triângulo_retângulo = lado_A * lado_C/2
area_do_círculo = (pi * lado_C ** 2)
area_do_trapézio = ((lado_A + lado_B) * lado_C)/2
area_do_quadrado = lado_B ** 2
area_do_retângulo = lado_A * lado_B

print(f"TRIANGULO: {triângulo_retângulo:.3f}")
print(f"CIRCULO: {area_do_círculo:.3f}")
print(f"TRAPEZIO: {area_do_trapézio:.3f}")
print(f"QUADRADO: {area_do_quadrado:.3f}")
print(f"RETANGULO: {area_do_retângulo:.3f}")