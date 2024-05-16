
def menu():
    menu = (''' 
    --------------------------

    Seja bem-vindo(a)

     O que você deseja fazer?

    [nu] Criar usuário
    [nc] Criar conta
    [lc]\t Listar contas
            
    --------------------------

    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [0]\t Sair

     --------------------------
    ''')
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\n Depósito: R${valor:.2f}\n"
        print("\n -> Depósito realizado com sucesso!")
        
    else:
        print("Operação falhou!")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_saques):
    excedeu_saldo = saldo < valor
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= limite_saques
         
    if excedeu_saldo:
        print("\n -> Operação falhou! Saldo insuficiente.")

    elif excedeu_limite:
        print("\n -> Operação falhou! Excedeu o valor limite do saque.")

    elif excedeu_saques:
        print("\n -> Operação falhou! Excedeu o número de saques.")
       
    elif valor > 0:
        saldo -= valor
        extrato += f"\n Saque: R${valor:.2f}\n"
        numero_de_saques += 1
        print("\n -> Saque realizado com êxito!")

    else:
        print("\n Operação falhou! Valor inserido inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n ==============Extrato==============")
    print("\n Não foram realizadas movimentações. \n " if not extrato else extrato)
    print(f"\n -> Saldo: R${saldo:.2f} \n ")
    print("\n ====================================")

def criar_usuario(usuarios):
    cpf = input("\n\t -> Insira seu CPF: ")
    usuario =  filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n\t Já existe um usuário com esse CPF!")
        return
    
    nome = input("\n -> Insira seu nome: ")
    data_de_nascimento = input("\n\t -> Insira sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("\n\t -> Insira seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\n\t -> Insira seu CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n\t Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n\t Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha =  f'''\
            Agência:\t {conta['agencia']}
            C/C:\t {conta['numero_conta']}
            Titular:\t {conta['usuario']['nome']}
        '''
        print(linha)

def main():
    saldo = 0
    extrato = ""
    numero_de_saques = 0
    limite = 500
    LIMITE_SAQUE = 3 
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

    #Depósito
        if opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "d":
            valor = float(input("\n Insira o valor que deseja depositar: \n "))
            saldo, extrato = depositar(saldo, valor, extrato)

    #Saque
        elif opcao == "s":
            valor = float(input("\n Insira o valor que você deseja sacar: \n "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_de_saques=numero_de_saques,
                limite_saques=LIMITE_SAQUE,
                )

    #Extrato
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato) 
    
        else: 
            break
        
main()
    