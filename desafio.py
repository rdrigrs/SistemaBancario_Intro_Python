menu = """

[d] - DEPOSITAR
[s] - SACAR
[e]- EXTRATO
[q] - SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        
    elif opcao == "s":
        #
    elif opcao == "e":
        #
    elif opcao == "q":
        break
    else:
        print("Operação Inválida!\n")
