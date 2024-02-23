nome = "keven"
idade = 26
profissao = "motoboy"
cnh = "ab"
salario_hora = 19.967

dados = {"nome": "keven","idade": 26,"profissao":"motoboy","cnh": "ab"}
pi = 3.14159

print("ola,me chamo %s e tenho %d anos.Atualmente minha profissao é %s, possuo habilitação %s." %(nome, idade,
 profissao, cnh))

print("ola,me chamo {} e tenho {} anos.Atualmente minha profissao é {}, possuo habilitação {}.".format(nome, idade,
 profissao, cnh))


print("ola,me chamo {2} e tenho {3} anos.Atualmente minha profissao é {0}, possuo habilitação {1}." .format(profissao, cnh,
 nome, idade))


print("ola,me chamo {nome} e tenho {idade} anos. Atualmente minha profissao é {profissao},possuo habilitaçao {cnh}".format(nome=nome, idade=idade, profissao=profissao, cnh=cnh))


print("ola,me chamo {nome} e tenho {idade} anos. Atualmente minha profissao é {profissao},possuo habilitaçao {cnh}".format(**dados))


print(f"ola,me chamo {nome} e tenho {idade} anos. Atualmente minha profissao é {profissao},possuo habilitaçao {cnh}, meu salario hora é {salario_hora: .2f}.")
### atualmente a maneira maisutilizada entre os programadores por deixar o código mais limpo e manutenivel


print(f"valor de pi: {pi: .2f}")
print(f"valor de pi: {pi:9.1f}") 


### é utilizado %s para variaveis tipo strig.
### é utilizado %d para variaveis inteiras.
### é utilizado %f para variaveis float.
### pode ser utilizado {} inves de %, unica diferença é que pode misturar a ordem das strings numerando o {}