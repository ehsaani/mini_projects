
import random, string, time

# Setup character list and shuffled key
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# Encryption function
def encryption(plain_text):
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    return print(f"Here is Encryption: {cipher_text}")

# Decryption function
def decryption(cipher_text):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return print(f"Here is Decryption: {plain_text}")

# Main program
def main():
    while True:
        print("")
        qs = input("What do you want? (Encrypt/Decrypt/Exit)? ")
        print("")

        if qs.lower() == "exit":
            print("Program ended!")
            break

        elif qs.lower() == "encrypt":
            msg = input("Enter a message to encrypt(or click E for exit): ")
            print("")
            encryption(msg)
            print("")

        elif qs.lower() == "decrypt":
            msg = input("Enter a message to decrypt(or click E for exit): ")
            decryption(msg)
            print("")
        else:
            print("Just answer the questions!")
        print("----------")
        time.sleep(1)
main()
