lista_1 = [1, 2 , 3]
lista_2 = [4, 5, 6]

rezultat = zip(lista_1, lista_2)
print(set(rezultat))  # print(list(rezultat))

# functia desfasurata

def zip_function(list_1, list_2):
    lista = []
    for i in range(0, min(len(lista_1), len(list_2))):
        lista.append((list_1[i], list_2[i]))
    return lista

print(zip_function(lista_1, lista_2))