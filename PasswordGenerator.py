import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    password = ''.join(random.sample(all_chars, length))

    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    password = generate_password(length)

    print("Generated password:", password)

if __name__ == "__main__":
    main()
