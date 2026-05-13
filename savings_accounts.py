from main import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.intrest_rate= 0.02
        self.writhdraw_limit=100
        
        
    def apply_intrest(self):
        intrest= self.get_balance()*self.intrest_rate
        self.deposit(intrest)
        print(f"Intrest of ${intrest} applied. New balance: {self.get_balance()}")
        
    def writhdraw(self, amount):
        current_balance = self.get_balance()
        if amount <= current_balance and amount<= self.writhdraw_limit:
            return super().writhdraw(amount)
           
        else:
           print(f"Denied: Amount exceeds limit (${self.writhdraw_limit}) or insufficient funds.")
        
        
print("---Savings Account---")
savings= SavingsAccount("Alice",1000)
print(f"Inital balance:{savings.get_balance()}")
savings.deposit(500)
savings.writhdraw(40)
savings.writhdraw(200)
savings.apply_intrest()