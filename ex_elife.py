import sys


opcao = int(input("informe umaopcao: [1] sacar \n[2] extrato \n: "))

if opcao ==1:
    valor = float(input("informe a quantia para o sauqe: "))

elif opcao ==2:
    print ("exibindo extrato... ")
else:
    sys.exit("opcao invalida")
