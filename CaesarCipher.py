import string

def encrypt(text, key, alphabet = None):
    """ 
        Receive a string which is wanted to be encrypted,
        a key to encrypt the text and optionally, an alphabet.
        If no alphabet is provided by the user, the English alphabet will be used
    """
        
    encryptedText = ""
    
    for letter in text:
        if letter in alphabet:
            # Find the position of the letter in the alphabet.
            position = alphabet.find(letter)
            # Get the new position in the alphabet.
            position = (position + key) % len(alphabet)
            #Add the encrypted character to the encrypted text.
            encryptedText += alphabet[position]
        else:
            encryptedText += letter
    
    return encryptedText


def decrypt(text, key, alphabet=None):
    """ 
        Similar with the encrypt function, the only difference is that the key
        will be negative. Multiply the key by (-1) and then encrypt the text
        with the new key.
    """
    
    key *= -1
    decryptedText = encrypt(text, key, alphabet)
    return decryptedText


def brute_force(text, alphabet=None):
    """
        Try all of the possible keys.
        The key will have the value between 0 and the length of the alphabet.
        Decrypt the string using every key possible and then display the outcome.
    """
    
    sizeOfAlphabet = len(alphabet)
    
    for key in range(sizeOfAlphabet):
        possibleOutcome = decrypt(text, key, alphabet)
        print(possibleOutcome)
        

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
        

def unique_alphabet(alphabet):
    """
        A function that receives an alphabet and returns it back sorted lexicographically
        and with unique elements.
    """
    
    newAlphabet = ""
    for character in alphabet:
        if character not in newAlphabet:
            newAlphabet += character
    
    alphabetString = "".join(sorted(newAlphabet))
    
    return alphabetString



def ask_for_input(userChoice):
    """
        If the user's choice is either 'd' or 'e' the user will have to provide a key.
        If the user's choice is b, only the text is mandatory.
        The alphabet is optional.
    """
    
    if userChoice == 'd' or userChoice == 'e':
        # Make sure that the user will write a valid answer.
        userText = input("Enter the text you want to encrypt/decrypt: ")
        
        alphabet = input("Enter a set of characters to represent the alphabet ( nothing = English Alphabet)")
        if alphabet == '':
            alphabet = string.ascii_letters
        else:
            alphabet = unique_alphabet(alphabet)
        
        sizeOfAlphabet = len(alphabet)
        
        while True:
            try:
                key = input(f"Enter key between 0 and {sizeOfAlphabet}: ")
                key = int(key) % sizeOfAlphabet
            except ValueError:
                print("Enter a valid number!")
            else:
                return (userText,key,alphabet)
    
    if userChoice == 'b':
        userText = input("Enter the text you want to encrypt/decrypt: ")
        
        alphabet = input("Enter a set of characters to represent the alphabet ( nothing = English Alphabet)")
        if alphabet == '':
            alphabet = string.ascii_letters
        else:
            alphabet = unique_alphabet(alphabet)
        
        return (userText,alphabet)

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
        brute_force(info[0],info[1])
      
       
# Call only if this file is run.
if __name__ == '__main__':
    main()           
    