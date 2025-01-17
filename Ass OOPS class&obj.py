#1
'''
class Demo:
    value="variable"
    
    def __init__(self, no1, no2):
        self.no1 =no1
        self.no2=no2
    
    #instance method Fun
    def Fun(self):
        print(f"Inside Fun: no1 = {self.no1}, no2 = {self.no2}")
    
    # Instance method Gun
    def Gun(self):
        print(f"Inside Gun: no1 = {self.no1}, no2 = {self.no2}")

# Create objects
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Call instance methods
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
'''
#2
'''class Bookstore:
    
    #class variable
    bookcount =0
    def __init__(self,name,author):
        self.name = name
        self.author = author
        
        Bookstore.bookcount += 1
    def Display(self):
        print(self.name ," by ",self.author , "No of books:", Bookstore.bookcount)
        
Obj1=Bookstore('Linux System Programming','Robert Love')
Obj1.Display()  # Linux System Programming. No of books : 1
Obj2=Bookstore('C Programming','Dennis Ritchie')
Obj2.Display()  # C Programming by Dennis Ritchie. No of books :2
'''
#3
'''
class circle:
    #class variable
    pi = 3.14
    def __init__(self):
        #instance variable 
        self.radius = 0
        self.area =0
        self.circumference= 0
    def accept(self):
        self.radius = int(input("enter ther radius: "))
    def calarea(self):
        self.area = circle.pi *self.radius**2
    def circum(self):
        self.circumference = 2*circle.pi*self.radius
    def display(self):
        print(self.radius)
        print(self.area)
        print(self.circumference)

circle1 = circle()
circle1.accept()
circle1.calarea()
circle1.circum()
circle1.display()
'''
#4
'''
class bankacc:
    roi = 10.5
    def __init__(self,name,amt):
        self.name = name
        self.amt = amt
    def deposit(self,amt):
        self.amt +=amt
    def withdrawl(self,amt):
        if amt<=self.amt:
            self.amt -= amt
        else:
            print("no sufficient balance in your account")
    def calintrest(self):
        intrest = (self.amt / bankacc.roi) *100-self.amt
        print(" intrest :", intrest)
    def display(self):
        print("Name:",self.name,"balance is ", self.amt,  )
        
obj=bankacc("surya",1500)
obj.deposit(2000)
obj.withdrawl(1500)
obj.calintrest()
obj.display()
'''
#5
'''
class number:
    value = 0
    def __init__(self,value):
        number.value =value

    def chkprime(self):
        for i in range(2,int(self.value**0.5)+1):
            if self.value%i==0:
                return False
        return True


    def chkperfect(self):
        sum_val=1+self.value
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                sum_val+=i
        if(sum_val==self.value):
            return True
        return False
        
    def factor(self):
        factor =[1]
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                factor.append(i)
        factor.append(self.value)
        return factor
        
    def sumfactors(self):
        sum_val=1+self.value
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                sum_val+=i
        return sum_val
        
obj=number(10)
print(obj.chkperfect())
print(obj.chkprime())
print(obj.sumfactors())
print(obj.factor())
'''
#6
class Number2():
    def __init__(self):
        self.val1=0
        self.val2=0
    def Accept(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def Addition(self):
        return self.val1+self.val2
    def Subraction(self):
        return self.val1-self.val2
    def Multiplication(self):
        return self.val1*self.val2
    def Division(self):
        return self.val1/self.val2
obj=Number2()
obj.Accept(8,3)
print(obj.Addition())
print(obj.Subraction())
print(obj.Multiplication())
print(obj.Division())
