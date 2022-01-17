n=int(input("Enter the number:"))
rev=0
temp=n
while(temp>0):
     d=temp%10
     rev=(rev*10)+d
     temp=temp//10
if(rev==n):
        print("The number is a palindrome")
else:
        print("The number is not palindrome")


        
