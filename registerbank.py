# def register():
#     account_name = input("Enter Account Name")
#     process = True
#     while process:
#         pin = int(input("Enter 4 digit Pin: "))
#         if pin not in range (1000,10000):
#             print("Invalid Pin")
#             print('Please try again!')
#         else:
#             print("Registration Successful! \n")
#             process = False
#             return account_name, pin 
        

#         name, pin = register()
#         print(name)
#         print(pin)
        


import library

library.student_info()
name, gender, age, phone_num, email_address = library.student_info()
