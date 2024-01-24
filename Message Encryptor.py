from cryptography.fernet import Fernet  # symmetric encryption, requires secret key

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message  = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message.decode())
    return decrypted_message

if __name__ == "__main__":
    key = generate_key()
    user_choice = input("Enter E to Encrypt, D to Decrypt or X to Exit: \n") # session key only valid once.

    while user_choice != "X":

        if user_choice == "E":        
            message = input("Message to encrypt: ")
            encrypted_message = encrypt_message(key, message)
            print(f"Encrypted message: {encrypted_message}")
        
        elif user_choice == "D":
            message = input("Message to decrypt: ").encode()
            decrypted_message = decrypt_message(key, message)
            print(f"Decrypted message: {decrypted_message}")

        user_choice = input("Enter E to Encrypt, D to Decrypt or X to Exit: \n")