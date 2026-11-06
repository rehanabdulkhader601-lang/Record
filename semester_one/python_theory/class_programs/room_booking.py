room_dict={}
roomno=input("enter the room number:")
customernmae=input("enter the name:")
contactno=int(input("enter the contact number:"))
bookingamount=int(input("enter the booking amount:"))
date=input("enter the date:")
gst=int(input("enter the gst:"))
gst=bookingamount*gst/100


room_dict={
    "room number":roomno,
    "name":customernmae,
    "contact number":contactno,
    "booking amount":bookingamount,
    "date":date,
    "gst":gst
}
print(room_dict)
