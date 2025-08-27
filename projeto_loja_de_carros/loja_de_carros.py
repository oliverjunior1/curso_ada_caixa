import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# opções do funcionário
def opcoes_funcionario():
    print("""
         ADA LOJA DE CARROS
         ______
        /|_||_\`.__
       (   _    _ _\\
       =`-(_)--(_)-'
    """)
    return input("Digite (1) para vender carro:\n"
                 "Digite (2) para comprar carro:\n"
                 "Digite (3) para ver os carros disponíveis:\n"
                 "Digite (4) para sair. Digite: ")

# vender carro
def vender_carro():
    try:
        with open('carros.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo 'carros.txt' não encontrado.")
        return

    linhas = [linha.strip() for linha in linhas]

    print("=== CARROS DISPONÍVEIS PARA VENDA ===")
    opcoes = []
    for i, linha in enumerate(linhas):
        partes = linha.split(' - ')
        if len(partes) == 4:
            modelo, cor, ano, valor = partes
            try:
                valor_original = float(valor.replace('R$', '').replace(',', '.'))
                valor_final = round(valor_original * 1.3, 2)
                print(f"{i + 1}. {modelo} | {cor} | {ano} | Valor com acréscimo: R${valor_final:.2f}")
                opcoes.append((modelo, cor, ano, valor_final))
            except ValueError:
                print(f"{i + 1}. {linha} (valor inválido)")
        else:
            print(f"{i + 1}. {linha} (formato inválido)")

    try:
        escolha = int(input("\nDigite o número do carro que deseja comprar: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if 1 <= escolha <= len(opcoes):
        indice = escolha - 1
        modelo, cor, ano, valor_pago = opcoes[indice]
        print("\n=== COMPRA REALIZADA COM SUCESSO ===")
        print(f"Você comprou o carro:\nMarca: {modelo}\nModelo: {cor}\nAno: {ano}\nValor pago: R${valor_pago:.2f}")

        # Remove a linha correspondente ao carro comprado
        del linhas[indice]
        with open('carros.txt', 'w', encoding='utf-8') as arquivo:
            for linha in linhas:
                arquivo.write(linha + '\n')
    else:
        print("Opção inválida. Nenhum carro foi comprado.")



# comprar carro
def comprar_carro():
    marca = input("Qual a marca do carro? ")
    modelo = input("Qual o modelo do carro? ")
    ano = input("Qual o ano do carro? ")
    valor = input("Qual o valor do carro na tabela fipe? ")
    with open('carros.txt', 'a', encoding='utf-8') as comprar:
        comprar.write(f"{marca} - {modelo} - {ano} - R${valor}\n")
    print("Carro comprado com sucesso.")

# consultar carros disponíveis
def consultar_carros():
    try:
        with open("carros.txt", 'r', encoding='utf-8') as consultar:
            print("\n=== CARROS DISPONÍVEIS ===")
            print(consultar.read())
    except FileNotFoundError:
        print("Arquivo 'carros.txt' não encontrado.")

# loop principal
while True:
    limpar_tela()
    opcao = opcoes_funcionario()
    match opcao:
        case '1':
            vender_carro()
        case '2':
            comprar_carro()
        case '3':
            consultar_carros()
        case '4':
            print("Encerrando o sistema. Até logo!")
            break
        case _:
            print('Opção inválida.')
    input("\nPressione Enter para continuar...")

