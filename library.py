def student_info():
 
 name = (input('Enter Your Name:'))
 gender = (input('Enter Your Gender'))
 age = int(input('Enter Your Age'))
 phone_num = (input('Enter Your Phone Number:'))
 email_address = (input('Enter Your Email Address'))

#  student_file = {
#      'name':name,
#      'gender':gender,
#      'age':age,
#      'phone_num':phone_num,
#      'email_address':email_address
#  }

 return name, gender, age, phone_num, email_address

 print(f'Student Name: {name}')
 print(f'Student Gender: {gender}')
 print(f'Student Age: {age}')
 print(f'Student PhoneNumber: {phone_num}')
 print(f'Student EmailAddress: {email_address}')



