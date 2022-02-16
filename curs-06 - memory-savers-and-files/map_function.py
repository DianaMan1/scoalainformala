# def adunare(n):
#     return n + n
#

lista_numere = [1, 2, 3, 4]
lista_numere_2 = [5, 6, 7, 8]
# rezultat = map(adunare, lista_numere)
# print(list(rezultat))

rezultat = map(lambda n, m, : n + m, lista_numere, lista_numere_2)
print(list(rezultat))

# another variant:

def adunare(lista_numere, lista_numere_2):
    for i, v in enumerate(lista_numere):
        for j, w in enumerate(lista_numere_2):
         #   suma = lista_numere[i] + lista_numere_2[j]
            suma = v + w
    return suma

print(adunare(lista_numere, lista_numere_2))