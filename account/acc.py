class Account: # class

    def __init__(self,filepath):
        self.filepath=filepath # instance variable
        with open(filepath,'r') as file:
            self.balance=int(file.read())
    
    def withdraw(self,amount):
        self.balance=self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount
        
   
    def commit(self): 
        with open(self.filepath,'w') as file:
            file.write(str(self.balance)) 
        

class Checking(Account): #inheritance

    """This class generates checking account objects""" #doc string
    type="checking" #class vaiable
      
    def __init__(self,filepath, fee): #Constructor : init function ,it also special method
        Account.__init__(self,filepath) # Instantiation:process of creating object instance so instance of class like 'jack_checking=Checking("jack.txt",1)' this is instantiation of class
        self.fee=fee                     #Data member : are basically class variable or instance variable

    def transfer(self,amount): # Methods : apply on object instance ex. transfer
        self.balance=self.balance - amount - self.fee   

jack_checking=Checking("jack.txt",1) #object instance
# checking.deposit(20)
jack_checking.transfer(100)
print(jack_checking.balance) # attributes ex. balance,type
jack_checking.commit()

john_checking=Checking("john.txt",1)
# checking.deposit(20)
john_checking.transfer(100)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)

print(john_checking.__doc__)




# account=Account("balance.txt")
# print(account.balance)  
# account.deposit(2000)
# account.withdraw(100)
# print(account.balance)
# account.commit()

