saldo = 1000.0

while True:
    print("   SENAIBank - Terminal de Atendimento   ")
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        print(f"\n[INFO] Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == '2':
        try:
            valor_deposito = float(input("\nDigite o valor para depósito: R$ "))
            if valor_deposito > 0:
                saldo += valor_deposito
                print(f"[SUCESSO] Depósito de R$ {valor_deposito:.2f} realizado.")
            else:
                print("[ERRO] O valor do depósito deve ser maior que zero.")
        except ValueError:
            print("[ERRO] Entrada inválida. Digite apenas números.")

    elif opcao == '3':
        try:
            valor_saque = float(input("\nDigite o valor para saque: R$ "))
            if valor_saque > 0:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    print(f"[SUCESSO] Saque de R$ {valor_saque:.2f} realizado.")
                else:
                    print("[ERRO] Saldo insuficiente para realizar este saque.")
            else:
                print("[ERRO] O valor do saque deve ser maior que zero.")
        except ValueError:
            print("[ERRO] Entrada inválida. Digite apenas números.")

    elif opcao == '4':
        print("\nObrigado por utilizar o SENAIBank. Até logo!")
        break

    else:
        print("\n[ERRO] Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
