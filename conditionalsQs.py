#write program to find greatest of four numbers entered by user

num1 = int(input("Input number 1: "))
num2 = int(input("Input number 2: "))
num3 = int(input("Input number 3: "))
num4 = int(input("Input number 4: "))

# if (num1 > num2):
#     max = num1
#     if(num1> num3):
#         max = num1
#         if (num1 > num4):
#             max = num1
#         else:
#             max = num4
#     elif(num3 > num1):
#         max = num3
#         if(num3 > num4):
#             max = num3
#         else:
#             max = num4
            
            # STUPID, we couldve used logic operators (use AND)

if(num1> num2 and num1 > num3 and num1 > num4):
    print(f"{num1} is greatestt")

elif(num2> num1 and num2 > num3 and num2 > num4):
    print(f"{num2} is greatestt")

elif(num3> num1 and num3 > num2 and num3 > num4):
    print(f"{num3} is greatestt")

else:
    print(f"{num4} is greatestt")

# -----------------------------------check for spam now
    
p1 = "buy this"
p2 = "make a lot of money"
p3 = "subscribe now"
p4 = "click this"

message = input("Enter your message: ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("\"",message, "\" is a spam text!")
