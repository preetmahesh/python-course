# if else, elif (if condition, then we do action)
# there can be multiple if statemts (independent too) + multiple elifs toooo

age = int(input("Enter your age: ")) # int converts str to int (typecasting)

if(age >= 18):
    print("wow youre a big kid!")
    name = input("pls enter ur name: ")
    print(f"hi {age} year old {name}")

elif(age<=0):
    print("invalid age, pls grow up")

else:
    print("boooo! youre still a kid!")