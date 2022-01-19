'''
--> Dictionary is a mutable one.

-->We can do CRUD Operation on dictionary.

CRUD Operations,

--> Create
--> Retrieve
--> Update
--> Delete

'''
# Create a Dictionary:

profile = {"name": 'Karthi', "email": "kkk@gmail.com", "ph.no": "9786910190", 'district': 'Theni', "pincode": "625531"}
print("Profile            :", profile)

# Retrieve a dictionary:

print("Value for given key:", profile["name"])
profile["ph.no"] = "7904134297"
profile["email"] = "karthirk17@gmail.com"

print("Updated dictionary :", profile)

profile['city'] = 'banglore'    # can directly add key value pair just like assigning the value for index
print(profile)

dict1 = {'name': 'karthik', 'id': 29}
dict2 = {'number': 989999}
dict1.update(dict2)   # Using update() method also we can add add one dict to another
print(dict1)

dict2.update(dict1)
print(dict2)
# Delete:

del profile["email"]
print("Updated:", profile)

# del profile["pincode", "ph.no"]
del profile["pincode"]
print('updated value', profile)

del profile
print(profile)  # NameError: name 'profile' is not defined

