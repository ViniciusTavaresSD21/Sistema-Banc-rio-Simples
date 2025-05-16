import time
import datetime

# CRIANDO UM SISTEMA BANCARIO

def linha_menu(tamanho_da_linha=50):
    print(f'\033[1;31m{'='*tamanho_da_linha}\033[m')


def texto_menu(texto, tamanho_da_linha=50):
    print(f'\033[1m{texto.center(tamanho_da_linha)}\033[m')


def menu_titulo(texto, tamanho_menu=50):
    linha_menu(tamanho_menu)
    texto_menu(texto, tamanho_menu)
    linha_menu(tamanho_menu)


def menu_opcoes(*opções):
    texto_menu('Selecione a operação:')
    linha_menu()

    lista_opcoes = []
    for opcao in opções:
        lista_opcoes.append(opcao)

    contador = 1
    for item in lista_opcoes:
        print(f'\033[1m[ {contador} ] - {item}\033[m')
        contador += 1


def funcao_deposito(saldo, valor, extrato):
    menu_titulo('Deposito')
    datahora_atual = datetime.datetime.now()
    datahora_formatado = datahora_atual.strftime('%H:%M do dia %d/%m/%Y')
    if valor >= 1:
        saldo += valor_do_deposito
        extrato += f'Deposito:    R$ {valor_do_deposito} ás {datahora_formatado}\n'
        print('Processando...')
        time.sleep(1)
        print('\033[1;32mDeposito realizado com sucesso.\033[m')
        time.sleep(1)
    else:
        print('\033[1;33mO valor minimo para deposito é de 1 real.\033[m')

    return saldo, extrato


def funcao_saque(*, saldo, extrato, limite_de_saques, numero_saques, limite_valor):
    menu_titulo('Saque')
    valor_do_saque = float(input('Valor do saque: '))
    datahora_atual = datetime.datetime.now()
    datahora_formatado = datahora_atual.strftime('%H:%M do dia %d/%m/%Y')
    if numero_saques < limite_de_saques:
        if valor_do_saque <= limite_valor and valor_do_saque <= saldo:
            saldo -= valor_do_saque
            extrato += f'Saque:    R$ {valor_do_saque} - {datahora_formatado}\n'
            numero_saques += 1
            print('Processando...')
            time.sleep(1)
            print('\033[1;32mSaque realizado com sucesso.\033[m')
            time.sleep(1)
            return saldo, extrato, numero_saques
        else:
            print('Processando...')
            time.sleep(1)
            print(f'\033[1;33mErro. Você excedeu o valor maximo de saque.\033[m')
            time.sleep(1)
            return saldo, extrato, numero_saques
    else:
        time.sleep(1)
        print('\033[1;33mVocê excedeu o numero de saques.\033[m')
        time.sleep(1)
        return saldo, extrato, numero_saques
    

def funcao_extrato(saldo, extrato):
    menu_titulo('Extrato')
    if extrato == '':
        time.sleep(1)
        print('\033[1;33mVocê ainda não realizou nenhuma transação.\033[m')
        time.sleep(1)
    else:
        time.sleep(1)
        print(extrato)
        print()
        print(f'Saldo:    R$ {saldo:.2f}')
        time.sleep(1)


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
        

def funcao_criar_usuario(lista_clientes):
    menu_titulo('Criando usuário')
    CPF = input('informe o CPF (somente números): ')
    usuario = filtrar_usuario(CPF, lista_clientes)

    if usuario:
        time.sleep(1)
        print('\033[1;33mJá existe um usuario com esse CPF.\033[m')
        time.sleep(1)
    else:
        nome = input('Nome: ')
        data_nascimento = input('Data de Nascimento: ')
        endereco = input('Endereço (Logradouro, nro - bairro - cidade - estado/sigla): ')
        lista_clientes.append({'nome': nome, 'data_de_nascimento': data_nascimento, 'cpf': CPF, 'endereço': endereco})
        print('Processando...')
        time.sleep(1)
        print('\033[1;32mUsuário criado com sucesso.\033[m')
        time.sleep(1)
        return lista_clientes


def criar_conta_corrente(agencia, usuarios, numero_da_conta):
    menu_titulo('Criando conta corrente')
    CPF = input('informe o CPF do usuário: ')
    usuario = filtrar_usuario(CPF, usuarios)

    if usuario:
        print('Processando...')
        time.sleep(1)
        print('\033[1;32mConta criada com sucesso\033[m')
        time.sleep(1)
        return {'agencia': agencia, 'numero_conta': numero_da_conta, 'usuario': usuario}
    else:
         print('\033[1;33mUsuario não encontrado.\033[m')


def listar_contas(contas):
    menu_titulo('Lista de Contas')
    for conta in contas:
        print(f'Agência:    {conta['agencia']}')
        print(f'Conta:      {conta['numero_conta']}')
        print(f'Titular:    {conta['usuario']['nome']}')
        linha_menu()


saldo = 0
extrato = ''
limite_de_saques = 3
numero_saques = 0
limite_valor = 500
lista_clientes = []
contas = []

agencia = '0001'

while True:
    while True:
        menu_titulo('BANCO AGRESTE', 50)
        menu_opcoes('Depositar', 'Sacar', 'Ver extrato', 'Criar usuário', 'Criar conta', 'Listar Contas')
        opcao = input('Opção: ')
        if opcao in '123456':
            break
        else:
            print('Erro. Escolha uma das 5 opções.')
    if opcao == '1':
        valor_do_deposito = float(input('Valor do deposito: '))

        saldo, extrato = funcao_deposito(saldo, valor_do_deposito, extrato)

    elif opcao == '2':
        saldo, extrato, numero_saques = funcao_saque(saldo=saldo, extrato=extrato, limite_de_saques=limite_de_saques, numero_saques=numero_saques, limite_valor=limite_valor)

    elif opcao == '3':
        funcao_extrato(saldo, extrato=extrato)

    elif opcao == '4':
        lista_clientes = funcao_criar_usuario(lista_clientes)

    elif opcao == '5':
        numero_da_conta = len(contas) + 1
        conta = criar_conta_corrente(agencia, lista_clientes, numero_da_conta)
        if conta:
            contas.append(conta)

    elif opcao == '6':
        listar_contas(contas)