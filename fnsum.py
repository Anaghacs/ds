def sumfn(x):
    sum=0
    while(x>0):
        l=x%10
        sum=sum+l
        x=x//10
    return(sum)


x=int(input("Enter the number:"))
sum=sumfn(x)
print("sum is=",sum)
