def fizzbuzz(n):
    #El FOR recorre los numeros desde el 1 hasta n
    for i in range(1, n + 1):
        #Verifica los multiplos de 3 y 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        #Verifica los multiplos de 3
        elif i % 3 == 0:
            print("Fizz")
        #Verifica los multiplos de 5
        elif i % 5 == 0:
            print("Buzz")
        #Si no es multiplo de 3 y 5 imprime el número
        else:
            print(i)

n = int(input("Ingresa un número: "))

#Ejecuta la función "fizzbuzz" usado el número que guardamos en "n"
fizzbuzz(n)
