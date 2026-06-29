marks = {
"preet": 100, #name mapped to its marks (extra info)
"jia": 90, 
"kit": 32,
"list": ["apple", "mango"]
}

print(marks.items()) # gives us dict in form of tuples 
# dict_items([('preet', 100), ('jia', 90), ('kit', 32), ('list', ['apple', 'mango'])])
# we can iterate it using for loops now

print(marks.keys()) #gives all keys we can iterate
# dict_keys(['preet', 'jia', 'kit', 'list'])

print(marks.values()) # dict_values([100, 90, 32, ['apple', 'mango']])

# bec dict is mutable, original would be changed w updates
marks.update({"preet": 50})

print(marks) # {'preet': 50, 'jia': 90, 'kit': 32, 'list': ['apple', 'mango']}
# if u update stuff whihc isnt there, it will be added end mein 

marks.update({"preet": 60, "cutu": 34})
print(marks) # {'preet': 60, 'jia': 90, 'kit': 32, 'list': ['apple', 'mango'], 'cutu': 34}

# marks.get("preet") # gives value of preet
# marks["preet"] #also gives value of preet

# but when used for keys not in the dict, they return diff output
# marks.get("pretttty") # gives NONE bec no value is there for this nonexistent key
# marks["pretttty"] # returns an error bec it cant find that key, get GETS a value, beshak none. direct indexing throws error

marks2 = marks.copy()

d = {} # pehle empty
# take name, and lang, add in dict
name = input("enter name: ")
lang = input("enter lang: ")

d.update({name: lang})

name = input("enter name: ")
lang = input("enter lang: ")

d.update({name: lang})

name = input("enter name: ")
lang = input("enter lang: ")

d.update({name: lang})

print(d)

# {'Preet': 'english', 'jia': 'c++', 'jiaa': 'french'} 