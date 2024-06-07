def dividir_numeros(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

resultado = dividir_numeros(numero1, numero2)

print(f"La división de {numero1} entre {numero2} es {resultado}")
