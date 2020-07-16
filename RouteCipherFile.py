import os, sys, easygui, time
import RouteCipher

def askInputFile():
    """
    It will open a .txt file and return the fileName back.
    """
    while True:
        print("Enter a valid .txt file")
        # Try until a plain-text file is provided.
        try:
            fileName = easygui.fileopenbox("Enter a .txt file",
                                           "Open file",
                                           default="C:\\",
                                           filetypes=["*.txt"])
            if fileName == None:
                raise 
        except :
            pass
        else:
            return fileName
   
   
def askOutputFile():
    """
    It will open a prompt to save a file at a specific location and name.
    """
    while True:
        print("Save the final file")
        # Try until the final file is saved.
        try:
            fileName = easygui.filesavebox("Save your file",
                                           "Save the file",
                                           default="C:\\DefaultFile.txt",
                                           filetypes=["*.txt"])
            if fileName == None:
                raise
        except:
            pass
        else:
            return fileName        
        
def readText(fileName):
    """
    Read the text from the file and return in back.
    """
    fileText = ""
    with open(fileName,"r") as fileObject:
        fileText = fileObject.read()
    
    return fileText             
        

def writeText(outputText, fileName):
    """
    Write the text into the output file.
    """
    with open(fileName,"w") as fileObject:
        fileObject.write(outputText)
        
     
def askOption():
     """
     The user will be prompted to choose between decode and encode.
     """
     while True:
        print("Do you want to (E)ncode or (D)ecode?")    
        choice = input(">> ")
        
        if choice.lower() in ['d','e']:
            return choice
            
     
def askForKey():
    """
    The user will be prompted to enter a key.
    """          
    while True:
        # Ask for key until the user will provide a valid one.
        try:
            userKey = input(f"Please enter a key: ")
            userKey = int(userKey)
        except ValueError:
            continue
        else:
            return userKey
     
     
def main():
    """
    Where the main logic takes place.
    """
    
    # Ask for their option.
    
    inputFile = ""
    outputFile = ""
    
    choice = askOption()
    key = askForKey()
    
    inputFile = askInputFile()
    inputText = readText(inputFile)
    
    outputFile = askOutputFile()
    
    #Start the timer here.
    startTimer = time.time()
    
    # Depending on their choice, encode or decode.
    if choice == 'e':
        encryptedText = RouteCipher.encrypt(inputText, key)
        writeText(encryptedText, outputFile)
    elif choice == 'd':
        decryptedText = RouteCipher.decrypt(inputText, key)
        writeText(decryptedText, outputFile)
    
    finishTimer = time.time()
    totalTime = round(finishTimer - startTimer, 2)
    
    print("The operation was succesful")
    print(f"Total time needed: {totalTime}")
    
if __name__ == "__main__":
    main()