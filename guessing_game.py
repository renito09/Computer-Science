import time

x = 1
answer = ""
print("Choose a number. 1 to 10")
time.sleep(3)
while(answer != "yes" and x < 11):
    answer = input("Is your number " + str(x) + "? ")
    if(answer != "yes"):
        x = x + 1
    else:
        print("Your number is " + str(x) + "!")

if(x > 10):
    print("Seriously go to college")