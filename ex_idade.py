maior_idade = 18
idade_especial = 17

idade = int(input("informe sua idade: "))

if idade >= 18:
    print("maior idade, cnh liberada ")

if idade < maior_idade:
    print("ainda naopode tirar cnh")



if idade >= 18:
    print("maior idade, cnh liberada ")
else:
    print("idade naopermitida para tirar cnh")



if idade >= 18:
    print("maior idade, cnh liberada ")
elif idade ==idade_especial:
    print("pode fazer as aulas teoricas")
else:
    print("idade naopermitida para tirar cnh")