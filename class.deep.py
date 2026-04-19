'''
1) encapsulation 
2) inheritance 
3) polymorfism

'''

# encapsulation   ->   public , __private , _protected 

class bankAccount:
    description = 'this class make bank account'

    def __init__(self, owner , amount):
        self.__owner = owner
        self.__amount = amount

    def checkBalance(self):
        print(f"{self.__owner} balance is {self.__amount} usd")

    def deposit(self , amount):
        print(f"* deposit : {amount} usd *")
        self.__amount += amount
        
    def withdraw(self , withdraw):
        print(f"you withraw {withdraw} usd from your balancne")
        self.__amount -= withdraw
    
    @property 
    def holder(self):
        return self.__owner
    
    @holder.setter 

    def holder(self, new_owner):
        self.__owner = new_owner 
        print(f"account owner is changed to {self.__owner}")


    def new_owner(self , new_ownner):
        self.__owner = new_ownner
        print(f"account owner is changed to {self.__owner}")


person = bankAccount('jone' , 1000)

# person.checkBalance()

# person.deposit(2500)
# person.checkBalance()
# person.withdraw(4000)
# person.checkBalance()

# person.owner = 'umar'
# person.checkBalance() 



# try:
#     result = bankAccount.__amount
#     print(f"Current balance: {result}")
# except Exception as err:
#     print(f"Error occurred: {err}")


#account_owner = person.holder     #  getter state 
#print(f"account owner : {account_owner})
print(f"before change owner : {person.holder}")

#person.new_owner('umar')
#person.checkBalance()
person.holder = 'umar'   # setter state

print(f"after change owner is : {person.holder}")