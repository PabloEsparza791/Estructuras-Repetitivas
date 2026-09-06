def piramide(n):
    #"for" recorre desde 1 hasta "n". Cada valor de "i" representa una fila
    for i in range(1, n +1):
        #Calculamos los espacios entre cada asterisco (*)
        espacio = " " * (n - i)
        #Calculamos cuantos asteriscos tendra cada fila
        asteriscos = "*" * (2 * i - 1)

        #Se imprime la fila, se juntan los espacios y asteriscos
        print(espacio + asteriscos)

n = int(input("Inggresa la altura (número de filas) de la piramide: "))

#Ejecuta la funcion utilizando el numero "n" ingresado por el usuario
piramide(n)
