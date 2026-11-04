def calculate_gst(room_price):
    return 0.18*room_price

#to collect individual room details
def get_room_detail():
    bookings={}
    for i in range(5):
        room_no=input("enter the room number:")
        customer_name=input("enter the name:")
        contact_no=int(input("enter the contact number:"))
        booking_amount=input("enter the booking amount:")
        date=input("enter the date:")
        gst=calculate_gst(booking_amount)
        bookings[i]={"room":room_no,"name":customer_name,"mobile number":contact_no,"amount":booking_amount,"date":date,"GST":gst}
    return bookings 

#to display booking details
def display_booking():
    

#to get total room price
def get_total_room_price():
    pass

#to get total gst
def get_total_gst():
    pass

get_room_detail()
total_room_price=get_total_room_price(booking_info)
total_gst=get_total_gst(booking_info)
display_booking()
print("total room price:{total_room_price}")
print("")
