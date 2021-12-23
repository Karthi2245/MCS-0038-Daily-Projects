# Remove duplicate items from dict

'''
Topics:
--------
--> Operators
--> DM and Loops
--> Data structure
--> Crud Operations(retrieval)

# Take the string
# Remove the odd position of the string
# Write the New string in White paper
'''
# 1.Builtin functions
print("-----1. Built Functions--------")

# 2. Algorithm:
print("-----1. Algorithm--------")
student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
        # add the dictionary key value pair into empty dictionary

print(result)


# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def duplicate():
    student_data = {'id1':
                        {'name': ['Sara'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    'id2':
                        {'name': ['David'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    'id3':
                        {'name': ['Sara'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    'id4':
                        {'name': ['Surya'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    }

    result = {}

    for key, value in student_data.items():
        if value not in result.values():
            result[key] = value
            # add the dictionary key value pair into empty dictionary

    return result


obj = duplicate()
print(obj)


# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
class Duplicate:

    def duplictaes(self):
        student_data = {'id1':
                            {'name': ['Sara'],
                             'class': ['V'],
                             'subject_integration': ['english, math, science']
                             },
                        'id2':
                            {'name': ['David'],
                             'class': ['V'],
                             'subject_integration': ['english, math, science']
                             },
                        'id3':
                            {'name': ['Sara'],
                             'class': ['V'],
                             'subject_integration': ['english, math, science']
                             },
                        'id4':
                            {'name': ['Surya'],
                             'class': ['V'],
                             'subject_integration': ['english, math, science']
                             },
                        }

        result = {}

        for key, value in student_data.items():
            if value not in result.values():
                result[key] = value
                # add the dictionary key value pair into empty dictionary

        print(result)

obj = Duplicate()
obj.duplictaes()



# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")

'''a='KIRAN kar'
b='KIRAN kar'
c='KARAN'
print(id(a),id(b),id(c))'''


