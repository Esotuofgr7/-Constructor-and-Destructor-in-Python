class Employee:
    
    # Initializing (Constructor)
    def __init__(self):
        print('Employee Created')

    # Deleting (Destructor)
    def __del__(self):
        print('Destructor Called, Employee Deleted')

# Create an instance of the class
obj = Employee()

# Delete the object
del obj
