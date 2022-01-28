# tuple
list = [1, 2, 3, 1, 'a']
list_1 = ['a', 'b', 'c']
list_total = list + list_1
print(list_total)
tuple = (1, 2, 3, 1, 'a')
tuple_1 = (1, 2, 3, 1, 'a')
tuple_total = tuple + tuple_1
print(tuple_total)
new_tuple = ('1',)
print(type(new_tuple))
dictionary = {"key1": "1", 1: "1", "list": [1, 2, 3]}
print(dictionary["key1"])
print(dictionary.get("key2"))
dictionary["key1"] = 2
dictionary["key2"] = 3
dictionary.update({"key1": 2})
dictionary.update({"key2": 4})
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
my_set = {}
my_set = {1, 1, 3}
print(my_set)
print(list_total)
print(set(list_total))
