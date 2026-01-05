# mean
# median
# mode
arr=[1,2,3,4,5,6,7,8,9,10]



# print(sum(arr))
def mean(*arr):
    s=sum(arr)
    n=len(arr)
    print(s/n)

mean(10,20,30,40,4,50,3,3,4)
mean(10,20,30,40,50)

def median(*arr):
    arr,n=sorted(arr),len(arr)
    print((arr[(n//2)-1]+arr[(n//2)])//2 if n%2==0 else arr[(n)//2])

# "if answer" if condition else "else answer"

median(10,20,30)
median(10,30,20)

10