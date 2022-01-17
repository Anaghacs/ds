a=int(input("Enter the number:"))
s=i=j=0
for i in range(1,a+1):
    for j in range(1,i+1):
        s=j*i
        print(s,end=" ")
    print(" ") 
