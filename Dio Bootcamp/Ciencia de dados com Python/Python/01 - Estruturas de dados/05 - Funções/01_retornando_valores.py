def calcular_total(numeros):
    return sum(numeros)
    
def retornar_antecesor_e_sucessor(numero):
    antecesor = numero - 1
    sucessor = numero + 1
    
    return antecesor, sucessor

print(calcular_total([10, 20, 30, 40, 50]))
print(retornar_antecesor_e_sucessor(10))