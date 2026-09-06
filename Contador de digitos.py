def contador_digitos(numero):
    contador = 0
    
    if numero == 0:
        return 1
    
    while numero > 0:
        numero = numero // 10
        contador += 1
    return contador

numero = int(input("Ingresa un número entero: "))

print(f"El Número {numero} tiene {contador_digitos(numero)} digitos.")
