import os, re, copy, pprint, copy
import SimpleSubstitutionCipher, makeWordPattern

if not os.path.exists("wordPatterns.py"):
    makeWordPattern.main() # create the wordPatterns.py file

import wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLetterOrSpace = re.compile('[^a-zA-Z\s]')


def getBlankMapping():
    """ Creates a dictionary whose keys are letters and the values
    are empty lists.
    """
    emptyMapping = {}
    for letter in LETTERS:
        emptyMapping[letter] = []
    return emptyMapping


def getIntersectionMapping(map1,map2):
    """ 
    Intersects two dictionaries received.
    """
    newMap = getBlankMapping()
    for letter in LETTERS:
        # If a list from a map is empty, add the other one.
            if map1[letter] == []:
                newMap[letter] = map2[letter][:]
            elif map2[letter] == []:
                newMap[letter] = map1[letter][:]
            else:
                #Add a letter only if it appears it both mappings.
                for mappedLetter in map1[letter]:
                    if mappedLetter in map2[letter]:
                        newMap[letter].append(mappedLetter)
                        
    return newMap


def addLettersToMapping(letterMap, cipherWord, candidate):
    """
    Add the letters of the candidate to the cipherWord's mapping.
    """
    # Create a copy of the original letterMap.
    letterMap = copy.deepcopy(letterMap)
    for i in range(len(cipherWord)):
        if candidate[i] not in letterMap[cipherWord[i]]:
            letterMap[cipherWord[i]].append(candidate[i])
            
    return letterMap
        

def removeSolvedLetters(letterMapping):
    """
    The letters from ciphers that appear only once is a letter's mapping
    are solved and can be removed from another letter's mapping.
    """
    # Create a copy of the original mapping.
    letterMapping = copy.deepcopy(letterMapping)
    loopAgain = True
    while loopAgain:
        loopAgain = False
        
        # 'solvedLetters' variable will store a list of the letters considered
        # solution.
        solvedLetters = []
        for letter in LETTERS:
            if len(letterMapping[letter]) == 1:
                solvedLetters.append(letterMapping[letter][0])
            
        # If a letter is solved, then it cannot be a potential decryption letter
        # for a different letter from the ciphertext.
        for letter in LETTERS:
            for solved in solvedLetters:
                if len(letterMapping[letter]) != 1 and solved in letterMapping[letter]:
                    letterMapping[letter].remove(solved)
                    if len(letterMapping[letter]) == 1:
                        # A new letter is now solved, so we will loop again.
                        loopAgain = True

    return letterMapping


def crackSubstitution(message):
    intersectionMapping = getBlankMapping()
    wordList = nonLetterOrSpace.sub('',message.upper()).split()
    
    for cipherWord in wordList:
        # Get a new mapping for each word.
        newMap = getBlankMapping()

        wordPattern = makeWordPattern.getWordPattern(cipherWord)
        if wordPattern not in wordPatterns.allPatterns:
            continue # This word is not in the included dictionary, so continue.
        
        # Add the letters of each candidate to the mapping.
        for candidate in wordPatterns.allPatterns[wordPattern]:
            newMap = addLettersToMapping(newMap, cipherWord, candidate)
        
        # Intersect the new mapping with the existing intersected mapping.
        intersectionMapping = getIntersectionMapping(intersectionMapping, newMap)
        
    # Remove any solved letters from the other lists.
    finalMapping = removeSolvedLetters(intersectionMapping)
    return finalMapping


def decryptWithMapping(message, letterMapping):
    """
    Returns a string of the ciphertext decrypted with the letter mapping,
    with any ambigous decrypted letters replaced with an underscore.
    """
    
    # Create a key fron the letterMapping.
    key = ["x"] * len(LETTERS)
    for letter in LETTERS:
        if len(letterMapping[letter]) == 1:
            # If there is only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[letter][0])
            key[keyIndex] = letter
        else:
            message = message.replace(letter.lower(), '_')
            message = message.replace(letter.upper(), '_')
    key = ''.join(key)
    
    # Decrypt the ciphertext with the key created.
    return SimpleSubstitutionCipher.decrypt(message, key)


def main():
    print("Enter your input")
    message = input("")
    message = message.upper()
    
    #Determine the possible valid ciphertext translations.
    print("Trying to translate the message...")
    letterMapping = crackSubstitution(message)
    
    # Display the results.
    print("Mapping: ")
    pprint.pprint(letterMapping)
    print()
    
    decrypted = decryptWithMapping(message, letterMapping)
    print("The decrypted text is:")
    print(decrypted)
    
if __name__ == "__main__":
    main()