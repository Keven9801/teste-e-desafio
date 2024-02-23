conta_normal = False
conta_universitaria = False


saldo = 2000
saque = 2000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso ! ")
    elif saque <= (saldo + cheque_especial):
        print("sauqe sendo realizado junto com cheque especial ! ")
    else:
        print("saque nao realizado, saldo insuficiente !")

elif conta_universitaria:
    if saldo >= saque:
        print("salque realizado com sucesso")
    else:
        print("saldo insuficiente ! ")

else:
    print("sua conta nao foi reconhecida pelo nosso servidor, entre em contato com oseu gerente !")

