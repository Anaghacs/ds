a=int(input("Enter the 1 st number:"))
b=int(input("Enter the 2 nd number:"))
while(a<=b):
    c=0
    i=1
    while(i<=a):
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        print(a)
    a=a+1
    
