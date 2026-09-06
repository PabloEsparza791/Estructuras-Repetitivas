def suma_par_impar(n):
    #Creamos 2 variables que...
    suma_par = 0   #guardara la suma de los pares
    suma_impar = 0 #guardara la suma de los impares

    #El "for" recorre los números desde 1 hasta "n"
    for i in range (1, n + 1):
        #Verificamos si el número es par, si al dividir, el residuo es 0 etonces es par
        if i % 2 == 0:
            suma_par += i
        else:
            suma_impar += i

    #Resultados de cada suma
    print(f"Suma total de los números pares: {suma_par}")
    print(f"Suma total de los números impares: {suma_impar}")

#Pide "n", hasta el número que vamos a sumar
n = int(input("Ingresa un número: "))

#Ejecutamos la funcion y le pasamos el valor de "n"
suma_par_impar(n)
