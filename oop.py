'''
# instance method vs class method vs static method
class Student:

    school = 'Atharva'
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.school

    @classmethod
    def getSchool(cls):
        cls.school = 'Thespia'class Student:

        return cls.school

    @staticmethod
    def info():
        print("This is Student class..in abc module")
         
    
s1 = Student(34, 67, 32)
s2 = Student(89, 32, 12)

#print(s1.getSchool())
print(Student.info())
'''
'''
# class in another class
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop('DELL', 'i7', 8)

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
        
    class Laptop:

        def __init__(self, name, cpu, ram):
            self.brand = name
            self.cpu = cpu
            self.ram = ram
            
        def show(self):
            print(self.brand, self.cpu, self.ram)
s1 = Student('Sourav', 15)
s2 = Student('Modric', 10)

s1.show()

#lap1 = s1.lap('DELL', 'i7', 8)
lap2 = s2.Laptop('HP', 'i5', 8)


print(id(lap2))

'''
'''
# inheritance
class A:
    def feature1(self):
        print('Feature 1 working')

    def feature2(self):
        print('Feature 2 working')

class B():
    def feature3(self):
        print('Feature 3 working')

    def feature4(self):
        print('Feature 4 working')

class C(A,B):
    def feature5(self):
        print('Feature 5 working')

    def feature6(self):
        print('Feature 6 working')

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b2 = B()

c1 = C()

'''
'''
# constructor in inheritance
class A:

    def __init__(self):
        print('in A init')
    
    def feature1(self):
        print('Feature 1-a working')

    def feature2(self):
        print('Feature 2 working')

class B:
    def __init__(self):
        print('in B init')
        
    def feature1(self):
        print('Feature 1-b working')

    def feature4(self):
        print('Feature 4 working')

class C(A,B):

    def __init__(self):
        super().__init__()
        print('in C init')

        

b1 = C()
b1.feature1()
'''
'''
# polymorphism(Duck Typing)

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self, ide):
        ide.execute()
     
lap1 = Laptop()
ide = MyEditor()
lap1.code(ide)
'''

# operator overloading

a = '5'

b = '6'


print(str.__add__(a,b))

print(a+b)
