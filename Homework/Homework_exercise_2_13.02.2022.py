# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]
# ○ suma numerelor pare de la [0, n]
# ○ suma numerelor impare de la [0. n]

def sum_of_all_numbers(number: int):
    if number == 0:
        return 0
    return number + sum_of_all_numbers(number-1)


def sum_of_even_numbers(number: int):
    if number <= 0:
        return 0
    if number % 2 == 0:
        return number + sum_of_even_numbers(number-2)
    if number % 2 == 1:
        return sum_of_even_numbers(number-1)


def sum_of_odd_numbers(number: int):
    if number <= 0:
        return 0
    if number % 2 == 1:
        return number + sum_of_odd_numbers(number-2)
    if number % 2 == 0:
        return sum_of_odd_numbers(number-1)


input = input('Enter a number = ')

try:
    result_1 = sum_of_all_numbers(int(input))
    print(result_1)
    result_2 = sum_of_even_numbers(int(input))
    print(result_2)
    result_3 = sum_of_odd_numbers(int(input))
    print(result_3)
except ValueError:
    print('Inccorect number. Please enter a correct number.')