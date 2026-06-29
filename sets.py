# collection of well defined objects
# (NON REPETIITVE ELEMENTS)
# if people input multiple stuff again n again, it helps to store unique elemets

s = {2,4,5,3,4,5,2,1,3}  #  (UNORDERED for order use a list)
print(s) # {1, 2, 3, 4, 5} once every element

# s = {1, 5, 20} # a set, dict brackets but no key pairs
# s = {} NOT AN EMPTY SET, ITS EMPTY DICT

a = set() # empty  set
print(type(a))  #class set


# SET FUNCTIONS

s = {"preet", 2, 2,23,4,1} #valid

s.add(290) # adds this in the set
print(s)

# s.add(2) # already added in the set
# print(s)

s.remove(2) # {1, 290, 4, 23, 'preet'}
print(s) # removes 2 from set

s1 = {1 ,2, 3}
s2 = {2, 3, 5, 6, 7}

print(s1.union(s2)) # combine both the sets, dont repeat
 # {1, 2, 3, 5, 6, 7}

s1.union(s2)
print(s1)  # {1, 2, 3} DOESNT CHANGE S1

print(s1.intersection(s2)) # {2, 3} is common

a = set()
a.add(20)
a.add(20.0)
a.add('20')
 # LENGTH OF SET HERE IS 2, BEC 20.0 AND 20 ARE SAME NUMERICALLY 
 # BUT 20 AND "20" ARE DIFF
print(len(a)) # 2