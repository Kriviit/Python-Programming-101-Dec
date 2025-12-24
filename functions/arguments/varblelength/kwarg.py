# varable length:-these is like a collection/Data structure which can store n no elements
# **kwargs=> takes n no keyword arguments
# def add(a,b):# vanshika
#     print(a+b)


def student(**kwarg):
    print(kwarg)


# mahender only name,age
student(name="mahender",age=30)
# vanshika name,age,rollno
student(name="vanshika",age=30,rollno=23)
# harish name ,age,rollo,bus
student(name="harish",age=30,rollno=23,bus="uppal")

