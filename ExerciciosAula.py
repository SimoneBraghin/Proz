# Exercício Regar a planta:
"""
i = 0
while i <= 5:
    print("Robôzin, por favor regue a planta de número " + str(i))
    i += 1
"""
# Pedir para o robô regar apenas as plantas de números pares, sendo o intervalo de 0 a 5:
"""
i = 0

while i <= 5:
    if i % 2 == 0:
        print("Robôzin, por favor regue a planta de número " + str(i))
        i += 1
"""

# Criar uma função que peça ao usuário um número entre 0 e 100 até que um valor válido seja recebido
# Acrescentar a restrição de que o número inserido seja par
# Acrescentar a restrição de que o número inserido seja divisível por 3
"""
def pedirNumero():

    valorUsuario = False

    while not valorUsuario:

        respostaUsuario = input("Escreva um número entre 0 a 100: ")
        numeroUser = int(respostaUsuario)

        if numeroUser > 100:
            print("O número deve ser menor ou igual a 100")
        elif numeroUser < 0:
            print("O número deve ser maior ou igual a zero")
        elif numeroUser % 2 != 0:
            print("O número deve ser par")
        elif numeroUser % 3 != 0:
            print("O número deve ser divisível por 3")
        else:
          print("Obrigada pelo preenchimento! O número " + respostaUsuario + " é um valor válido")
          valorUsuario = True

pedirNumero()
"""

