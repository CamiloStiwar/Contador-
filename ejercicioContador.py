listOfNumers = [-10, 50, 800, 9, 6, 23.5]
cont = 0
for element in listOfNumers:
    cont = cont + 1

print("El total de elementos en la lista es ", cont)

suma = 0
for element in listOfNumers:
    suma = suma + element

print("La suma de los elementos en la lista es ", suma)
print("El promedio de los datos es ", suma/cont)