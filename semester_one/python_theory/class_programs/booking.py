# To calculate GST
def calculate_gst(room_price):
    return 0.18 * room_price


# To get individual room details
def get_room_details():
    booking_info = {}

    for i in range(5):
        print("\nEnter details of booking", i + 1)

        room_id = int(input("Enter room ID: "))
        customer_name = input("Enter customer name: ")
        contact_no = input("Enter contact no: ")
        date = input("Enter date: ")
        booking_amount = float(input("Enter booking amount: "))

        gst = calculate_gst(booking_amount)

        booking_info[i + 1] = {
            "Room ID": room_id,
            "Customer Name": customer_name,
            "Contact No": contact_no,
            "Date": date,
            "Booking amount": booking_amount,
            "GST": gst
        }

    return booking_info


# To display main dictionary
def display_booking(booking_info):
    for i in booking_info:
        print("\nBooking", i)
        print(booking_info[i])


# To get total price
def get_total_room_price(booking_info):
    total_room_price = 0

    for i in booking_info:
        total_room_price += booking_info[i]["Booking amount"]

    return total_room_price


# To get total GST
def get_total_gst(booking_info):
    total_gst = 0

    for i in booking_info:
        total_gst += booking_info[i]["GST"]

    return total_gst


# Main program
booking_info = get_room_details()

display_booking(booking_info)

total_room_price = get_total_room_price(booking_info)
total_gst = get_total_gst(booking_info)

print("\nTotal Room Price:", total_room_price)
print(f"Total GST: {total_gst}")
