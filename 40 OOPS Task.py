        # create a Axis bank class which will display id , bank name , roi , dept 

class Bank():

    def getdata(self , id, b_name, roi, dept):
        self.id = id
        self.b_name = b_name
        self.roi = roi
        self.dept = dept

    def display(self):
        print("Bank id is :- ", self.id)
        print("Bank name is :- ", self.b_name)
        print("Bank dept is :- ", self.dept)
        print("Bank Rate of Interest (roi) is :- ", self.roi)

s = Bank()

id = int(input("Enter Bank id :- "))
b_name = input("Enter the name of the Bank ")
dept = input("Enter the dept of the Bank ")
roi = input("Enter the Rate of Interest (roi) of the Bank ")

s.getdata(id,b_name,roi,dept)
s.display()
