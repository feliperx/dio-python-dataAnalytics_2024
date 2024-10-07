#feliperx

MENU = """

[D] Depositar
[E] Extrato
[S] Sacar
[Q] Sair

=> """

LIMIT = 500
ACCOUNT_BALANCE = 0
EXTRACT = ""
WITHDRAWAL_COUNT = 0
WITHDRAWAL_LIMIT = 3

#loop
while True:

    option = input(MENU)

    if option == "D":
        value = float(input("Informe o valor do depósito: "))

        if value > 0:
            ACCOUNT_BALANCE += value
            EXTRACT += f"Depósito: R$ {value:.2f}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif option == "S":
        value = float(input("Informe o valor do saque: "))

        exceeded_balance = value > ACCOUNT_BALANCE
        exceeded_limit = value > LIMIT
        exceeded_withdrawals = WITHDRAWAL_COUNT >= WITHDRAWAL_LIMIT

        if exceeded_balance:
            print("Falha na operação! Não há saldo suficiente.")

        elif exceeded_limit:
            print("Falha na operação! O valor do saque excedeu o limite.")

        elif exceeded_withdrawals:
            print("Falha na operação! O limite de saques foi excedido.")

        elif value > 0:
            ACCOUNT_BALANCE -= value
            EXTRACT += f"Saque de: R$ {value:.2f}\n"
            WITHDRAWAL_COUNT += 1

        else:
            print("Falha na operação! Valor informado inválido.")

    elif option == "E":
        print("\n>>>>>>>>>>>>>> EXTRATO\n")
        print("Não foram realizadas movimentações nessa conta." if not EXTRACT else EXTRACT)
        print(f"\nSaldo atual: R$ {ACCOUNT_BALANCE:.2f}")
        print("****************************")

    elif option == "Q":
        break

    else:
        print("Essa operação é inválida")
        print("Por favor, selecione novamente a operação desejada.")