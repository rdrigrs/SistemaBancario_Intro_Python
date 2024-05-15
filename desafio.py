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
        valor = float(input("Quanto quer depositar? "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor Inválido!")

    elif opcao == "s":
        valor = float(input("Quanto quer sacar? "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!\n")
        elif excedeu_limite:
            print("O valor excede o limite de saques!\n")
        elif excedeu_saques:
            print("Quantidade de saques atingida, consulte sua agência.")
        elif valor>0:
            saldo -= valor
            numero_saques += 1
            limite -= valor
            extrato += f"Saque no valor de R$ {valor:.2f}\n"
        else:
            print("Valor Inválido!")

    elif opcao == "e":
        print("\n==================== EXTRATO ====================")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("===================================================\ne")
    elif opcao == "q":
        break
    else:
        print("Operação Inválida!\n")
