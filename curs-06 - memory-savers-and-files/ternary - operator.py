# a, b = 10, 20
# min = a if a < b else b (operator ternar)
# if a < b:
#     min = a
# else:
#     min = b
# print(min)

# lista_produse = ['ciocolata', 'suc', 'mere', 'miere', 'apa']
# lista_noua = [x if x != 'suc' else 'apa minerala' for x in lista_produse]
# print(lista_noua)

# lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# functie filter
# def functie_nr_pare(number):
#     if number % 2 == 0:
#         return True
#     return False
#
# iterator_numere_pare = filter(functie_nr_pare, lista_numere)
#
# print(list(iterator_numere_pare))
#
# litere = ['a', 'b', 'c', 'd', 'e', 'f']
#
#
# def filter_vocale(letter):
#     vocale = ['a', 'e']
#     return True if letter in vocale else False
#
# filtrare_vocale = filter(filter_vocale, litere)
# print(list(filtrare_vocale))