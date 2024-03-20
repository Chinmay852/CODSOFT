#Note:- This project is completely new for me as I don't know how to make and generate passwords so for this task I had taken a reference from some online resources. Hope you consider and consolidate my problem.

import random
import string

def generate_password(length):
    characters  = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of your password: "))
        if length <=0:
            print("Please enter a positive integer")
            return
        password = generate_password(length)
        print("Passwoed Generated Succesfully:", password)
    except ValueError:
        print("Please enter the integer as you choose.")
if __name__ == "__main__":
    main()