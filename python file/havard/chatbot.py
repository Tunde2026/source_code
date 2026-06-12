print()
print()
print('================================= WELCOME TO PYTHON PROGRAMMING LANGUAGE CHATBOT  =================================')
print('MADE FOR ENGLISH TO IMPROVE ENGLISH LANGUAGE')
print('type \"BYE\" to end the conservation')
print()
print()

user_name = input('ENTER YOUR NAME HERE: ').lower().strip()

example_of_noun = {
    "Name: " " EMMANUEL ISREAL ANU JOHN",
    "Things: " " CUP SPOON CAR" , 
    "Places: " " ABUJA LAGOS KANO"
    
    # {'Things: CUP, SPOON, CAR'},
    # {'Places: ABUJA, LAGOS, KANO'},
}

        
while True:
    
    
    user = input('You: ').lower().strip()
    # greetings = ['hi', 'hello', 'hey']
    
    if 'hi' in user:
        print(f'chatBot: Hi {user_name} i am emmanuel chatbot, how are you doing today?')
        
    elif 'hey' in user:
        print(f'chatBot: Hi {user_name} i am emmanuel chatbot, how are you doing today?')
        
    elif 'hello' in user:
        print(f'chatBot: Hi {user_name} i am emmanuel chatbot, how are you doing today?')
        
    elif 'fine' in user:
        print(f'chatBot: nice to hear that you are fine. {user_name}')
        print("chatBot: what are you up to in doing today.")
        
    elif 'problem' in user or 'issue' in user:
        print(f'chatBot: i will be gald to help you out,  so what is the problem all about {user_name}.')
        
    elif 'noun' in user:
        print(f'chatBot: alright {user_name} ')
        print()
        print('chatBot: A NOUN: \n IS A NAMING WORD THAT IT GIVE NAME TO PEOPLE, PLACES, ANIMALS OR THINGS')
        print(f'chatBot: DID YOU GET THAT {user_name}, so did you want examples of noun')
    
    elif 'yes' in user:
        print(f'chatBot: here are some examples of noun \n {example_of_noun}')
        print(f'chatBot: so {user_name} i think this is where was will stop in todays class i can not go beyound this just type bye to end this conversation')
        
    elif 'bye' in user:
        print('chatBot: bye for now see you next time')
        break
    else:
        print('chatBot: i can not do anything again (i have reach my limit!!!!)')