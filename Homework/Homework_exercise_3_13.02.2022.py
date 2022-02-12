# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă:
# aceasta este un număr întreg, altfel returnează valoarea 0.

number = input('Enter a number: ')


def is_integer(number: str):
    try:
        int(number)
        return number
    except ValueError:
        return 0


print(is_integer(number))

