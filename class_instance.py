class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            self.age=0
            print("Age is not valid, setting age to 0.")
        else:
            self.age=initialAge
    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
         self.age+=1

t = int(input("Enter the number of test cases:"))
for i in range(0, t):
    age = int(input("Enter the age:"))         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()        
    p.amIOld()
    print("")
              