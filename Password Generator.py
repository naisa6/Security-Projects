import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter password length:\n"))

    if password_length < 8:
        print("Password needs to be at least 8 characters")
    else:
        generated_password = generate_password(password_length)
        print("Generated password: " + generated_password)