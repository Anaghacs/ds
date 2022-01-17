def neon1(num):
    sqr=num*num
    sum=0
    while sqr>0:
        sum=sum+sqr%10
        sqr=sqr//10
    if(num==sum):
        print("It is an neon number")
    else:
        print("It is not an neon number")
            

num=int(input("Enter the number:"))
neon1(num)
