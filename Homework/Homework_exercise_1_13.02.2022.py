# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze
# suma parametrilor
# care reprezintă numere întregi sau reale.
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# ○ your_function() va returna 0.
# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

def get_sum(*args):
    sum = 0
    for element in args:
        element_type = type(element)
        if element_type == int or element_type == float:
            sum = sum + element
    return sum

param_1 = 2

print(get_sum(1, 5, -3, 'abc', [12, 56, 'cad']))
print(get_sum())
print(get_sum(2, 4, 'abc', param_1))