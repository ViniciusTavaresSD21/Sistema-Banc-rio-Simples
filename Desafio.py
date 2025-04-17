import time

# CRIANDO UM SISTEMA BANCARIO

# 1° Passo - Criar uma função que faça uma linha para o menu.
def linha_menu(tamanho_da_linha=30):
    print(f'\033[1;31m{'='*tamanho_da_linha}\033[m')

# 2° Passo - Criar uma função que faça um texto para o menu.
def texto_menu(texto, tamanho_da_linha=30):
    print(f'\033[1m{texto.center(tamanho_da_linha)}\033[m')

# 3° Passo - Criar uma função que faça um titulo.
def menu_titulo(texto, tamanho_menu=30):
    linha_menu(tamanho_menu)
    texto_menu(texto, tamanho_menu)
    linha_menu(tamanho_menu)

# 4° Passo - Criar uma função que faça um menu de opção.
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

# 5° Passo - Criar o menu com as opções.
menu_titulo('Banco Agreste')

# 6° Passo - programar a seleção de opções.
conta_corrente = []
Depositos = []
Saques = []
contador_de_saques = 1
while True:
    while True:
        menu_opcoes('Depósito', 'Saque', 'Extrato', 'Sair')
        opção_selecionada = str(input('\033[1;33mOpção: \033[m'))
        if opção_selecionada in '1234':
            linha_menu()
            break

        else:
            print(f'\033[1;31mERRO: Escolha uma das 3 opções.')
            linha_menu()

# 7° Passo - Programar a opção de deposito.
    if opção_selecionada == '1':
        while True:
            try:
                valor_deposito = float(input('Valor do deposito: '))
                if valor_deposito >= 1:
                    if len(conta_corrente) == 0:
                        Depositos.append(valor_deposito)
                        conta_corrente.append(valor_deposito)
                        print('Processando...')
                        time.sleep(2)
                        print('\033[1;32mDeposito realizado com sucesso.\033[1;32m')
                        time.sleep(2)
                        linha_menu()
                        break

                    else:
                        Depositos.append(valor_deposito)
                        valor_em_conta = conta_corrente[0]
                        soma_dos_valores = valor_em_conta + valor_deposito
                        del conta_corrente[0]
                        conta_corrente.append(soma_dos_valores)
                        print('Processando...')
                        time.sleep(2)
                        print('\033[1;32mDeposito realizado com sucesso.\033[m')
                        time.sleep(2)
                        linha_menu()
                        break
                else:
                    print('\033[1;33mO valor minimo para deposito é de 1 real.\033[m')
                    linha_menu()
            except ValueError:
                print('\033[1;31mERRO: Digite um valor válido.\033[m')
                linha_menu()

# 8° Passo - Programar a opção de saque:
    elif opção_selecionada == '2':
        if contador_de_saques < 4:
            try:
                if conta_corrente[0] == 0:
                    print('\033[1;33mVocê não tem saldo em conta.\033[m') 
                    linha_menu()
                    time.sleep(2)
            except IndexError:
                print('\033[1;33mVocê não tem saldo em conta.\033[m')
                linha_menu()
                time.sleep(2)
            else:
                while True:
                    try:
                        valor_saque = float(input('Valor do saque: '))
                        if valor_saque <= conta_corrente[0] and valor_saque <= 500:
                            Saques.append(valor_saque)
                            saldo_pos_saque = conta_corrente[0] - valor_saque
                            del conta_corrente[0]
                            conta_corrente.append(saldo_pos_saque)
                            print('\033[1mprocessando...\033[m')
                            time.sleep(2)
                            print('\033[1;32mSaque realizado com sucesso.\033[m')
                            time.sleep(2)
                            contador_de_saques += 1
                            linha_menu()
                            break

                        elif valor_saque > 500:
                            print('\033[1;33mVocê só pode sacar até 500 reais.\033[m')
                            linha_menu()
                            time.sleep(2)

                        elif conta_corrente[0] < valor_saque:
                            print('\033[1;33mVocê não tem saldo suficiente.\033[m')
                            linha_menu()
                            time.sleep(2)

                    except ValueError:
                        print('\033[1;31mDigite um número valido.\033[m')
                        linha_menu()
                        time.sleep(2)
        else:
            print('\033[1;33mVocê atingiu o numero máximo de saques por hoje.\033[m')
            linha_menu()
            time.sleep(2)

# 9° Passo - Programar a opção de extrato.
    elif opção_selecionada == '3':
        print('Processando...')
        print()
        time.sleep(2)
        if len(Depositos) > 0:
            contador = 1
            for i in Depositos:
                print(f'{contador}° Deposito: R{i}')
                contador += 1
        if len(Saques) > 0:
            contador = 1
            for i in Saques:
                print(f'{contador}° Saque: R{i}')
                contador += 1
        try:
            print()
            print(f'\033[1mSaldo: R${conta_corrente[0]}\033[m')
            linha_menu()
            time.sleep(2)
        except IndexError:
            print('\033[1mVocê não tem saldo em conta.\033[m')
            linha_menu()
            time.sleep(2)

# 10° Passo - Encerrar o Programa.
    elif opção_selecionada == '4':
        print('\033[1;33mPrograma encerrado.\033[m')
        linha_menu()
        break