import time
print("THIS IS A TEST TO SAVE YOUR INFORMATION SO YOU CAN LOG IN INTO GITHUB WITHOUT PASSWORD")
answers = []
answers.append(input("WHAT IS YOUR NAME?!?! "))
answers.append(input("What is your favourite videogame? "))
answers.append(input("Where do you live? "))
answers.append(input("Do you have a pet? and what is it? "))
answers.append(input("How old are you? "))
x = int(answers[4])
time.sleep(2)
print("Thanks for your time, now you can log in with this info!")
print("GITHUB ACCOUNT UPGRADED")
time.sleep(2)
print("NAME: " + answers[0])
print("VIDEOGAME: " + answers[1])
print("HOME: " + answers[2])
print("PET: " + answers[3])
print("AGE: " + answers[4])
time.sleep(2)
print("I AM A HACKER NOW I HAVE YOUR DETAILS")
print("THIS CHANGE IS IRREVERSIBLE")