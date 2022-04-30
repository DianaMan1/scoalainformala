# with open("fisier.txt", "w") as file:
#     file.write("Buna seara")

# file = open("fisier.txt", "w")
# file.write("Buna")
# file.close()
# file = open("fisier.txt", "r")
# try:
#     file.write("Buna ziua")
# except Exception:
#     pass
# finally:
#     file.close()
#
# with open("fisier1.txt", "w") as file:
#     file.write("Buna seara")
#
# with open("fisie2.txt", "a") as file:
#     file.write("Buna dimineata")

# with open("fisie2.txt", "r") as file:
#     for line in file.readlines():
#         print("line", line)

with open("fisie2.txt", "r") as file:
    for line in list(file):
        print('line', line)