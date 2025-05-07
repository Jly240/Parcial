# Inicializamos la suma en 0
suma_pares_positivos = 0

# Repetimos 5 veces para leer 5 números
for i in range(5):
    numero = int(input("Ingrese un número: "))
    if numero > 0 and numero % 2 == 0:
        suma_pares_positivos += numero

# Mostramos el resultado
print(f"La suma de los pares positivos es: {suma_pares_positivos}")
