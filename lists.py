# lists are mutable, we can access index and change values
# list of lists psbl, search it

friends = ['preet', 232, 'apples', 24.3, True]
print(friends)

friends[1] = 'lemons'
print(friends)  # ['preet', 'lemons', 'apples', 24.3, True] ---> MUTABLE

friends.append("pretty")  # pretty added
print(friends)

listt = [2,5,6,8,3,3,2,1,9]
print(listt)
print(sum(listt))

listt.sort()  # [1, 2, 2, 3, 3, 5, 6, 8, 9]
print(listt)  # sorts ascending (updatedlistt)

listt.reverse()  # [9, 8, 6, 5, 3, 3, 2, 2, 1]
print(listt)

# list.insert(index, value)
listt.insert(1,"preett") # inserts preet at 1st index
print(listt)    # [9, 'preett', 8, 6, 5, 3, 3, 2, 2, 1]

listt.pop(2) # pops 2nd index = 8
print(listt)  # [9, 'preett', 6, 5, 3, 3, 2, 2, 1]

listt.remove(3) # REMOVES THAT VALUE ONCE, NOT INDEX
print(listt)    # [9, 'preett', 6, 5, 3, 2, 2, 1]

listt.remove(3) 
print(listt)   # [9, 'preett', 6, 5, 2, 2, 1]


#return value of popped stuff, store in variable n can be used
# popped = listt.pop(0)
# print(popped)
print(listt.pop(0))  # prints the value that it pops = 9

