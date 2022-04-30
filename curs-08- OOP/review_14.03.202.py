class ClasaMea:

    gamma = 0           # atribut sau variabila de clasa

    def __init__(self):              # constructor
        self.alpha = 1               # variabila de instanta pentru ca e definita in constructor
        self.__delta = 3             # variabila de instanta privata (are 2 __)


obj = ClasaMea()                     # instantiere a clasei, asa definim un obiect
obj.beta = 2                         # variabila de instanta si poate exista doar in interiorul obj
print(obj.__dict__)                  # returneaza un dictionar cu obiectele clasei
print(obj.alpha)                     # accesarea alpha din obiect
print(ClasaMea.gamma)                # acesare gamma
print(obj._ClasaMea__delta)          # accesare valoare privata
