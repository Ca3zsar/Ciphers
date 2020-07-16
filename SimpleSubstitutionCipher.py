import sys, random, string

SYMBOLS = string.ascii_uppercase

def checkKey(key):
    """
    Check if a provided key is valid.
    """
    symbolList = sorted(list(SYMBOLS))
    keyList = sorted(list(key))
    
    # If the lists are the same, the key is valid, therefore, return True
    return symbolList == keyList


def getRandomKey():
    """
    Generate a random key and return it.
    """
    possibleKey = SYMBOLS
    possibleKey = list(possibleKey)
    random.shuffle(possibleKey)
    return "".join(possibleKey)


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


def ask_for_input(userChoice):
    """
    Asks the user for the input.
    """
    
    if userChoice == 'd':
        # Make sure that the user will write a valid answer.
        userText = input("Enter the text you want to decrypt: ")
        userText = userText.upper()
        while True:
            # Make sure the key is valid.
            key = input("Enter the key you want to decrypt with: ")
            if checkKey(key):
                return (userText, key)
    if userChoice == 'e':
        # If the choice was to encrypt, only the text is necessary.
        userText = input("Enter the text you want to encrypt: ")
        userText = userText.upper()
        return userText


def translate(userText, key, mode):
    """
    Substitues every symbol from the text provided by user
    with the corresponding one from the key.
    """
    translated = ""
    # We substitute each character from charsA with one from charsB
    charsA = SYMBOLS
    charsB = key
    
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
    
    # Loop through each symbol of the text.
    for symbol in userText:
        if symbol in charsA:
            # Find its index in charsA
            symIndex = charsA.find(symbol)
            translated += charsB[symIndex]
        else:
            translated += symbol

    return translated

def encrypt(userText, key):
    return translate(userText, key, "encrypt")


def decrypt(userText, key):
    return translate(userText, key, "decrypt")


def main():
    """
    Where the main logic will take part.
    """
    choice = ask_for_choice()
    
    if choice == 'e':
        # If the user wants to encrypt, generate a random key.
        key = getRandomKey()
        userText = ask_for_input(choice) 
        
        encryptedText = encrypt(userText, key)
        print(f"Your key is : {key}")
        print(f"You encrypted message is :\n{encryptedText}")
    if choice == 'd':
        info = ask_for_input(choice)
        
        decryptedText = decrypt(info[0],info[1])
        print(f"The decrypted message is :\n{decryptedText}")
        

if __name__ == "__main__":
    main()