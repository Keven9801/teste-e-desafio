# texto = input("informe um texto:")

texto = ""
vogais= "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()  #adiciona uma quebra de linha


    #else esta como exemplo e nao é muito comun ser utilizado
