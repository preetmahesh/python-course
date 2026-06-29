# also used to store
# key value pairs (can name mapped paired to its marks) 
# basically list of key value pairs
# used for lookup search directly

'''
It is unordered
It is mutable
it is indexed (directly looks up the key)
CAN NOT CONTAIN DUPLICATE KEYS
'''
# dict = {
#  "dictionary": "sds"
# }

# d = {} # empty dict

marks = {
"preet": 100, #name mapped to its marks (extra info)
"jia": 90, 
"kit": 32,
"list": ["apple", "mango"]
}

print(marks, type(marks))
# {'preet': 100, 'jia': 90, 'kit': 32} 
# <class 'dict'>  

# CAN NOT INDEX THE DICT AS 0 1 2 
# HOWEVER WE CAN SEARCH KEY AND FIND ITS PAIRED VALUE

# print(marks[0]) wrong

print(marks["preet"])  # 100
print(marks["list"])  