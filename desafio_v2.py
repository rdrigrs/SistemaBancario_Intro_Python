menu = """

[d] - DEPOSITAR
[s] - SACAR
[e]- EXTRATO
[cu] - CRIAR USUÁRIO
[co] - CRIAR CONTA
[q] - SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = list()
lista_contas = list()
cpfs_cadastrados = set()
NUM_AGENCIA = "0001"
num_conta = 0

def sacar(*, saldo, valor, extrato, limite, numero_saques):
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
    return saldo, extrato, limite, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor Inválido!")
    
    return saldo, extrato

def visualizar_historico(saldo, /, *, extrato):
    print("\n==================== EXTRATO ====================")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("===================================================\ne")
    return 0

def criar_usuario(nome="NOME", nascimento="DD-MM-AAAA", cpf="00000000000", endereco="L - N - B - C/UF"):
    if cpf in cpfs_cadastrados:
        print("CPF já cadastrado!\n")
    else:
        cpfs_cadastrados.add(cpf)
        lista_usuarios.append((nome, nascimento, cpf, endereco))
        print("Usuário cadastrado com sucesso!\n")
    return 0

def criar_conta_bancaria(cpf_usuario):
    if cpf_usuario not in cpfs_cadastrados:
        print("Usuário não cadastrado.\n;")
    else:
        num_conta+=1
        lista_contas.append((NUM_AGENCIA, num_conta, cpf_usuario))
        print("Conta criada com sucesso.\n")
    return 0



while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Quanto quer depositar? "))
        
        (saldo, extrato) = depositar(saldo, valor, extrato)

        print("Depósito realizado com sucesso.\n")
    elif opcao == "s":
        valor = float(input("Quanto quer sacar? "))
        (saldo, extrato, limite, numero_saques) = sacar(
            saldo=saldo, 
            valor=valor, 
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques
            )
        
        print("Saque realizado com sucesso.\n")
    elif opcao == "e":
        visualizar_historico(
            saldo, 
            extrato=extrato
            )
    elif opcao == "cu":
        nome = str(input("Digite o nome do usuário: "))
        nascimento =  input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF: ")
        endereco = input("Endereço Completo: ")
        criar_usuario(
            nome, 
            nascimento, 
            cpf, 
            endereco
            )
    elif opcao == "co":
        cpf = input("Digite o CPF do usuário: ")
        criar_conta_bancaria(cpf)
    elif opcao == "q":
        break
    else:
        print("Operação Inválida!\n")
