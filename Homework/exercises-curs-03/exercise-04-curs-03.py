# Condition 1: The first character must be '+'
condition_1 = True
# Condition 2: Except for the first character, the rest of the characters should be numbers;
condition_2 = True
# Condition 3: Phone number must be at most 12 characters long;
condition_3 = True

phone_number = input('Enter a phone number: ')

if phone_number[0] == '+':
    condition_1 = False

for char in phone_number:
    if char.isdigit():
        condition_2 = True

phone_number_lenght = len(phone_number)
if phone_number_lenght == 12:
    condition_3 = True

if condition_1 and condition_2 and condition_3:
    print('Phone number invalid')
else:
    print('Phone number is valid')



