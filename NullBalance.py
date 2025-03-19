class NullBalance:
    def __init__(self, name):
        self.name = name
        self.value = None
    

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
        
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("qiymat 0 dan katta bolishi kerak")
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        del instance.__dict__[self.name]


class BankAccount:
    balance = NullBalance('balance')

customer = BankAccount()
customer.balance = 75
print(customer.balance)
