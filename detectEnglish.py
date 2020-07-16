
# A module to help detecting Enlgish words after decrypting.

# To use this module, type this code:
#   import detectEnglish
#   detectEnglish.isEnglish(some string) # Returns True or False
# To make it work you will need to have a "dictionary.txt" file
# in this directory, with English words in it.

import string, sys, time

UPPERLETTERS = string.ascii_uppercase   
ALPHABET = string.ascii_letters + ' \t\n'

def loadDictionary():
    """
    Read the content of the "dictionary.txt" file and return it
    """
    dictionaryFile = "dictionary.txt"
    
    # Check if the file exists, otherwise, exit
    try:
        with open(dictionaryFile) as fileObject:
            content = fileObject.readlines()
    except FileNotFoundError:
        print("Dictionary file not found!")
        sys.exit()    
    else:
        # Add the content of the file in a set. The set's lookup is faster
        # than the list's and take less memory that a dictionary's
        englishWords = set()
        for word in content:
            englishWords.add(word.strip())
        return englishWords
    
ENGLISH_WORDS = loadDictionary()


def removeNonLetters(message):
    """
    Removes any character that is not a letter or space.
    """
    lettersOnly = ""
    for symbol in message:
        if symbol in ALPHABET:
            lettersOnly += symbol
            
    return lettersOnly

# Faster aproach, maybe?
# def removeNonLetters(message):
#     lettersOnly = []
#     for symbol in message:
#         if symbol in ALPHABET:
#             lettersOnly.append(symbol)
#     return "".join(lettersOnly)

def getEnglishCount(message):
    """
    Count the number of the English words from the received message.
    """
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    
    # If the list of possible words is empty, return 0.0, that means no words at all.
    if possibleWords == []:
        return 0.0
    
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    
    # Return the ratio of the words in the message that are in the dictionary file.
    return float(matches) / len(possibleWords)


def isEnglish(message, wordPercentage = 20, letterPercentage = 85):
    """
    By default, 20% of the words must exist in the dictionary file, and
    85% of all characters must me letters or spaces.
    """
    start = time.time()
    wordsMatch = getEnglishCount(message) * 100
    numberOfLetters = len(removeNonLetters(message))
    lettersMatch = float(numberOfLetters) / len(message) * 100
    
    # If both wordstMatch and lettersMatch are greater than the minimum
    # percentages required, return True
    
    print(f"Total time needed: {round(time.time() - start,4)}")
    
    if (wordsMatch > wordPercentage) and (lettersMatch > letterPercentage):
        return True
    else:
        return False

