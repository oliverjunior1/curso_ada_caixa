lista_exercicio = ['Stone', 1, 'Lets', 2, True, '2', 'show', 234, 87, 1.33333, 7.0000, 1e-9, 'uasdhfusah', 'zuei', False, False, True, 132434, "1324123", "False", "True", "Sucesso", 5, "u", "c", 3, 55, 0]

booleano = 0
inter = 0
floated = 0  # nome alternativo para evitar conflito com o tipo float
stringed = 0
complexed = 0

for x in lista_exercicio:
    if type(x) == bool:
        booleano += 1
    elif type(x) == int:
        inter += 1
    elif type(x) == float:
        floated += 1
    elif type(x) == str:
        stringed += 1



print("Quantidade de valores booleanos:", booleano)
print("Quantidade de valores int:", inter)
print("Quantidade de valores float:", floated)
print("Quantidade de valores str:", stringed)
