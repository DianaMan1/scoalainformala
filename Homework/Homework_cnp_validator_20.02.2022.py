def validate_length(cnp):
    return len(cnp) == 13


def validate_format(cnp):
    return cnp.isdigit()


def validate_month(month):
    return 1 <= month <= 12


def validate_day(day):
    return 1 <= day <= 31


def validate_county(county_index):
    return 1 <= county_index <= 52


def validate_nnn(nnn_index):
    return nnn_index >= 1


def validate_control_char(cnp):
    control_char_number = '279146358279'
    current_sum = 0

    for index in range(12):
        current_sum = int(control_char_number[index]) * int(cnp[index]) + current_sum

    last_digit = int(cnp[12])
    modulo = current_sum % 11

    if modulo == 10 and last_digit != 1 or modulo != last_digit:
        return False

    return True


def validate(cnp_param):
    cnp_month = int(f'{cnp_param[3]}{cnp_param[4]}')
    cnp_day = int(f'{cnp_param[5]}{cnp_param[6]}')
    cnp_county = int(f'{cnp_param[7]}{cnp_param[8]}')
    cnp_nnn = int(f'{cnp_param[9]}{cnp_param[10]}{cnp_param[11]}')

    if validate_length(cnp_param) and\
            validate_format(cnp_param) and\
            validate_month(cnp_month) and\
            validate_day(cnp_day) and\
            validate_county(cnp_county) and\
            validate_nnn(cnp_nnn) and\
            validate_control_char(cnp_param):
        return True
    return False


inputted_cnp = input('Enter a CNP:')

if validate(inputted_cnp):
    print('cnp is valid')
else:
    print('cnp is invalid')