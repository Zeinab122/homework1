#code1-A
def f(lis1,lis2):
    list=zip(lis1,lis2)
    d=dict(list)
    print('d=',d)
l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,443,21,53]
f(l1,l2)  

#code1-B
def f(i):
    if i ==0:
        return 1
    else:
        return i*f(i-1)
    
num=int(input("Enter number:"))
print(num,'! =',f(num))

#code1-C
def f(list):
    for i in range(len(list)):
        if list[i].startswith('B'):
            print(list[i])

            
l=['Network','Bio','Programming','Physics','Music']
f(l)

#code1-D
d={i:(i+1) for i in range(0,11)}
print(d)

#code 2
num=input("Enter binary number:")
intnum=list(map(int,num))
intnum=intnum[::-1]
n=0
for i in range(len(intnum)):
    x = intnum[i]*2**i
    n +=x
    
print("the decimal number=",n)

#code 3
import json

def test(data):
    s=0
    for j in data:
        print(j["Question"])
        an=input("Enter your answer:")
        if an == j["answer"]:
            s +=1
    return s
def results(name,s,file):
    result={"namr_user":name,"result_user":s}
    with open(file,"w") as f:
        json.dump(result,f)

def main(test_file,result_file):
    with open(test_file,"r") as f:
        d=json.load(f)
    print("welcome!")
    unam=input("Enter your name,please:")
    umark=test(d)
    print(f"your result:{umark}/20")
    results(unam,umark,result_file)
t_file="C:\\Users\\HP\\Desktop\\quize.json"
r_file="C:\\Users\\HP\\Desktop\\result.json"

main(t_file,r_file)

#code4
class BankAccount:
    def __init__ (self,account_number,account_holder,balance):
        #instance variables
        self._account_number=account_number
        self._account_holder=account_holder
        self.balance=balance
    def deposit(self,amount1):
        self.balance +=amount1
        return amount1
    def withdraw(self,amount2):
        self.balance -= amount2
        return amount2
    def get_balance(self):
        print(f"You have just used your bank account and the current balance after last operation is:",self.balance,"$")
Account1=BankAccount("125964","zeinabsa",0.0)
Account1.deposit(1000)
Account1.get_balance()
Account1.withdraw(500)
Account1.get_balance()
class Saving_Account(BankAccount):
    def __init__(self,account_number,account_holder,balance,interest_rate):
        super().__init__(account_number,account_holder,balance)
        self.interest_rate=interest_rate
    def apply_interest(self):
        interest=self.balance*self.interest_rate
        self.balance=+ interest
    def __str__(self):
        return (f"The current your balance is: {self.balance} $  and your interest rate= {self.interest_rate} %")
S_account=Saving_Account("756492","ahmad",650.0,15)
S_account.apply_interest()
print(S_account)
