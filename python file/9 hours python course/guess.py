import random

top_of_range = int(input('Type a number: '))


if top_of_range <= 0:
    print('Please type a number larger than 0 next time')
    quit()
else:
    print('Please type a number next time')



random_number = random.randint(-5, 11)

while True:
    user_guess = int(input('Make a guess: '))

    if user_guess <= 0:
        print('Please type a number larger than 0 next time')
    
    quit()

else:
    
    print('Please type a number next time')
    

if user_guess == random_number:
    print('you got it')
else:
    print('you got it wrong')

# print(top_of_range)

