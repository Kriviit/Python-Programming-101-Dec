# print from one to 10
# DRY donot repeat yourself

#syntax
# def <function name>(): function declarition
#     block


# concepts of function
    # function decl
    # function calling
    # function address

#parameter/arguments=> these are present inside the paranthesis
# <functonname>()=>calling the function


# waf to add two nums

def add(a,b):
    print(a+b)

def check_even_odd(num):
    if num%2==0:
        print('even')
    else:
        print('odd')


def get_max_two_number(num1,num2):
    if num1>num2:
        print('num1 is greather num2 ',num1)
    elif num1<num2:
        print('num2 is greather num1 ',num2)
    else:
        print('both num2 and num1 are equal ',num2)




def print_n_natural_number(n):
    i=1
    while(i<=n):# 1.....10
        print(i)
        i+=1

# print_n_natural_number(10)
# print_n_natural_number(100)

# check whethe the given number is even or not => 

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(11))

# get_max_two_number(10,20)
# get_max_two_number(110,320)
# get_max_two_number(-110,0)
# get_max_two_number(-110,-110)
# check_even_odd(10)
# check_even_odd(11)
# check_even_odd(12)