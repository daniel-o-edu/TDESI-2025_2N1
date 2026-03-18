while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        result = num1 / num2
        print(f"O resultado de {num1} dividido por {num2} é: {result}")
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero. Por favor, insira um segundo número diferente de zero.") 
        break 