import time
import RouteCipher, detectEnglish, RouteFileCipher


def brute_borce(message):
    """
    Try all of the possible key for the message.
    """
    possibleOutcomes = []
    messageLength = len(message)
    
    print("If you want to stop at some point, press CTRL+C")
    
    # We will measure the time needed to brute force the encryption
    startTime = time.time()
    for key in range(1,messageLength):
        try:
            print(f"Trying key #{key} ...")
            
            decryptedText = RouteCipher.decrypt(message,key)
            
            #See if the decrypted text has at least 40% of its content as words.
            if detectEnglish.isEnglish(decryptedText,40):
                print(f"Possible encryption key #{key}")
                possibleOutcomes.append(decryptedText)
            
            print()
        except KeyboardInterrupt:
            totalTime = time.time()-startTime
            print(f"Total time needed for brute force: {totalTime}")
            return possibleOutcomes
        
    totalTime = time.time()-startTime
    print(f"Total time needed for brute force: {totalTime}")
    return possibleOutcomes
    

def main():
    """
    Try all the possible keys for an encrypted text and display only
    the keys for which the decrypted text is written in English.
    """
    
    print("Please enter your message that you want to be decrypted:")
    # We will get the text to be decrypted from a file.
    inputFile = RouteFileCipher.askInputFile()
    message = RouteFileCipher.readText(inputFile)
    
    decryptedMessages = brute_borce(message)
    if decryptedMessages == []:
        print("Decryption failed")
    else:
        print("Please select a file where to save all possible outcomes: ")
        outputFile = RouteFileCipher.askOutputFile()
        
        for text in decryptedMessages:
            RouteFileCipher.writeText(text,outputFile)
    
        print("All of the possible outcomes were printed in the file")
    
main()