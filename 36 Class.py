#===================================================================================================================================
                                                #  CLASS
#===================================================================================================================================

class Employee():         # define class 
    e_id = 100
    e_name = "Max"            # (class object / members ) or data members or attributes 
    salary = 98000
    address = "Mumbai"

e = Employee()

print("The ID of the employee is :- ", Employee().e_id)
print("The name of the employee is :- ", Employee().e_name)
print("The salary of the employee is :- ", e.salary)
print("The address of the employee is :- ", e.address)