# dacă condiție:
#   print('adevărat')
# dacă altă condiție:
#   print('nici aceasta nu este adevărată')
#altfel:
#   print("afișez doar dacă 'condiție' și 'altă condiție' nu sunt adevărate”)

# my_var = 5
# if my_var < 6:
#    print('set instrucțiuni #1')
# elif my_var < 10:
#    print('set instrucțiuni #2')
# else:
#    print('set instrucțiuni #3')
# print('a ieșit')

# my_var = 7
#    message = 'set instrucțiuni #3'
# if my_var < 6:
#    message = 'set instrucțiuni #1'
# elif my_var < 10:
#    message = 'set instrucțiuni #2'
# print(message)
# print('a ieșit')

# var = 1
# while var < 10:
#       var = var + 1
#   print('bloc de instrucțiuni', var)
#   var += 1
#   break

string = 'Ana are mere'
list = [1, 2, 3, 'a']
# for i, v in enumerate(list):
#     print(i, '=>', v)
for variabila_temporara in range(0, len(list)):
    print(list[variabila_temporara])
    print(variabila_temporara)

dictionar = {1: 'unu', 2: 'doi', 3: 'trei'}
for item in dictionar.keys():
    print(item, dictionar.get(item))