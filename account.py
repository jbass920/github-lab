class Account:
    def __init__(self, name: str) -> None:
        """
        Initializes a new account object with the specified name and a balance of zero.
        
        Args:
        - name (str): The name of the account holder.
        """
        self._name = name
        self._balance = 0
        
    def deposit(self, amount: float) -> bool:
        """
        Adds the specified amount to the account balance.
        
        Args:
        - amount (float): The amount to deposit.
        
        Returns:
        - True if the transaction is successful, False otherwise.
        """
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False
        
    def withdraw(self, amount: float) -> bool:
        """
        Subtracts the specified amount from the account balance.
        
        Args:
        - amount (float): The amount to withdraw.
        
        Returns:
        - True if the transaction is successful, False otherwise.
        """
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False
        
    def get_balance(self) -> float:
        """
        Returns the current account balance.
        """
        return self._balance
    
    def get_name(self) -> str:
        """
        Returns the name of the account holder.
        """
        return self._name
