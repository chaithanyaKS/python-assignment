import re

STUD_ID_REGEX = r'\d+'
STUD_NAME_REGEX = r'[a-zA-z]+' 

stud_id = input('Enter Student ID: ')
if bool(re.fullmatch(STUD_ID_REGEX,stud_id)):
    stud_name = input('Enter name: ')
    if bool(re.fullmatch(STUD_NAME_REGEX,stud_name)):
        fee = input('Enter fees: ')
        email = stud_name + '@vvce.com'
        print(f'''
Student ID: {stud_id}
Student name: {stud_name}
Fees Amount: {fee}
E-mail: {email}
        ''')
    else:
        print('Enter proper name')
else:
    print('Enter proper ID')
