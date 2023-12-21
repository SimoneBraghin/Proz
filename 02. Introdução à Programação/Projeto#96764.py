def calculadora():
    while True:
        print("Escolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == '0':
            print("Saindo da calculadora.")
            break
        elif opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe.\n")
            continue

        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

        if opcao == '1':
            resultado = valor1 + valor2
            print(f"O resultado da soma é: {resultado}\n")
        elif opcao == '2':
            resultado = valor1 - valor2
            print(f"O resultado da subtração é: {resultado}\n")
        elif opcao == '3':
            resultado = valor1 * valor2
            print(f"O resultado da multiplicação é: {resultado}\n")
        elif opcao == '4':
            if valor2 == 0:
                print("Não é possível dividir por zero. Tente novamente.\n")
                continue
            resultado = valor1 / valor2
            print(f"O resultado da divisão é: {resultado}\n")

calculadora()