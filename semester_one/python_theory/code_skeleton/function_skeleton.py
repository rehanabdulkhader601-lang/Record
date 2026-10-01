def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa":
        return 10
        # TODO
    # TODO: complete the remaining items
    elif item == "golli baja":
        return 15
    elif item == "coffee":
        return 20
    else:
        return 0
            # TODO


def item_cost(item, qty):
    amount=get_price(item)*qty
    return amount
    # TODO: call get_price() and return the cost


def calculate_gst(amount, rate=0.05):
    gst=amount*rate
    return gst
    # TODO: return the GST rounded to 2 decimals


def generate_bill(subtotal, discount_percent=0):
    discount =subtotal+discount_percent # TODO
    amount_after_discount = subtotal-discount # TODO
    gst = calculate_gst(subtotal,rate=0.05)# TODO: call calculate_gst()
    total = amount_after_discount+gst# TODO
    return discount,gst,total # TODO: return discount, gst and total


def split_bill(total, people):
    each_pays = total/people# TODO
    left_over = total % people# TODO
    return each_pays,left_over# TODO


# ---------------- Main program ----------------
# A group of 3 friends orders 2 dosa and 3 coffee, with a 10% coupon.
subtotal1 = item_cost("dosa",2)+item_cost("coffee",3)      # TODO: call item_cost() for dosa and coffee and add them 
discount1, gst1, total1 = generate_bill(subtotal1,0.02)    # TODO: call generate_bill() using a KEYWORD argument
subtotal2 = item_cost("dosa",2)+item_cost("coffee",3)
discount2, gst2, total2 = generate_bill(subtotal2,0.02)

each, extra =split_bill(total1,total2,3)                   # TODO: call split_bill() with the total (as a whole number) and 3 people

print("Subtotal :", subtotal1)
print("Discount :", discount1)
print("GST      :", gst1)
print("Total    :", total1)
print("Subtotal :", subtotal2)
print("Discount :", discount2)
print("GST      :", gst2)
print("Total    :", total2)

print("Each pays:", each, "| Left over:", extra)
