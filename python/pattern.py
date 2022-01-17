a=int(input("Enter the starting position:"))
b=int(input("Enter the ending position:"))
i=j=0
for i in range(a,b+1):
    for j in range(1,i+1):
        print("*",end = " ")
    print(" ")
