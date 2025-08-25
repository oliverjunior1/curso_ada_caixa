# Projeto: Venda de veículos usados Loja CAIXAVERSO
# Grupo: Joaquim, Ingrid
# e
# Kelly

# Listagem dos nossos carros
carros = {
    1: {"modelo": "Fiat Uno", "ano": 2010, "preco": 15000},
    2: {"modelo": "Fort KA", "ano": 2015, "preco": 25000},
    3: {"modelo": "Chevrolet Onix", "ano": 2018, "preco": 40000},
    4: {"modelo": "Toyota Corolla", "ano": 2020, "preco": 85000}
}


# Mostra os carros disponíveis
def mostrar_carros():
    print("\n=== CARROS DISPONÍVEIS CAIXAVERSO ===")
    for id, info in carros.items():
        print(f"{id} - {info['modelo']} ({info['ano']}) - R$ {info['preco']}")


# Função principal
def vender_carro():
    mostrar_carros()

    # Cliente escolhe um carro
    escolha = int(input("\nDigite o número do carro que você deseja comprar: "))

    # Verifica se a escolha existe
    if escolha in carros:
        carro = carros[escolha]
        print(f"\nVocê escolheu: {carro['modelo']} ({carro['ano']}) - R$ {carro['preco']}")

        # Confirmação da compra
        confirmar = input("Deseja confirmar a compra? (s/n): ").lower()

        if confirmar == "s":
            print(f"\nParabéns! Você comprou o {carro['modelo']} da loja CAIXAVERSO!")
        else:
            print("\nCompra cancelada.")
    else:
        print("\nNúmero inválido. Tente novamente.")


# Iniciar programa
print("Bem-vindo à loja de veículos CAIXAVERSO!")
vender_carro()