valid_msg = 'cnp is valid'
invalid_msg = 'cnp is invalid'

CONTROL_CHAR_NUMBER = '279146358279'

is_valid = False

cnp = input('Enter a cnp: ')

while True:
    if len(cnp) != 13:
        break

    if not cnp.isdigit():
        break

    month = int(f'{cnp[3]}{cnp[4]}')
    if month < 1 and month > 12:
        break

    day = int(f'{cnp[5]}{cnp[6]}')
    if day < 1 and day > 31:
        break

    county = int(f'{cnp[7]}{cnp[8]}')
    if county < 1 and county > 52:
        break

    nnn = int(f'{cnp[9]}{cnp[10]}{cnp[11]}')
    if nnn < 1:
        break

    control_char = int(cnp[12])

    sum = 0
    for index in range(12):
        sum = int(CONTROL_CHAR_NUMBER[index]) * int(cnp[index]) + sum

    last_digit = int(cnp[12])
    modulo = sum % 11

    if modulo == 10 and last_digit != 1:
        break
    if modulo != last_digit:
        break

    is_valid = True
    break

if is_valid:
    print(valid_msg)
else:
    print(invalid_msg)