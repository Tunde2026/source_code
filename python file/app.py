# patient_name= ' John Smith'
# age = 30 
# name = input('what is your name ? ')
# print('hello ' + name)
# birth_year = input('enter your date of birth here ')
# age = 2026 - int(birth_year)
# message = 'wow you are ' + str(age) + ' years old'
# print(message)
# price = 3

# print(price ==3 )

temperature = input('what is your current temperateure state ') 
temperature = int(temperature)

if temperature >= 30:
    print("it's is a hot day")
    print("make sure you drink a lot of water")
elif temperature >= 29 :
    print("it is a nice day")
    print("make sure you sleep well")
elif temperature >= 10 :
    print("it is a cold day")
    print("make sure you sleep well")
# elif temperature <= 20:
#     print("it is a nice day but till close to coldness ")
#     print("make sure you sleep well")
else:
    print('your weather must be very cold!!!')
# if temperature > 30:
#     print("it's is a hot day")
#     print("make sure you drink a lot of water")
#     print('done')
# elif temperature > 20:
#     print("it is a nice day")
#     print("make sure you sleep well")
#     print('done')
