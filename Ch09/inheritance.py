
#--------Ch03 Lab 2 Inheritance------------#
class Customer:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"Customer id #{self.id}: {self.name}")

c = Customer('Frank',111)
c.print_info