#==========================================================================================================
                                        # TYPES OF INHERITANCE
#==========================================================================================================
'''
THERE ARE 5 TYPES OF INHERITANCE:-
    1. single inheritance
    2. multilevel inheritance
    3. heirarchical inheritance
    4. multiple inheritance
    5. hybrid inheritance
'''
#----------------------------------------------------------------------------------------------------------
                            # 1. SINGLE INHERITANCE
#----------------------------------------------------------------------------------------------------------

# Program 43 is also an example of single inheritance 

#superclass
class Employee():
    def getdata(self,id,name,age,salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
    def details(self):
        print("The ID of the employee is ",self.id)
        print("The name of the employee is ",self.name)
        print("The age of the employee is ",self.age)
        print("The salary of the employee is ",self.salary)

# Subclass
class Bonus(Employee):
    def get_Bonus(self,bonus):
        self.bonus = bonus 
        print("The Bonus recieved is ",self.bonus)

# Accessing data of Superclass
print("******* Employee Details *******")
e = Employee()
e.getdata(100,"Yash Katkar",22,87000)
e.details()

# Accessing data of Subclass
print("******* Bonus Details *******")
b = Bonus()
b.getdata(200,"Vishal Mourya",21,87000)
b.details()
b.get_Bonus(35000)

