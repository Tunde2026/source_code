print('welcome to python course let confirm if you are the real user')

first_name = input('what is your first name: ').upper().strip()
surname = input('what is your Surname name: ').upper().strip()
last_name = input('what is your Last Name name: ').upper().strip()

full_name = surname + " " + first_name + " " + last_name

if full_name == "AJIBADE EMMANUEL ADURAGBEMI":
    print('let move on you are the real user')
    
else:
    print('ERROR you are not the real user go away')

# if name == ''