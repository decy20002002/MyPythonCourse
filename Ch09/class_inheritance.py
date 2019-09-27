
class Parent:
    def __init__(self, last_name):
        self.last_name = last_name
    
    def print_info(self):
        print('I am in the ' + self.last_name + ' family')

class Child(Parent):
    pass #use pass if dont want any new properties
    
mom = Parent('Smith')
mom.print_info()

#--------Ch03 Lab 2 Inheritance------------#
class Customer:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"Customer id #{self.id}: {self.name}")

c = Customer('Frank',111)
c.print_info