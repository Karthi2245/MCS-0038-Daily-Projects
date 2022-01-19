'''
Dictionary:
--> Group of elements arranged in the form of key&value pair.
--> First element considered as Key and the immediate next element considered
as Value.
--> Key and Value are separated by ':'
--> Key should be Unique and it is immutable in nature.
--> Value can be anything and its mutable in nature
--> It is enclosed with {} curly braces.
--> We can get the value of the dictionary through dictionary key.

# Dictionary Methods:
clear() = removes all key-values pair from dictionary

Points:
--> Each key value pairs considered as element

'''
# Ex:

employee = {'name': 'Karthi', 'eid': 'MCS-0038', 3: 'Software Engineer',
            'address': 'Bangalore', 'salary': 25000}
# accessing the value:

print('Salary of the employee : ', employee['salary'])
print('Employee Id :', employee['eid'])
print(employee[3])

# Operation on Dictionaries:
# Knowing number of Key and Value pairs:

'''Use len() function to know the key value pairs'''

n = len(employee)
print('No.of Key value pairs :', n)

# To modify the existing value:

employee['salary'] = 32000
employee['name'] = 'Karthikeyan'
print('The modified salary :', employee['salary'])
print('The modified name :', employee['name'])

# To add the new key-value pair

employee['id'] = 38
print(employee)

# To delete Key-Value pair:

del employee['eid']
print('The Dictionary of Employee:', employee)

# To check whether key exist or not:(in, not in)

print('eid' in employee)
print(('eid' not in employee))
print('id' in employee)




''
# num = int(input('number'))
# for i in range(0, num):
#     for j in range(0, num):
#         if i == j:
#             a = i * j
#             print(a)










