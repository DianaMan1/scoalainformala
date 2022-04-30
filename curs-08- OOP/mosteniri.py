# 1. Vehicul - clasă principală
# 1.1. Vehicul de apa - sub clase
# 1.2. Vehicul de aer
# 1.3.Vehicul de spatiu
# 1.4. Vehicul terestru
# 1.4.1. Vehicul de teren
# 1.4.2. Vehicul de curs
# 1. este super clasa pentru 1.1 => 1.4.
# 1.1. => 1.4. este subclasa pentru 1

# 2. Animale
# 2.1. Mamifere
# 2.1.1 Animale salbatice
# 2.1.2 Animale domestice
# 2.2. Reptile
# 2. pentru 2.1. si 2.2.este superclasa
# 2.1. si 2.2 pentru 2. sunt subclase
# 2.1.1. si 2.1.2 pentru 2.1 sunt subclase
# 2.1.1. si  2.1.2. pentru 2 sunt subclase

# Max este un caine mare care doarme toata ziua.
# obiectul -> Max (substantiv)
# clasa -> caine (substantiv)
# proprietatea -> mare (adjectiv)
# activitatea -> doarme toata ziua (verb) -> metoda

# Un Logan verde merge incet.
# obiect -> Logan
# clasa -> masina
# proprietate -> verde
# activitate -> merge incet

# sa se realizeze jocul x si 0 intre 2 jucatori in care:
# primul jucator este mereu calculatorul
# exista reguli de joc pentru mutari
# obiectele -> calculatorul / omul
# clasa -> Jocul
# proprietatea -> regulile
# activitatea -> mutarile / calculul de scor al jocului

# class MyFirstClass:
#     pass
#
#
# my_object = MyFirstClass()

stack = []

#
# def push(val):
#     stack.append(val)
#     return True
#
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return  val

# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())
#
# class Stack:
#
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def  __str__(self):
#         return f"{self.__stack_list}"
#
# obiect_stiva = Stack()
# obiect_stiva.push(3)
# obiect_stiva.push(2)
# obiect_stiva.push(1)
# print(obiect_stiva)
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())

# class  ClasaExemplu:
#
#     def __init__(self, val=1):
#         self.first = val
#         self.second = 0
#
#     def set_second(self, val=2):
#         self.second = val
#
#     def __str__(self):
#         return f"{self.first} {self.second}"
#
# obiect_1 = ClasaExemplu()
# obiect_2 = ClasaExemplu(2)
# obiect_3 = ClasaExemplu(3)
#
# print(obiect_1)
# print(obiect_2)
# print(obiect_3)
# print(obiect_3.second)

# class Caine:
#     nr_picioare = 4
#
#     def __init__(self, name, age=3):
#         self.__nume = name
#         self.__varsta = age
#         # Caine.nr_picioare = 3
#
#
#     def __str__(self):
#         return f"{self.__nume} - {self.__varsta}"
#
# obiect_1 = Caine('Rex', 4)
# print(obiect_1.__dict__)
# print(Caine.__dict__)
# print(hasattr(Caine, 'nr_picioare'))
# print(type(obiect_1).__name__)
# print(obiect_1.__dict__)
# var2 = obiect_1.__dict__
# print(obiect_1._Caine__nume)
# print(obiect_1.nr_picioare)
# print(obiect_1.varsta)
# print(obiect_1.nume)

# class Star:
#
#     def __init__(self, nume, galaxie):
#         self.name = nume
#         self.galaxy = galaxie
#
#     def __str__(self):
#         return f"{self.name} este in {self.galaxy}"
#
# soare = Star("Soarele", "Calea Lactee")
# print(soare)

# vehicul
# vehiculdeteren
# vehiculdetractare

# class Vehicul:
#     pass
#
# class VehiculTeren(Vehicul):                          # in paranteza se trece clasa pe care o mostesnete
#     pass
#
# class VehiculTractare(VehiculTeren):
#     pass

# parintii sunt Vehicul pentru VehiculTeren si VehiculTractare(indirect)
# parinte e VehiculTeren pentru VehiculTractare
# parintii sunt super clase pentru copii (superclass)
# copiii sunt VehiculTeren si VehiculTractare(indirect)
# copilul este VehiculTractare pentru VehiculTeren
# copiii se numesc subclase

# for cls1 in [Vehicul, VehiculTeren, VehiculTractare]:
#     for cls2 in [Vehicul, VehiculTeren, VehiculTractare]:                 # afisare relatii clase cu metoda issubclass
#         print(issubclass(cls1, cls2), end='\t')
#     print()
#

# vehicul1 = Vehicul()       #vehicul1 instanta pentru Vehicul
# vehicul_teren = VehiculTeren
# vehicul_tractare = VehiculTractare
# print(isinstance(vehicul1, VehiculTeren))        # daca vehicul1 este instanta de VehiculTeren
# print(isinstance(vehicul1, VehiculTractare))      # afiseaza true in momentul este mostenire sau mostenire indirecta

# class Exemplu:
#
#     def __init__(self, val):
#         self.value = val
#
# obiect_1 = Exemplu(0)
# obiect_2 = Exemplu(2)
# obiect_3 = obiect_1
# obiect_3.value += 1

# print(obiect_1 is obiect_2)
# print(obiect_2 is obiect_3)
# print(obiect_3 is obiect_1)
# print(obiect_1.value, obiect_2.value, obiect_3.value)

# string_1 = "Maria are mere "
# string_2 = "Maria are mere mari"
# string_1 = "mari"
#
# print(string_1 == string_2, string_1 is string_2)

class SuperClass:

    supVar = 1
    variabila = 6
    def __init__(self, nume):
        self.name = nume

    def __str__(self):
        return f'Numele meu este {self.name}'

class Clasa3:

    variabila = 5

    def __init__(self, nume):
        self.name = nume

class SubClass(Clasa3, SuperClass):               #ordinea de citirea a mostenirilor este de la stanga la dreapta

    subVar = 2 #variabila de clasa
    supVar = 3

    def __init__(self, nume):
        super().__init__(nume)

    # def __init__(self, nume):
    #     self.name = nume
 #       Super.__init__(self, nume)

    def __str__(self):
        return f"Nume"

obiect = SubClass('Alexandra')
print(obiect.supVar)
