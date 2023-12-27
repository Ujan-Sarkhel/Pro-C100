class Atm():
    def __init__(self, card_num, atm_pin):
        self.card_num = card_num
        self.atm_pin = atm_pin
    def CashWithdrawal(self):
        x = input("Type the amount of money to be withdrawn")
        print(x, "money has been withdrawn")
    def BalanceEnquiry(self):
        print("10000/- is in your bank account")
    def details(self):
        print("Your ATM Card Number is:-"+str(self.card_num))
        print("YOUR ATM PIN number is:- "+str(self.atm_pin))

obj1 = Atm(92384792873348, 12862)
obj1.details()
obj1.CashWithdrawal()
obj1.BalanceEnquiry()
