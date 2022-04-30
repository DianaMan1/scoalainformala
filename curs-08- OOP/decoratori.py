# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"
#
# print(functie_simpla())
#
# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def ambalaj_intern(*args):
#             print(f"Ambalam produse din {functia_noastra.__name__} cu {material}")
#             return f'Ambalam produse din {functia_noastra.__name} cu {material}:{','.join(x for x in (functia_noastra(*args)))}'
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit("hartie")
# def impachetare_carti(*args):
#     return args
#
# @decorator_depozit("folie_alimentara")
# def impachetare_fructe(*args):
#     return args
#
#
# print(impachetare_fructe("mere", "pere"))
#
# def decorator(functie):
#     def decoreaza(var):
#         return functie(var)
#     return decoreaza
#
# def p(functie):
#     def decoreaza(var):
#         return f"<p>{functie(var)}<p>"
#     return decoreaza
#
# @p
# def text(sir):
#     return sir.upper()
#
# text_p = decorator(text)
# print(text_p("Salut"))

# class Dog:
#
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property                           #citeste valoarea din atribut
#     def name(self):
#         return self.__nume
#
#     @name.setter                        #scrie valoarea
#     def name(self, nume):
#         self.__nume = nume
#
#     @name.deleter
#     def name(self):
#         del self.__nume
#
# my_dog = Dog(nume="Rex")
# print(my_dog.name)
#
# my_dog.name = "Ben"
# print(my_dog.name)
#
# del my_dog.name
# print(my_dog.name)

# class Cat:
#
#     legs_no = 4
#
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property
#     def name(self):
#         return self.__nume
#
#     @name.setter
#     def name(self, nume):
#         self.__nume = nume
#
#     @name.deleter
#     def name(self, nume):
#         del self.__nume
#
#     def change_name(self, name):
#         self.__nume = nume
#
#     def __str__(self):
#         return f"{self.__nume}"
#
# cat_object = Cat("Fluffy")
# # cat_object.change_name("Milly")
# # print(cat_object)
# print(cat_object.name)
# cat_object.name = "Milly"
# print(cat_object.name)

from datetime import date

class Persoana:

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    @classmethod
    def varsta_ani(cls, nume, varsta):
        return cls(nume, date.today().year - varsta)

    @staticmethod
    def stare(varsta):
        return varsta > 18

persoana_1 = Persoana("Ion", 21)
print(persoana_1.varsta)
persoana_2 = Persoana.varsta_ani("Maria", 20)
print(persoana_2.varsta)
print(Persoana.stare(22))