x = open('operacoes_realizadas.txt', 'a')
x.write('#############SIMPLE-BANK#################\n')
saldo = 0
# Fazer a função de saque
def saque(valor):
  global saldo
  if saldo>0 and valor<=saldo:
    saldo -=valor
    print(f"seu saldo após o saque é R$ {saldo:.2f}")
    x = open("operacoes_realizadas.txt", 'a')
    x.write(f"saque de R$ {valor:.2f}: saldo de R$ {saldo:.2f}\n")


  else:
    print("Saldo Insuficiente!")


# Fazer a função de depósito
def deposito(valor):
  global saldo
  saldo += valor
  print(f"Seu saldo após o deposito é: R$ {saldo:.2f}")
  x = open("operacoes_realizadas.txt", 'a')
  x.write(f"deposito de R$ {valor:.2f}: saldo de R$ {saldo:.2f}\n")


# Fazer a função de mostar o saldo
def mostrar_saldo():
    print(f"Seu saldo atual é de: R$ {saldo:.2f}")

# Fazer a função de extrato
def extrato():
    x = open('operacoes_realizadas.txt', 'r')
    print(x.read())
    x.close()

# Finalizar para as opções do cliente
print('''###########SIMPLE-BANK##############''')

while True:
    opcoes = int(input("Para saque (1), deposito (2), ver saldo (3), extrato (4) sair (5): "))
    match opcoes:
        case 1:
            saque(float(input("Qual o valor do saque?")))
        case 2:
            deposito(float(input("Qual o valor do depósito? ")))
        case 3:
            mostrar_saldo()
        case 4:
            extrato()
        case 5:
            break

x = open('operacoes_realizadas.txt', 'w')
x.write('')
x.close()