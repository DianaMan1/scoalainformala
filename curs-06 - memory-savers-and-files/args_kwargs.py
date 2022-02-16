# def my_function(*param_1):
#     print(type(param_1))
#     return param_1
#
# print(my_function('string', 'string1', 'string2'))

# def numbers_sum(*var):
#     suma = 0
#     for item in var:
#         suma = suma + item
#     return suma
#
# print(numbers_sum(1, 2, 3, 4, 5))

# def diff_vars(*params):
#     diferenta = 0
#     for item in params:
#         diferenta = diferenta - item
#     return diferenta
#
# print(diff_vars(1, 2, 3, 4))

def catalog(*args, **kwargs):
    return args, kwargs.keys()


print(catalog(1, 2, nume="Popa", prenume="Ionut", varsta="12"))
