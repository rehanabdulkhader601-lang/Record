# Collect an employee's name, number, company name, and salary.
employee_set = set()
employee_dict = {}
emp_name = input("Enter the name:").upper()

emp_no = int(input("Enter the number:"))
company = input("Enter the company name:").upper()
salary = int(input("Enter the salary:"))
address= input("enter the address:").upper()

employee_set.update({emp_name, emp_no, company, salary,address})
employee_dict["NAME"] = emp_name
employee_dict["NUMBER"] = emp_no
employee_dict["COMPANY"] = company
employee_dict["SALARY"] = salary
employee_dict["ADDRESS"] = address 

print("Employee set:", employee_set)
print("Employee dictionary:",employee_dict)

print(f"NAME\tPHONE\tCOMPANY\tSALARY\tADDRESS")
print(f"{emp_name}\t{emp_no}\t{company}\t{salary}\t{address}")

