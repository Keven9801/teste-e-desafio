while True:
    numero = int(input("informe um numero: "))

    if numero == 10:
        break

    print(numero)


for numero in range (100):

    if numero == 10:
        break

    print(numero, end=" " )


for numero in range (100):

    if numero %2 == 0:
        continue

    print(numero, end=" ")

#observação if numero %2 ==0: (é usado para selecionar numeros impares ou pares)
    


    numero = int(input("informe um numero: "))

    if numero == 10:
        break

    if numero %2 == 0:
        continue


    print(numero)