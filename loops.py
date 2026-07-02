# for loop
# while loop


for i in range(1, 6):  # 1 se 5 tak, just like slicing
    print(i)   # print value of i, then i++ till i doesnt become 5

# i = 2
# while(condition):  # checks the condition first, if condition is true, the body is excuted
#     functions to perform
    
i = 1
while(i < 6):
    print(i)
    i += 1 # i++

# program to print content of a list
    
l = ["preeet", "aaaalu", 3, 43 , 43]

i = 0
while(i < len(l)):
    print(l[i])
    i += 1

for i in l:
    print(i)  # for each item in list, print it
# --------------------
for i in range(4):    # it assumes range(0,4) ---> 0 till 3 it goes (0 till n-1)
    print(i)  # 0, 1, 2, 3

for i in range(0, 100, 4):
    print(i)  # START, STOP, STEP SIZE (number of jumps to skipp)


#----BREAK for abrupt halt
    
for i in range(100):
    if(i == 34):
        break  # if i is 34, stop da loop (33 pe pa bec print is baad mein)
    print(i) # 0 till 99
    
#------CONTINUE
    
for i in range(100):
    if(i == 34):
        continue  # if i is 34, skipppp this iteration, continue agayy # 31, 32,33,35
    print(i) # 0 till 99

#-----PASS
# basiclly null statemnt in ptyhon, if u use pass in body of for loop, it ignores the for loop and does nothing and moves on agay

    