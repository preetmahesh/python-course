# just like lists, theyre just immutable(jese strings)
# if u do changes in tuples, original tuple wont be chnaged, NEW TUPLE MADE (list changes)
# however elemnts of tuples cant be changes like strings, functions used only 


a = (1,3,4,5)
print(type(a))  # ()brackets for tuples, [] brackets for list

a = () # empty tuple+
print(type(a)) 

a = (1) # int, it doesnt store 1 element in tuple like this'
print(type(a)) 

a = (1,) # now it knows its a tuple
print(type(a)) 

a = (1,3,4,5, 3)
# a[0] = 5 GIVES ERROR

counting = a.count(3) # counts how many times 3 is there in tuple
print(counting) # 2 times its there

print(a.index(3))  # index where 3 is found first

# concatenation of tuples psbl too
tuple1 = (1,2,3,4)
tuple2 = (4,3,2,1)
concatee = tuple1 + tuple2
print(concatee)  # (1, 2, 3, 4, 4, 3, 2, 1)

fruits = [] # made a list
f1 = input("Enter fruit name: ")
fruits.append(f1)  # chipka the input to list
f2 = input("Enter fruit name: ")
fruits.append(f2)
f1 = input("Enter fruit name: ")
fruits.append(f1)
f1 = input("Enter fruit name: ")
fruits.append(f1)
f1 = input("Enter fruit name: ")
fruits.append(f1)

print(fruits)

