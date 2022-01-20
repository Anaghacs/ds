l1=[0,9,3,50]
l2=[78,5,2,10]
print(l1)
print(l2)
c=0
if(len(l1)==len(l2)):
    print("number of elements in both list are equal")
else:
    print("Sum of the elements in list 1:",sum(l1))
    print("sum of the elemnets in list 2:",sum(l2))
if sum(l1)==sum(l2):
    print("sum of the elements in both lists are equal")
else:
    print("sum of the elements in both lists are not equal")
for i in l1:
          for j in l2:
              if i==j:
                  c=c+1
                  print(i)
if c==0:
          print("common elements does not exit")
else:
          print("number of common elements",c)
