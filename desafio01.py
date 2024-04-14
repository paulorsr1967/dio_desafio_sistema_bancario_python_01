from datetime import datetime

def extratos(saldo, extrato):
    print('\n')
    print("-------------------- EXTRATO -------------------")
    if not extrato:
        print("Nenhuma movimentação encontrada.")
    else:
        for item in extrato:
            print(f"{item}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("------------------------------------------------")
    
def acrescenta_extrato(extrato, historico):
    data_e_hora_em_texto = datetime.now().strftime("%d/%m/%Y %H:%M")
    extrato.append(f"{str(len(extrato)+1).zfill(3)} - {data_e_hora_em_texto} - {historico}")
    
    
def deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        acrescenta_extrato(extrato, f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo
    
def saque(saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        acrescenta_extrato(extrato, f"Saque: R$ {valor:.2f}")
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, numero_saques

    
    
def main():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    saldo = 0
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3

    extrato = []

    while True:
        print(f'Saldo: R$ {saldo:.2f}')
        print(f'Número Saques: {numero_saques}')
        opcao = input(menu)

        if opcao == "d":
            saldo = deposito(saldo, extrato)

        elif opcao == "s":
            saldo, numero_saques = saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            extratos(saldo, extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
