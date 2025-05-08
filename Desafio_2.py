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


menu_titulo('Banco Agreste')

conta_corrente = []

Depositos = []
deposito = {}

Saques = []
saque = {}


Modelo_data_hora = "%H:%M do dia %d/%m/%Y"
modelo_data = "%d/%m/%Y"
data_hora_atual = datetime.datetime.now()
data_hora_amanha = data_hora_atual + datetime.timedelta(days=1)
data_amanha = data_hora_amanha.strftime(modelo_data)

Contator_de_transições = 0

while True:
    data_hora_atual = datetime.datetime.now()
    data_de_hoje = data_hora_atual.strftime(modelo_data)

    while True:
        menu_opcoes('Depósito', 'Saque', 'Extrato')
        opção_selecionada = str(input('\033[1;33mOpção: \033[m'))
        if opção_selecionada in '123':
            linha_menu()
            break
        else:
            print(f'\033[1;31mERRO: Escolha uma das 3 opções.')
            time.sleep(1)
            linha_menu()

    if opção_selecionada in '12':
        if Contator_de_transições < 11:
            if opção_selecionada == '1':
                while True:
                    try:
                        valor_deposito = float(input('Valor do deposito: '))
                        
                        if valor_deposito >= 1:
                            if len(conta_corrente) == 0:
                                conta_corrente.append(valor_deposito)
                                deposito['valor'] = valor_deposito
                                deposito['hora'] = data_hora_atual.strftime(Modelo_data_hora)
                                Depositos.append(deposito.copy())
                                print('Processando...')
                                time.sleep(2)
                                print('\033[1;32mDeposito realizado com sucesso.\033[1;32m')
                                Contator_de_transições += 1
                                time.sleep(2)
                                linha_menu()
                                break

                            else:
                                valor_em_conta = conta_corrente[0]
                                soma_dos_valores = valor_em_conta + valor_deposito
                                del conta_corrente[0]
                                conta_corrente.append(soma_dos_valores)
                                deposito['valor'] = valor_deposito
                                deposito['hora'] = data_hora_atual.strftime(Modelo_data_hora)
                                Depositos.append(deposito.copy())
                                print('Processando...')
                                time.sleep(2)
                                print('\033[1;32mDeposito realizado com sucesso.\033[m')
                                Contator_de_transições += 1
                                time.sleep(2)
                                linha_menu()
                                break

                        else:
                            print('\033[1;33mO valor minimo para deposito é de 1 real.\033[m')
                            linha_menu()
                    except ValueError:
                        print('\033[1;31mERRO: Digite um valor válido.\033[m')
                        linha_menu()
        
            elif opção_selecionada == '2':
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
                                    saldo_pos_saque = conta_corrente[0] - valor_saque
                                    del conta_corrente[0]
                                    conta_corrente.append(saldo_pos_saque)
                                    saque['valor'] = valor_saque
                                    saque['hora'] = data_hora_atual.strftime(Modelo_data_hora)
                                    Saques.append(saque.copy())
                                    print('\033[1mprocessando...\033[m')
                                    time.sleep(2)
                                    print('\033[1;32mSaque realizado com sucesso.\033[m')
                                    Contator_de_transições += 1
                                    time.sleep(2)
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
            if data_de_hoje == data_amanha:
                Contator_de_transições = 0
                data_amanha = data_de_hoje + datetime.timedelta(days=1)
            else:
                time.sleep(2)
                print('Você alcançou o limite diario de transições.')
                time.sleep(2)

    if opção_selecionada == '3':
        print('Processando...')
        print()
        time.sleep(2)
        if len(Depositos) > 0:
            contador = 1
            for item in Depositos:
                print(f'{contador}° Deposito: R${item['valor']} ás {item['hora']}')
                contador += 1
        if len(Saques) > 0:
            contador = 1
            for item in Saques:
                print(f'{contador}° Saque: R${item['valor']} ás {item['hora']}')
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