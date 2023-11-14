#Q.1 Create a multi-level inheritance ,override default constructors in the child classes ,instantiate
# the child class and show how will u invoke parent class constructor from child class ?
"""
class vehicle:
    def __init__(self):
        print("Vehicles")
        
class Bus(vehicle):
    def __init__(self):
        super().__init__()
        print("Bus has 40 seats")
        
class Minibus(Bus):
    def __init__(self):
        super().__init__()
        print("Minibus has 20 seats")
        
m = Minibus() """


# Q.2 Create a class "Vehicle", define a method "start()" in it.
# From this class derive a class FourWheeler. How will you override "start()" method of parent class ?

"""
class Vehicle:
     def start(self):
         print("start Vehicle as parent")
         
class Fourwheeler(Vehicle):
    def start(self):
        super().start()
        print("start Fourwheeler as child")
        
f = Fourwheeler()
f.start()

"""

#Q3.Go for Hierarchical inheritance, create instances of child class and observe constructor invocation.

"""
class Base:
    def __init__(self):
        print("inside the Base class constructor")
class Sub1(Base):
    def __init__(self):
        print("inside the Sub1 class constructor")
        super().__init__()
    
class Sub2(Base):
    def __init__(self):
        print("inside the Sub2 class constructor")
        super().__init__()

Sub1_obj = Sub1()
Sub2_obj = Sub2()

"""

# Q.4 Create a class "Top1" with "disp1()" method.
# From this class Derive "Bottom1", "Bottom2" and "Bottom3" classes ,override the "disp1()".
# create a function "perform" which can take argument as object of any child class.
# Now show how will u achieve dynamic polymorphism.

"""
class Top1:
    def disp1(self):
        print("inside Top1")
class Bottom1(Top1):
    def disp1(self):
        print("inside Bottom1")
class Bottom2(Top1):
    def disp1(self):
        print("inside Bottom2")
class Bottom3(Top1):
    def disp1(self):
        print("inside Bottom3")

def perform(object): # dynamic Polymorphism
    object.disp1()
    
perform(Top1())
perform(Bottom1())
perform(Bottom2())
perform(Bottom3())

"""

#Q.5.create Base class and Sub class with parameterized constructors. Show how will you invoke Base class parameterized constructor from Sub class.

"""
class Base:
    def __init__(self,val):
        self.val = val
        print("inside the Base class constructor","\t",val)
class Sub(Base):
    def __init__(self,val):
        self.val = val
        super().__init__(val+50)
        print("inside the Sub Class Constructor","\t",val)

s1 = Sub(100)

    """
