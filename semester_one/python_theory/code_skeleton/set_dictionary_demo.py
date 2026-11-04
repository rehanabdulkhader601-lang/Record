# Collect an employee's name, number, company name, and salary.
from os import name


employee_set = set()
employee_dict = {}
emp_name = input("Enter the name:").upper()

emp_no = int(input("Enter the number:"))
company = input("Enter the company name:").upper()
salary = int(input("Enter the salary:"))
address = input("Enter the address:").upper()

employee_set.update({emp_name, emp_no, company, salary,address})
employee_dict["NAME"] = emp_name
employee_dict["NUMBER"] = emp_no
employee_dict["COMPANY"] = company
employee_dict["SALARY"] = salary
employee_dict["ADDRESS"] = address

print("Employee set:", employee_set)
print("Employee dictionary:",employee_dict)

print(f"name\t\tPHONE\t\tCOMPANY\t\tSALARY\t\tADDRESS")
print(f"{emp_name}\t\t{emp_no}\t\t{company}\t\t{salary}\t\t{address}")
