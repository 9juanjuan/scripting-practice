

employee_file = open('employees.txt', 'r')

# Readable
# print(employee_file.read())  // Read all file
# print(employee_file.readlines())  // Takes each line and put it in array, can call index []
# for employee in employee_file.readlines():
#     print(employee)

#append
# employee_file = open('employees.txt', 'a')
# employee_file.write("\nKelly - Customer Service")


# Overwrite 
# employee_file = open('employees.txt', 'w')
# employee_file.write("\nKelly - Customer Service")

#  You can also create different filetypes with open 'w', for example
#  You can create HTML files and write html by inserting as plain text
employee_file.close()