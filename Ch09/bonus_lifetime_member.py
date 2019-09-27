class Customer:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"Customer id: {self.id}. {self.name}")

#c = Customer('Frank',111)
#c.print_info()

class PrimeCustomer(Customer):
    def __init__(self, name, id, expiration):
        super().__init__(name, id)
        self.expiration = expiration

    def print_info(self):
        print(f"Prime membership expires {self.expiration} ", end="")
        super().print_info()
p = PrimeCustomer("Betty", 222, "12.15.2021")
p.print_info()