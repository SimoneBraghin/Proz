# Exercício Regar a planta:
"""
Este arquivo consiste nas atividades desenvolvidas durante as aulas síncronas, sendo então propostas coletivas, 
não apenas de autoria da criadora deste repositório
"""


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
            print("Você digitou um número ímpar. O número deve ser par")
        elif numeroUser % 3 != 0:
            print("O número deve ser divisível por 3")
        else:
          print("Obrigada pelo preenchimento! O número " + respostaUsuario + " é um valor válido")
          valorUsuario = True

pedirNumero()
"""

# Exercício de exemplo da aula:
"""
numeroCorreto = False

while (numeroCorreto == False):
   print("Insira um número par")
   try:
       numero = int(input())
       if (numero%2 == 0):
           numeroCorreto = True
           print("Você digitou um numero par !")
       else :
           print("Você digitou um número impar")
   except:
       print("Caracter inválido, por favor digite um número par")
"""

# 08/01

# Escreva uma função que verifica se array contém dado elemento

def verificarElemento(array, elemento):
    return elemento in array

elemento_existe = verificarElemento([1,2,3,4,5,6], "hello")
print(elemento_existe)

