# demonstrate hashtable usage


# TODO: create a hashtable all at once

items1 = dict({"key1" : 1, "key2" : 2, "key3" : 3})
print(items1)
print(items1["key2"])
items1["key2"] = "BOOM!!!"
print(items1["key2"])
print(items1)

print("----------------------------")

items2 = {}

items2["key4"] = 4
items2["key5"] = 5
items2["key6"] = 6

print(items2)

print("----------------------------")

for key, value in items2.items():
    print("key: " , key, " value ", value)
