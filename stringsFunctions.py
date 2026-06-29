name = 'preeeetmahesh'

print(name.endswith('hesh')) # variable.endswith("blahblah") prints T or F for that string
print(name.endswith('heshaa'))  # False

print(name.startswith('pree'))  # false if P capital

print(name.capitalize())  # makes P capital

capital = name.capitalize()  

print(capital.startswith('Pree'))

# str.find("word")  finds that word in the entire string at index wtv

poem = '''tha ha rainl rain go ha ha rain ha'''

print(poem.find('rain'))


#str.replace(old word, new word) # replaces all old words with new
s = 'hello world world'
print(s.replace("world", "preet"))

print(s.split()) #splits the string into a list literally

# print("she likes beautiful pictures") we cant print inverted commas using ""
# we use backslash

print("she likes \"beautiful\" pictures")  