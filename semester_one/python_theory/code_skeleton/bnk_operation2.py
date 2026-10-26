# write a python script to demonstrate basic banking operations such as deposit, withdraw, and check balance.
account=int(input("Enter your account number: "))
account_details=[]
for i in range(0,account):
    tuple=[()]
    account_no=int(input("Enter your account number: "))
    account_name=input("Enter your name: ")
    DOB=input("Enter your date of birth (dd/mm/yyyy): ")
    pancard=input("Enter your PAN card number: ")
    emailid=input("Enter your email id: ")
    address=input("Enter your address: ")
    contact_no=int(input("Enter your contact number: "))
    current_balance=int(input("enter current balance:"))

    tuple1=(account_no,account_name,DOB,pancard,emailid,address,contact_no,current_balance)

    current_balance=tuple1[4]
    new_deposit=500
    current_balance=current_balance + new_deposit
    tuple1[4]=current_balance

    print(tuple1)
    account_details.append(tuple1)
    print(account_details)
    