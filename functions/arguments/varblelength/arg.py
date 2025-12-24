# varable length:-these is like a collection/Data structure which can store n no elements
# *args=> takes n no required arguments
# def add(a,b):# vanshika
#     print(a+b)

def add(*args):
    s=0 # sum of all the elements
    for i in args:
        s+=i
    print(s)
    print(args)# tuple



#mahender use this function with 5 params
add(10,20,30,40,50)
#harish use this function with 3 params
add(10,20,30)



#kavya use this function with 10 params
add(10,20,30,40,50,60,70,80,90,100)


