# def numbers(x,y, z):
#     sum = x + y + z
#     return sum
#
# print(numbers(10,20,30))

# def numbers(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum
#
# print(numbers(10,20,30,40))
# num1 = 0
# num2 = 0
# def operacao(num1, num2):
#     num1 = float(input("Coloque o número 1: "))
#     num2 = float(input("Coloque o numero 2: "))
#     operator = input("Coloque se será multiplicação, divisão, subtração ou soma: ")
#
#     if operator=="soma":
#         return num1+num2
#     elif operator=='subtracao':
#         return num1-num2
#     elif operator=='multiplicacao':
#         return num1*num2
#     elif operator=="divisao":
#         return num1/num2
#     else:
#         return "Operador inexistente"
#
# print(operacao(num1, num2))

def date_convert():
    data = input("Coloque a data no formato DD/MM/AAAA: ")
    partes = data.split('/')

    if len(partes) != 3:
        return "Formato inválido. Use DD/MM/AAAA."

    dia, mes, ano = partes

    try:
        mes_num = int(mes)
    except ValueError:
        return "Mês inválido."

    match mes_num:
        case 1: y = 'Janeiro'
        case 2: y = 'Fevereiro'
        case 3: y = 'Março'
        case 4: y = 'Abril'
        case 5: y = 'Maio'
        case 6: y = 'Junho'
        case 7: y = 'Julho'
        case 8: y = 'Agosto'
        case 9: y = 'Setembro'
        case 10: y = 'Outubro'
        case 11: y = 'Novembro'
        case 12: y = 'Dezembro'
        case _: return "Mês fora do intervalo válido."

    return f"{dia} de {y} de {ano}"

# Testando
print(date_convert())