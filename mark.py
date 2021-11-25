a=int(input("Enter the first subject mark:"))
b=int(input("Enter the second subject mark:"))
c=int(input("Enter the third subject mark:"))
d=int(input("Enter the fourth subject mark:"))
e=int(input("enter the fifth subject mark:"))
total=a+b+c+d+e
print("The total mark is :",total)
avg=total/5
print("The avarage=",avg)
if avg<=80:
         print("A grade")
elif avg<=50:
         print("B grade")
elif avg<=40:
         print("C grade")
    
else:
        print("Failure")
    
          
