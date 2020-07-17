import string

LETTERS = string.ascii_uppercase

def ask_for_choice():
    """
        Get the user's option:
        - 'd' to decrypt a text.
        - 'e' to encrypt a text.
    """
    
    # Ask until the user provide a valid answer.
    while True:
        choice = input("""Please enter an option: 
                       d for decrypt
                       e for encrypt
                       """)
        if choice in ['e','d']:
            return choice    
    
    
def ask_for_input():
    """
    Read the user's text to be encrypted / decrypted and the key.
    """
    # Make sure that the user will write a valid answer.
    userText = input("Enter the text you want to encrypt/decrypt: ")
    userKey = input(f"Please enter a key : ")
    return (userText,userKey)


def translate(message, key, mode):
    key = key.upper()
    translated = []
    keyCount = 0

    for index in range(len(message)):
        letterIndex = LETTERS.find(message[index].upper())
        keyIndex = LETTERS.find(key[keyCount%len(key)])
        
        if letterIndex != -1:
            # We go through the key only if we change a character.
            keyCount += 1
            
            #Get the new letter index, dedending on the mode of the translation.
            if mode == 'e':
                newLetterIndex = (letterIndex+keyIndex)%len(LETTERS)
            else:
                newLetterIndex = (letterIndex-keyIndex)%len(LETTERS)
                
            # Keep the upper and lower letters as they were in the original message.    
            if message[index].islower():
                translated.append(LETTERS[newLetterIndex].lower())
            else:
                translated.append(LETTERS[newLetterIndex])
                
        else:
            translated.append(message[index])
    
    return "".join(translated)


def encrypt(message, key):
    """
    Receives a message and a key and encrypt the message with the Vigenere Cipher
    """
    return translate(message, key, 'e')
                
    
def decrypt(message, key):
    """
    eceives a message and a key and decrypt the message
    """
    return translate(message, key, 'd')


def main():
    choice = ask_for_choice()
    info = ask_for_input()
    
    if choice == 'e':
        encrypted = encrypt(info[0],info[1])
        print("Your encrypted message is:")
        print(encrypted)
    elif choice == 'd':
        decrypted = decrypt(info[0],info[1])
        print("Your decrypted message is: ")
        print(decrypted)
        

if __name__ == "__main__":
    main()