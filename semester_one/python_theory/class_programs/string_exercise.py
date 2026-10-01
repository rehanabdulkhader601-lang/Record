#Program to demonstrate real python string processing to clean and transform
# Output formate:
# ==============================
#  PROFILE CARD
# ==============================
#  Name     : Naveen Kumar
#  Initials : NK
#  Email    : naveen.kumar@company.com
#  Domain   : company.com
#  Phone    : *********3210
#  Valid    : True
# ==============================

raw_data = """
   naveen   KUMAR
naveen.kumar@COMPANY.com
+91-98765-43210
"""

name,email,phone=raw_data.split("\n")[1],raw_data.split("\n")[2],raw_data.split("\n")[3]
print(name.strip().title())
first,last=name.split()[0],name.split()[1]
initials=first[0].upper()+last[0].upper()
print("initials:",initials)
print("email   :",email.lower())
print("phone  :",phone,replace("+91-98765-43210","********3210"))

if len(phone) == 13:
    valid=True

else:
    valid=False 
print("VALID  :",initials)

print("======================")