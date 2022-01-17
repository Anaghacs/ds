a=int(input("Enter the number:"))
i=1
count=0
while(i<=a):
    if(a%i==0):
        
        count=count+1
    i=i+1
if(count==2):

    print("It is a prime number")
else:
    print("It is not prime number")
