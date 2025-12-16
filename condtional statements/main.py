# condtional statements : these are block of codes which are 
#                          going to be executed only when the condition is satisfied
# types of statements
# if :- when ever the if condition gets True  Value then it will entire the block
# syntax:
    # if condition:True
        # block of code

# else : whenever the previouse condition gets False this block will execute
#elif : when a previouse condition gets False and current condition gets True then the block will exc
age=2
print("general code")
if age>=18:#False
    print("he is eligible") 
else:
    print("he is not eligibile")
print("general code")


# check whether the given number is even or odd
# num%2==0 even
# num%2!=0 odd
num=9

if num%2==0: # only one block
    print("Even")
else:
    print("Odd")


if num%2!=0:
    print("Odd")
else:
    print("Even")



# pos,neg,zero more than 2 
# pos >0
#pos <0
# pos ==0
num=0
if num>0:#False
    print("pos")
elif num<0:# False
    print("neg")
else:
    print("zero")




# wap if the number is div of 2 print foo,
# if a num is div of 3 print boo and if it is div of both print fooboo

num=6
if num%2==0 and num%3==0 :#True
    print("fooboo")
elif num%3==0:
    print('boo')
elif num%2==0:
    print('foo')




# print("Welcome to Election Day")# running
# age=10# ini
# if age>=18:#False
#     print("he is eligible")
# print("Thank You for u r vote")