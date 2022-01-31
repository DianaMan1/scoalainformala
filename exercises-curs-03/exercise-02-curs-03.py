my_string = 'Test-24.01.2022!'


def get_no_of_elements(my_string):
    count = 0
    for element in my_string:
        count += 1
    return count


print(get_no_of_elements(my_string))