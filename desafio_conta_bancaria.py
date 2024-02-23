menu = """

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("informe o valor adepositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2F}\n"
            
        else:
            print("valor informado invalido! ")

    elif opcao == "2":
        valor = float(input("informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques > limite_saques

        if excedeu_saldo:
            print("voce não tem saldo suficiente para realizar a operação !")

        elif excedeu_limite:
            print("valor desejado excede o limite de saque !")

        elif excedeu_saques:
            print("numero de saques excede valor diario !")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("operação falhou, valor invalido")

    elif opcao == "3":
        print("/n========== extrato ==========")
        print("não foram realizadas movimentações."if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "4":
        break

    else:
        print("selecione novamente a operação desejada, valor invalido")

        