class Atm:
    def __init__(self, card_number, balance):
        self.card_number=card_number
        self.balance=balance
    def check_balance(self):
        print("your balance is ", self.balance)
    
    def withdraw(self):
        kfc=int(input("how much do you want to withdraw?"))

        self.balance=self.balance-kfc

        print("transaction success, you now have ",self.balance,"left in your account!")

def main():
    card_number=input("Insert your card number")
    user1=Atm(card_number,5000)
    user1.check_balance()
    user1.withdraw()


if __name__=="__main__":
    main()
    