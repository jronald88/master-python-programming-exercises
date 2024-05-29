# Your code here
class InputOutString():
    def __init__(self): #class method to initialize parameters
        self.s = ""

    def get_string(self):
        self.s = input("Please enter your string: ")

    def print_string(self):
        print(self.s.upper())

#create an instance of the class
obj = InputOutString()

#call get_string method
obj.get_string()

#call print_string
obj.print_string()
