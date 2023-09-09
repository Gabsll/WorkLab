conjunto_a ={1, 2, 3,}
conjunto_b = {4, 5, 6, 7}
conjunto_c = {1, 0}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))
print(conjunto_b.isdisjoint(conjunto_a))
print(conjunto_b.isdisjoint(conjunto_c))
print(conjunto_c.isdisjoint(conjunto_a))
print(conjunto_c.isdisjoint(conjunto_b))

