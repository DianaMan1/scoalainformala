print("Numele meu este Diana")
print(1, type(-1)) #tipul int
print(1.1, type (1.1)) #type float (rational / zecimal)
print(1j, type(1j)) #type complex
print(int(1.1)) #conversie float în int
print(float(1)) #concersie de int în float
print(1+1) #adunare
print(1-1)
print(1*0)
print(1*5)
print(5/2) #împărțire exactă
print(5 // 2) #câtul
print(5 % 2) # restul => modulo
print(5 ** 2) #ridicare la putere
print(5 == 2) #operator de egalitate => returnează un boolean (True 1 sau False 0)
print(5 != 2) #operator de diferențiere => returnează un boolean (True 1 sau False 0)
print(5 < 2)
print(5 > 2)
print(5 >= 2)
print(5 <= 2)
print(5 > 2 and 3 > 1) #operator logic and
print(5 > 2 or 3 > 1) #opeator logic or
print(not(5 > 2 and 3 > 1)) #operator de negare
# print(7 is 7)
# print(7 is not 7)

# my_var = 0
# my_var, my_var_1 = 0, 1
# my_var = 3
# my_var = my_var + 1 #asignare prin adunare/incrementate
# my_var += 1
# my_var *= 2 #asignare prin înmulțire

print("Ana are mere")

variabila = "Ana \'are\' \n mere" # \n - despărțim pe mai multe rânduri
print(variabila)
nume = "Man"
prenume = "Diana"
vârstă = 20
înâlțime = 1.65
# prezentare = "Numele meu este {} și prenumele meu este {}".format(nume, prenume)
# prezentare = f"Numele meu este {nume} și prenumele este {prenume}."
# prezentare = "Numele meu este " + nume + " și prenumele este " + prenume + "."
# prezentare = "Numele meu este " + nume + " și prenumele este " + prenume + " și vârsta mea este " + str(vârstă) + "."
# prezentare = f"Numele meu este {nume} și prenumele este {prenume} și vârsta este {vârstă}"
# print(prezentare)
#calcul = vârstă + înâlțime
#print(calcul)
calcul = nume + prenume
print(calcul)

