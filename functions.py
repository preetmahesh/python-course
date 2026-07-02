# block/group of statements that perform a specific task
# function can be used again n again to perform that task (unlike loops (they cant be called again n again))
# there should be no redundancy

# instead of taking 2 numbers and wriitng sum formula again n again
# we use one sum formula wth parameters in definition, and pass arguments when calling the func 

# 1- Built in function
# 2- User defined function

def calc_sum(a, b):  # we will pass the vlaues later when called
    sum = a + b
    print(sum)
    return sum  # so if sum is used kahin aur, comp knows the sum value stored

calc_sum(3,3)
calc_sum(5,5)
calc_sum(4,4)

def print_hello():
    print("Hello") # no parameters, no return value so no output.
    # if i store the output of this fun in some variable, it will give none

print_hello()  # Hello

output = print_hello()
print(output)  # gives None

def converter(usd_value):
    pkr_value = usd_value * 278.12
    print(f"{usd_value} USD = {pkr_value} PKR")

converter(1)
converter(100)

def calc_fact(n):  # pass n, we calculate n's fact
    fact = 1
    for i in range(1, n+1): # 1! * 2! * 3! * 4! # n = 4, multiplies each i
        fact = fact * i 
    print(fact)

calc_fact(5)
calc_fact(3)

def print_list(list):  # not list like [], we print each item, we want in one line so we use end = " ", that ends each iteration with spaces and not a line
    for i in list: # for each item in list, print it, loop next, print again, move next 
        print(i, end = " ")
    print() # so next print can change line

nums = [3 ,2,3,6,7,8,7]
cars = ["sportage", "LC", "Porsche 911", "Yaris"]

print_list(nums)
print_list(cars)

def odd_even(n):
    if(n % 2 == 0):
        print(f"{n} is EVEN")
    else:
        print(f"{n} is ODD")

odd_even(5)
odd_even(6)