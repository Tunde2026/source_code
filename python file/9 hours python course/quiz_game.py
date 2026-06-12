print('welcom to my computer quiz')

playing = input('do you want to play? ')

if playing.lower() != 'yes':
    quit()


print("okay ! let play on")

answer = input('what is the meaning of iot ')
if answer.lower() == 'internet of things':
    print('corect!')
else:
    print('not quite correct') 