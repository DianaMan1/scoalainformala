print(ord("a"))
print(ord("d"))
print(chr(97))
print("Marian e \n\"amuzant\" ")
print(R"Marian e amuzant. \n Robert e amuzant")

my_first_list = [1, 2, 3, 4, 5, 6]
my_second_list = [2, 3, 4]
my_first_list.append("Diana")
print(my_first_list)
my_first_list.insert(0, 9)
print(my_first_list)
my_first_list.__len__()
print(my_first_list.__len__())
my_first_list.clear()
print(my_first_list)
my_first_list.insert(0, 1)
print(my_first_list)
my_first_list.remove(1)
print(my_first_list)
my_first_list.append(1)
print(my_first_list)
my_first_list.clear()
print(my_first_list)
my_first_list.insert(0, 2)
my_first_list.insert(1, 3)
print(my_first_list)
my_first_list.clear()
print(my_first_list)

list = [1, 2, 5, 6, 8, 9]
print(list)

ascendant_list = sorted(list)
print(ascendant_list)

descendant_list = sorted(list, reverse=True)
print(descendant_list)

# Dicționar

dex_1 = {}
print(dex_1)
dex_1 = {
    "Robert": "First",
    "Diana": "Second",
    "Marian": "Third"
}
print(dex_1)
dex_1.pop("Diana")
print(dex_1)
print(str(dex_1))

print(dex_1.items())
dex_1.pop("Robert")
print(dex_1)

dex_2 = {
    "Ana": "1",
    "Bia": "2",
    "Cam": "3"
}
print(dex_2)
dex_2.update({"Romi": "4"})
dex_2.update({"Ana": "2"})
print(dex_2)
dex_2["Andreea"] = "5"
print(dex_2)

# phone = input("Phone: ")
# my_phone_number = {
#    "1": "one",
#   "2": "two",
#    "3": "three",
#    "4": "four"
#}
# output = ""
# for ch in phone:
#    output += my_phone_number.get(ch, "!") + " "
# print(output)

# message = input(">")
# words = message.split(" ")
# emojis = {
#    ":)": "😊",
#    ":(": "☹"
# }
# output = ""
# for word in words:
#    output += emojis.get(word, word) + " "
# print(output)


def greet_user(name):
    print(f"Hi, {name}!")
    print("Welcome aboard!")


print("Start!")
greet_user("Robi")
greet_user("Didi")
print("Finish!")

my_string = [1, 2, 3, 4]

def get_no_of_elements(my_string):
    count = 0
    for element in my_string:
        count+= 1
    return count
print(get_no_of_elements(my_string))