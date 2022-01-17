def calc(a,b,c):
    sum=0
    thr=0
    

    if a==b==c:
        sum=a+b+c
        thr=sum*3

        print("sum is:",sum)
        print("Sum thirce is:",thr)
    else:
        sum=a+b+c
        print("The numbers are not equal")
        print("sum of the number:",sum)

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the last number:"))
calc(a,b,c)
