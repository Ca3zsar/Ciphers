import pprint, sys

def readDictionary():
    """ Read the content of the "dictionary.txt" file """
    try:
        with open("dictionary.txt") as fileObject:
            content = fileObject.read()
    except FileNotFoundError:
        sys.exit("There is no dictionary file.")
    else:
        return content.split('\n')
    
    
def getWordPattern(word):
    """
    Makes the pattern for a specific word. 
    e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    """
    word = word.upper()
    nextIndex = 0
    pattern = []
    letterIndex = {}
    for letter in word:
        if letter not in letterIndex:
            letterIndex[letter] = str(nextIndex)
            nextIndex += 1
        pattern.append(letterIndex[letter])
    return '.'.join(pattern)
        
        
def writePythonFile(patterns):
    """Creates a new Python files with only a dictionary assignment"""
    file = "wordPatterns.py"
    with open(file,"w") as fileObject:
        fileObject.write("allPatterns = ")
        fileObject.write(pprint.pformat(patterns))


def main():
    allPatterns = {}
    
    dictionary = readDictionary()
    
    for word in dictionary:
        # Get the pattern for each word.
        wordPattern = getWordPattern(word)
        
        if wordPattern not in allPatterns:
            allPatterns[wordPattern] = [word]
        else:
            allPatterns[wordPattern].append(word)
            
    # Writes the 'allPatterns' dictionary in a new Python file.
    writePythonFile(allPatterns)
    

if __name__ == "__main__":
    main()