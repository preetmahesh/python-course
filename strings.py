# Strings
name = "Preet"
name = 'preet'
name = '''Preet'''
print (len(name))

# Immutable (cant change single char of a string)

# 0 1 2 3 index ---- backwards last char is -1 -2 -3 -4


# Strings SLICING (picking single char slice from a string)
sliced = name[0:2] # Pr ---> 2 se pehle stopped. LAST ISNT INCLUDED
print(sliced)

sliced2 = name[0:3] # till 2nd index ---> Pre
print(sliced2)

print(name[0]) # prints 0th index element

# SLICING WITH SKIP
print(name[1: 5: 2]) # 1st index se 4th index tak go bec 5th isnt considered. 
                     # then 1 se print stuff every 2nd jump like P, r skip (1), e print bec 2nd
                    # so re will be printed here