def get_room_details():
    bookings={}
    for i in range(5):
        room_id=int(input("enter room number:"))
        customer_name=input("enter customer name:")
        contactno=input("enter customer contact number:")
        booking_amount=int(input("enter booking amount:"))
        date=input("enter booking date:")
        date=input("enter the date:")
        gst=calculate_gst(booking_amount)