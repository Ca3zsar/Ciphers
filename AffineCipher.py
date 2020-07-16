import string, sys, random
import mathFunctions, detectEnglish

# Get all the ASCII characters.
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def ask_for_choice():
    """
        Get the user's option:
        - 'b' to try all of the possible combinations.
        - 'd' to decrypt a text.
        - 'e' to encrypt a text.
    """
    
    # Ask until the user provide a valid answer.
    while True:
        choice = input("""Please enter an option: 
                       b for brute-force
                       d for decrypt
                       e for encrypt
                       """)
        if choice in ['e','d','b']:
            return choice


def ask_for_input(userChoice):
    """
        If the user's choice is either 'd' or 'e' the user will have to provide a key.
        If the user's choice is b, only the text is mandatory.
    """
    
    if userChoice == 'd' or userChoice == 'e':
        # Make sure that the user will write a valid answer.
        userText = input("Enter the text you want to encrypt/decrypt: ")
        while True:
            # Make sure the keys are valid
            try:
                keyA = input(f"Enter key A which is between 0 and {len(SYMBOLS)}: ")
                keyA = int(keyA) % len(SYMBOLS)
                if mathFunctions.GCD(keyA,len(SYMBOLS)) != 1:
                    raise ValueError
                keyB = input(f"Enter key B: ")
                keyB = int(keyB) % len(SYMBOLS)
            except ValueError:
                print("Enter a valid number!")
            else:
                return (userText,keyA,keyB)
    
    if userChoice == 'b':
        userText = input("Enter the text you want to encrypt/decrypt: ")
        return userText


def encrypt(text, keyA, keyB):
    """ 
        Receive the string that is wanted to be encrypted,
        key A and key B and encrypts every character by the rule
        char = (char * keyA + keyB) % len(SYMBOLS)
    """    
    encryptedText = ""
    
    for letter in text:
       if letter in SYMBOLS:
           # encrypt this symbol.
           symIndex = SYMBOLS.find(letter)
           encryptedText += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
       else:
           encryptedText += letter
           
    return encryptedText


def decrypt(text, keyA, keyB):
    """ 
        Similar with the encrypt function, the only difference is that the key
        will be negative. Multiply the key by (-1) and then encrypt the text
        with the new key.
    """
    
    inverseA = mathFunctions.mInverse(keyA,len(SYMBOLS))
    decryptedText = ""
    for letter in text:
       if letter in SYMBOLS:
           # encrypt this symbol.
           symIndex = SYMBOLS.find(letter)
           decryptedText += SYMBOLS[(symIndex - keyB) * inverseA % len(SYMBOLS)]
       else:
           decryptedText += letter
    
    return decryptedText
    
    
def brute_force(text):
    """
        Tries all the possible combinations of keys.
    """
    for keyA in range(1,len(SYMBOLS)):
        for keyB in range(len(SYMBOLS)):
            if mathFunctions.GCD(keyA,len(SYMBOLS)) == 1:
                decryptedText = decrypt(text,keyA,keyB)
                if detectEnglish.isEnglish(decryptedText):
                    print(decryptedText)


def main():
    """
        The main logic will happen here.
        Ask user for option. Depending on their option ask for text, key and
        alphabet.
    """
    
    userChoice = ask_for_choice()
    info = ask_for_input(userChoice)
    
    if userChoice == 'e':
        encryptedText = encrypt(info[0],info[1],info[2])
        print(encryptedText)
    elif userChoice == 'd':
        decryptedText = decrypt(info[0],info[1],info[2])
        print(decryptedText)
    elif userChoice == 'b':
        brute_force(info)
      
       
# Call only if this file is run.
if __name__ == '__main__':
    main()           