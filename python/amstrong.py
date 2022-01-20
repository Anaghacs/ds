def amstrong(sum):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(num,"is an amstrong number")
    else:
        print(num,"this number is not armstrong number")
    return(num)


num=int(input("Enter the number:"))
amstrong(sum)
