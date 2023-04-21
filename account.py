class Account:
    def __init__(self, name):
        self._name = name
        self._balance = 0
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False
        
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False
        
    def get_balance(self):
        return self._balance
    
    def get_name(self):
        return self._name

    