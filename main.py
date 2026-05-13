class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited ${amount}. New balance ${self.__balance}")
        else:
            print("Deposit amount must be positive ")
    def writhdraw(self,amount):
        if amount<= self.__balance:
            self.__balance -= amount
            print(f"Whritdrawal of ${amount} successful. New balance is ${self.__balance}")
        else:
            print("Insufficient funds or Invalid writhdrawal amount")
    def get_balance(self):
        return self.__balance        
        