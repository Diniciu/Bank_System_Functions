menu = """
====================Operações====================
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] CRIAR USUÁRIO
[5] CRIAR CONTA CORRENTE
[6] LISTAR CONTAS
[0] SAIR
=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3
usuarios = []
contas_correntes = []
numero_agencia = "0001"

def depositar(saldo, valor, extrato, /):
    saldo += valor
    extrato.append(f"Depósito: R${valor:.2f}")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print("Valor do saque excede o limite!")
    elif numero_saques >= limite_saques:
        print("Limite de saques excedido!")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R${valor:.2f}")
        numero_saques += 1
    else:
        print("Valor inválido! Tente novamente.")
    return saldo, extrato

def mostrar_extrato(saldo, *, extrato):
    print("\n===============EXTRATO===============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R${saldo:.2f}")
    print("======================================")

def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere não numérico do CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário já existe!")
            return
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print("Usuário criado com sucesso!")

def criar_conta_corrente(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere não numérico do CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            numero_conta = f"{len(contas_correntes) + 1:04d} 1234 5678 9123"
            if any(conta['numero_conta'] == numero_conta for conta in contas_correntes):
                print("Número da conta já existe! Tente novamente.")
                return
            contas_correntes.append({'agencia': numero_agencia, 'numero_conta': numero_conta, 'usuario': usuario})
            print(f"Conta corrente {numero_conta} criada com sucesso!")
            return
    print("Usuário não encontrado!")

def listar_contas():
    if not contas_correntes:
        print("Nenhuma conta encontrada.")
    else:
        print("\n===============CONTAS===============")
        for conta in contas_correntes:
            usuario = conta['usuario']
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {usuario['nome']}, CPF: {usuario['cpf']}")
        print("======================================")

while True:
    opcao = input(menu)
    
    if opcao == '1':
        valor = float(input("Digite o valor do depósito: R$"))
        if valor > 0:
            saldo, extrato = depositar(saldo, valor, extrato)
        else:
            print("Valor inválido! Tente novamente.")
    
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: R$"))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
    
    elif opcao == '3':
        mostrar_extrato(saldo, extrato=extrato)
    
    elif opcao == '4':
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário (logradouro, número, bairro, cidade/sigla do estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
    
    elif opcao == '5':
        cpf = input("Digite o CPF do usuário para vincular a conta corrente: ")
        criar_conta_corrente(cpf)
    
    elif opcao == '6':
        listar_contas()
    
    elif opcao == '0':
        print("Fim do programa.")
        break
    
    else:
        print("Opção inválida! Tente novamente.")