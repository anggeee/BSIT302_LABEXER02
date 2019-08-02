
data = True
my_empty = []

    
while data:
    class Employees:

        def __init__(self, name,department, position,rate):

            self.name = name
            self.department = department
            self.position = position
            self.rate = rate
    
        choices = ("""
            EMPLOYEE MANAGEMENT SYSTEM BY: ANGGE

             [1] Add new Employee
             [2] Add Hourly Rate
             [3] Show Employee Information
             [4] Exit

              ****************************
             """)
        print(choices)
    
    num = (input("Enter a  number: "))

    if num == "1":
        name = (input("Enter Employee Name: "))
        department = (input("Enter Employee Department: "))
        position = (input("Enter Employee Postion: "))
        rate = int(input("Enter Employee Rate: "))
        
        options = Employees(name, department, position, rate)
        my_empty.append(options)
        
        
    elif num == "2":
        for x in my_empty:
            print("Employee Number:")
            print(my_empty.index(x))
            
        hours = int(input("Enter Employee Hours: "))
        print("Employee Salary for ", hours , " hours is " , rate * hours)
           
        
    elif num == "3":
            print("Enter Employee Name: " + name)
            print("Enter Employee Department: " + department)
            print("Enter Employee Position: " + position)
            print("Enter Employee Rate: " + str(rate))

    elif  num == "4":
        data = False
        print("EXITED")
    else:
        data = False
        print("Invalid Choice, Please Try Again")
    
    





        

        

    
