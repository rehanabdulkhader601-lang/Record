age=int(input("enter ur age:"))
day=input("enter the day")
weekday = "monday","tuesday","wednesday","thursday","friday"
price=250
weekend = "saturday","sunday"
price=price*75/100
if(age<=5):
    print("child")

    if(day == weekday):
        price1 = price * 50/100
        print("price",price1)
    else:
        day == weekend
        price2 = price * 75/100
        print("price",price2)

elif(age<=50):
    print("adult")
    price = 250
    print("price:",price)

else:
    print("senior citizen")
    price = 250 * 10/100
    print("price",price)

