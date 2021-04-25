import datetime 
import random
database={}
userdetails=[]
bank=[]
timenow=datetime.datetime.now()
def init():
	print("WELCOME TO ATBANK")
	haveAccount=int(input("Do you have an acount : 1 Yes  2 No\n"))
	if haveAccount==1:
		login()
	elif haveAccount==2:
		register()
	else:
		print("invalid option")
		init()
def register():
	email=input("Enter Email\n")
	fname=input("Enter your first name\n")
	lname=input("Enter last name\n")
	password1= input("Enter your password\n")
	password2=input("Confirm your password\n")
	if password1==password2:
		print("Successfully registered account")
		userdetails.append(fname)
		userdetails.append (lname)
		userdetails.append (email)
		userdetails.append(password2)
		print(userdetails)
		generateAccount()
	else:
		print("wrong password")
		register()
def generateAccount():
	accountnumber=random.randrange(3333000000,3333999999)
	print(f"Your account number is {accountnumber}")
	database[accountnumber]=userdetails
	print(database)
	login()
def login():
	accountNumbersfromuser=int(input("Enter account number\n"))
	passwordfromuser=input("Enter password\n")
	for accountnumber,userID in database.items():
		if accountNumbersfromuser==accountnumber:
			if passwordfromuser==userID[3]:
				bankoperation()
			else:
				print("wrong password")
				login()
		else:
				print("account number doesnt exist")
				login()
def bankoperation():
	print(f"Welcome {userdetails[0]} {userdetails[1]}    {timenow} ")
	selectedOption =int(input("what action do you want to perform,\n 1 deposit\n 2 withdrawal\n 3 transfer \n 4 check balance\n 5 logout\n"))
	if selectedOption ==1:
		deposit()
	elif selectedOption==2:
		withdrawal()
	elif selectedOption ==3:
		transfer()
	elif selectedOption==4:
		balancecheck()
	elif selectedOption ==5:
		logout=int(input("Are you sure you want to logout? 1 yes 2 no\n"))
		if logout==1:
			login()
		elif logout==2:
			auxiliary()
		else:
			print("invalid option")
			bankoperation()
def deposit():
	depositAmount= int(input("How much do you want to deposit \n"))
	bank.append(depositAmount)
	print("deposit successful")
	auxiliary()
def auxiliary():
	option=int(input("Do you want to perform another transaction? 1 yes 2 no\n"))
	if option ==1:
		bankoperation()
	elif option==2:
		print("Thanks for banking with us")
		login()
	else:
		auxiliary()
def withdrawal():
	withdrawnAmount=int(input("enter amount to be withdrawn:"))
	if withdrawnAmount <=sum(bank):
		amount=-withdrawnAmount
		bank.append(amount)
		print("take your cash")
		auxiliary()
	elif withdrawnAmount>sum(bank):
		print("insufficient funds")
		print("deposit some money")
		auxiliary()
	else:
		print("invalid amount")
def transfer():
	transferAmount = int(input("How much to be transfered "))
	if transferAmount<=sum(bank):
		amounttaken=-transferAmount 
		bank.append(amounttaken)
		receiver=int(input("enter account number\n"))
		print("Transaction complete")
		auxiliary()
	elif transferAmount>sum(bank):
		print("insufficient funds")
		auxiliary()
def balancecheck():
	print(f"your balance is {sum(bank)}")
	auxiliary()
init()