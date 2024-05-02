def chatbot():
    print("hi i'm chatbot ,how can i help you today")
    while True:
        user_input=input("you : ")
        if user_input.lower()=="bye":
            print("chatbot : bye ! have a great day")
            break
        elif user_input.lower()=="hello":
            print("chatbot : hello there! how are you doing today")
        elif user_input.lower()=="how are you":
            print(" chatbot : i'm doing great thanks for asking,what would you like to see")
        elif user_input.lower()=="phone":
            print(" chatbot : Which brand")
        elif user_input.lower()=="apple":
            print(" chatbot : ok. what is your budget")
        elif user_input.lower()=="100000":
            print(" chatbot : ok")
        elif user_input.lower()=="ok":
            print(" chatbot : Here are some top models")
        elif user_input.lower()=="Thank you":
            print("welcome")
            print("See you again")
        else :
            print("chatbot : i didn't understand what you said ,can you please rephrase")
chatbot()

