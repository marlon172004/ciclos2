numero = int(input("Ingrese un número: "))
suma = 0
contador_impares = 0

for i in range(1, numero+1, 2):
    suma += i
    contador_impares += 1

print("La suma de los números impares desde 1 hasta", numero, "es:", suma)
print("Hay", contador_impares, "números impares.")