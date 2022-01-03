a=list(input("Enter the string:"))
for i in a:
    if i!="#":
        c=0
        for j in range(0,len(a)):
            if i==a[j]:
             c=c+1
             a[j]="#"
        print(i,"=",c)
