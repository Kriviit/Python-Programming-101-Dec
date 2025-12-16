num1,num2,num3=220,120,120
# num1> num2 and num1>num3 ==> num1
# num2> num1 and num2>num3 ==> num2
# num3> num1 and num3>num2 ==> num3
# num3==num1 and num3==num2 ==> equal

if num1>num2 and num1>num3:
    print("Num1 is greather")
elif num2>num3 and num2>num1:
    print("Num2 is greather")
elif num3>num1 and num3>num2:
    print("Num3 is greather")
elif num1==num2 and num2==num3:
    print("equal")

