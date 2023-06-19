n = int(input("Ingrese un número: "))

suma = 0
contador = 1
cantidad_impares = 0

while contador <= n:
    if contador % 2 != 0:
        suma += contador
        cantidad_impares += 1
    contador += 1

print("La suma de los números impares desde 1 hasta", n, "es:", suma)
print("Cantidad de números impares:", cantidad_impares)