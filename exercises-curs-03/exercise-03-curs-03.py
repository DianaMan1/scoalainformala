# Condition 1: At least first 5 chars to be alphanumeric;
condition_1 = True

# Condition 2: "@" appears once and after at least five characters;
condition_2 = False
at_occurrences = 0

# Condition 3: "." appears once and after at least five characters after "@";
condition_3 = False
point_occurrences = 0

# Condition 4:  index "@" < index "."
condition_4 = False

email_address = input("Enter an email address: ")

for index, char in enumerate(email_address):
    if index >= 0 and index <= 4:
        if not char.isalnum():
            condition_1 = False
    if index >= 5:
        if char == '@':
            at_occurrences += 1
    if index >= 11:
        if char == '.':
            point_occurrences += 1

if at_occurrences == 1:
    condition_2 = True
if point_occurrences == 1:
    condition_3 = True
if email_address.index('@') < email_address.index('.'):
    condition_4 = True

if condition_1 and condition_2 and condition_3 and condition_4:
    print('Mailul este valid')
else:
    print('Mailul este invalid')

















