menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor para ser depositado: "))

        if deposito > 0:
            print(f"Você depositou o valor de R$ {deposito}")
            saldo = deposito
            extrato += f"\nDeposito : R$ {deposito:.2f}"
        else:
            print("Deposite um valor positivo e maior que 0(zero).")
    
    elif opcao == "s":
        saque = float(input("Digite o valor para ser sacado: "))

        if saque <= 0:
            print("O valor precisa ser positivo para poder sacar.")
        elif saque > saldo:
            print("O valor excede o seu saldo.")
        elif saque > limite:
            print("O valor excede o seu limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("O seu limite de saques já foi excedido.")
        else: 
            print(f"Você sacou o valor de R$ {saque}")
            saldo -= float(saque)
            saque = float(saque)
            numero_saques += 1
            extrato += f"\nSaque : R$ {saque:.2f}"
    
    elif opcao == "e":
        print("\n========================= EXTRATO =========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================================")
    
    elif opcao == "q":
        break

    else: 
        print("Opção inválida, por favor selecione uma opção válida!")