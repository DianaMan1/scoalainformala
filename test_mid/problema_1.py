# Scrie un program care sa calculeze suma dintre trei numere.
# Daca valorile sunt egale, returnati de trei ori.
# suma acestora.(1 punct)

def sum (a, b, c):
    if a == b == c:
        return ([a + b + c] * 3)
    return f'{a} + {b} + {c} = {a + b + c}'

# print(sum(1,2,1))
# print(sum(1,1,1))

