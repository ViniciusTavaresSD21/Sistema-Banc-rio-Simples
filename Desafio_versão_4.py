from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
from datetime import datetime
import time

def linha_menu(tamanho_da_linha=50):
    print(f'\033[1;31m{"="*tamanho_da_linha}\033[m')


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


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario._cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


class Cliente:
    def __init__(self, endereco):
        self._endereço = endereco
        self.contas = []


    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco)
  

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def Saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    

    def Sacar(self, valor):
            if valor <= self._saldo:
                self._saldo -= valor
                print('Processando...')
                time.sleep(1)
                print('\033[1;32mSaque realizado com sucesso.\033[m')
                time.sleep(1)
                return self._saldo
            else:
                print('Saldo insuficiente.')


    def Depositar(self, valor):
        if valor >= 1:
            self._saldo += valor
            print('Processando...')
            time.sleep(1)
            print('\033[1;32mDeposito realizado com sucesso.\033[m')
            time.sleep(1)
            return True
        else:
            print('\033[1;33mO valor minimo para deposito é de 1 real.\033[m')

        

class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        self._limite = float(limite)
        self._limite_saques = int(limite_saques)
        super().__init__(numero, cliente)

    def sacar(self, valor):
        numero_de_saques = 0
        for transacao in self._historico.transacoes:
            if transacao['tipo'] == Saque.__name__:
                numero_de_saques += 1
        
        if valor > self._limite:
            print('Você excedeu o valor maximo do saque.')
        
        elif numero_de_saques >= self._limite_saques:
            print('Você excedeu o limite de saques.')
        
        else:
            return super().Sacar(valor)

        return False


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass
          

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.Sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        Depositar_valor = conta.Depositar(self.valor)

        if Depositar_valor:
            conta.historico.adicionar_transacao(self)


def recuperar_conta(cliente):
    if cliente.contas:
        return cliente.contas[0]
    
    else:
        print('Usuário não encontrado.')


def novo_usuario(lista_de_clientes):
    menu_titulo('Novo usuário')
    Cpf = input('Digite o seu CPF: ')
    cliente = filtrar_usuario(Cpf, lista_clientes)
    if cliente:
        print('Esse CPF já está cadastrado.')
        return
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    Cadastro = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=Cpf, endereco=endereco)

    print('Processando...')
    time.sleep(1)
    print('\033[1;32mCadastro criado com sucesso.\033[m')
    time.sleep(1)
    
    lista_clientes.append(Cadastro)


def nova_conta():
    menu_titulo('Nova conta')
    while True:
        a = input('Você já tem um cadastro no banco? [S/N]: ')
        if a.lower() in 'sn':
            break
        else:
            print('Digite apenas "S" ou "N".')
    if a == 's':
        cpf_do_titular = input('informe o CPF: ')
        conta_filtrada = filtrar_usuario(cpf_do_titular, lista_clientes)
        if conta_filtrada:
            numero_da_conta = len(conta_filtrada.contas) + 1
            conta_filtrada.adicionar_conta(Conta_corrente(numero=numero_da_conta, cliente=conta_filtrada))
            print('Processando...')
            time.sleep(1)
            print('\033[1;32mConta criado com sucesso.\033[m')
            time.sleep(1)
        else:
            print('Usuario não encontrado.')
    else:
        print('Você precisa cadastrar um usuário antes de abrir a sua conta.')


def funcao_saque():
    menu_titulo('Saque')
    cpf_do_titular = input('CPF do cliente: ')
    cliente = filtrar_usuario(cpf_do_titular, lista_clientes)

    if not cliente:
        print('Usuario não encontrado.')
        return
    
    valor = float(input('Valor do Saque: '))
    transacao = Saque(valor)
     
    conta = recuperar_conta(cliente)

    if not conta:
        print('Esse usuário não possui conta.')
        return
        
    cliente.realizar_transacao(conta, transacao)


def funcao_deposito():
    menu_titulo('Deposito')
    cpf_do_titular = input('CPF do cliente: ')
    cliente = filtrar_usuario(cpf_do_titular, lista_clientes)

    if not cliente:
        print('Cliente não cadastrado.')
        return
    
    valor = float(input('Valor do deposito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta(cliente)
    if not conta:
        print('Esse usuário não possui uma conta.')
        return
    
    cliente.realizar_transacao(conta, transacao)


def funcao_extrato():
    menu_titulo('Extrato')
    cpf_do_titular = input('CPF do cliente: ')
    cliente = filtrar_usuario(cpf_do_titular, lista_clientes)

    if not cliente:
        print('Cliente não encontrado.')
        return
    
    conta = recuperar_conta(cliente)
    if not conta:
        print('Esse cliente não possui conta.')
        return
    
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.Saldo:.2f}")


lista_clientes = []

while True:
    menu_titulo('Banco Agreste')
    while True:
        menu_opcoes('Novo usuario', 'Nova Conta', 'Sacar', 'Depositar', 'Ver extrato')
        opcao_do_menu = input('Opção: ')
        if opcao_do_menu in '12345':
            break
        else:
            print('Escolha uma das cinco opções.')
            linha_menu()

    if opcao_do_menu == '1':
        novo_usuario(lista_clientes)

    elif opcao_do_menu == '2':
        nova_conta()
    
    elif opcao_do_menu == '3':
        funcao_saque()

    elif opcao_do_menu == '4':
        funcao_deposito()

    elif opcao_do_menu == '5':
        funcao_extrato()