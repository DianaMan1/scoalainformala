from random import choice

# condition_1 = 'exit'

# Ask for player name
nume_jucator = input('Cum te cheama?')

# Greet and show playing options
print("Optiunile tale sunt: \n Piatra \n Foarfeca \n Hartie")

# Player is asking to make a choice

while True:

    alegere_jucator = input('Alege o optiune: ')

    alegeri_totale = ['piatra', 'foarfeca', 'hartie']

    alegere_calculator = random.choice(alegeri_totale)

    print(f'Tu ai ales {alegere_jucator}, si calculatorul a ales {alegere_calculator}')

    if alegere_jucator == alegere_calculator:
        print('Ati ales amandoi acelasi lucru. Incearca din nou.')
    elif alegere_jucator == 'piatra' and alegere_calculator == 'foarfeca':
        print('Piatra bate foarfeca. Ai castigat!')
    elif alegere_jucator == 'foarfeca' and alegere_calculator == 'hartie':
        print('Foarfeca bate hartia. Ai castigat!')
    elif alegere_jucator == 'hartie' and alegere_calculator == 'piatra':
        print('Hartie bate piatra. Ai castigat!')

    elif alegere_jucator == 'foarfeca' and alegere_calculator == 'piatra':
        print('Piatra bate foarfeca. Ai pierdut!')
    elif alegere_jucator == 'hartie' and alegere_calculator == 'foarfeca':
        print('Foarfeca bate hartia. Ai pierdut!')
    elif alegere_jucator == 'piatra' and alegere_calculator == 'hartie':
        print('Hartie bate piatra. Ai pierdut!')

    restart_joc = input('Vrei sa joci din nou? Da/Nu: ')
    if restart_joc != "Da":
        break



