class reactangle:
    def __init__(self,length,breadth):
      self.length=length
      self.breadth=breadth
    def area(self):
      return (self.length*self.breadth)
    def perimeter(self):
      return(2*(self.length+self.breadth))
leng=int(input("Enter the length of the reactangle:"))
br=int(input("Enter the breadth of reactangle:"))
rect1=reactangle(leng,br)
print("Area =",rect1.area())
print("perimeter =",rect1.perimeter())

    
