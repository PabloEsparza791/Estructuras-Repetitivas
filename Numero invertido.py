def invertir_numero(numero):
    #En la variable "invertido" guardamos poco a poco el númereo invertido
    invertido = 0

    while numero > 0:
        digito = numero % 10
        #Se va construyendo el número invertido
        invertido = invertido * 10 + digito
        numero = numero // 10

    #Cuando termina el "while" la función devuelve el número invertido
    return invertido

numero = int(input("Ingresa un Número entero: "))

print(f"Número invertido: {invertir_numero(numero)}")
