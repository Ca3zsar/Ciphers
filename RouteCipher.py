import math # For math.ceil


def encrypt(text, key):
    """
    Receives a text, makes a grid with key columns and returns the encrypted text.
    For this example a simple order will be considered.
    Go from the top-left corner and concatenate each column.
    """
    
    #Create a grid with key columns
    grid = ['']*key 
    
    for column in range(key):
        # Starting from the first character, 
        # add the character to the (index % key)th column.
        pointer = column
        while pointer < len(text):
            grid[column] += text[pointer]
            pointer += key

    encryptedText = "".join(grid)
    return encryptedText


def decrypt(text,key):
    """
    Receives a text and a key, the number of the rows will be the rounded up 
    result of the division between the length of text and the key. 
    The remaining "boxes" ( (key*period)-length of Text) will be shaded.
    """
    # The period is the number of columns the initial grid would have.
    period = int(math.ceil(len(text) / key ))
    
    # Create the grid with period columns.
    grid = ['']*period
    
    column = 0
    row = 0
    # Get the number of shaded boxes in the grid.
    numOfShadedBoxes = period * key - len(text)
    
    for symbol in text:
        grid[column] += symbol
        column += 1
        
        # If there are no more columns or we are at a shaded box, we go back to
        # the first column and the next row.
        if ( (column == period) or 
             (column == period - 1 and row >= key - numOfShadedBoxes )):
                column = 0
                row += 1
            
    decryptedText = "".join(grid)
    return decryptedText
 

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
    while True:
        # Ask for key until the user will provide a valid one.
        try:
            userKey = input(f"Please enter a key between 0 and {len(userText)//2}: ")
            userKey = int(userKey)
            if userKey > len(userText)//2:
                raise ValueError
        except ValueError:
            continue
        else:
            return (userText,userKey)
    
def main():
    """ 
    Where the main logic is going to take part.
    """
    userChoice = ask_for_choice()
    info = ask_for_input()
    
    if userChoice == 'e':
        encryptedText = encrypt(info[0],info[1])
        print(encryptedText)
    elif userChoice == 'd':
        decryptedText = decrypt(info[0],info[1])
        print(decryptedText)
    
# Call only if this file is run.
if __name__ == '__main__':
    main()    
    
        
    