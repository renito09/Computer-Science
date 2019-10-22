import time
secret_message = float (input("Enter a 2 factor number between 0 - 1 (0 or 1 doesnt count): "))
if (secret_message == 0.1) or (secret_message == 0.2) or (secret_message == 0.3) or (secret_message == 0.4) or (secret_message == 0.5) or (secret_message == 0.6) or (secret_message == 0.7) or (secret_message == 0.8) or (secret_message == 0.9) :
    time.sleep(2)   
    print("Your answer was correct")
else:
    time.sleep(2)
    print("Unfortunately your answer was incorrect")