#Write a function that takes two lists of numbers and combines them into a single list.
def combineLists (list1, list2):
    newlist = list1 + list2
    return newlist


#Given a string, find and return any duplicate characters.
def findDuplicateCharacters(stringToCheck):
    setlist = set()
    duplicates = []
    for c in stringToCheck:
        if c in setlist:
            duplicates.append(c)
        else:
            setlist.add(c)
    return duplicates


#Given a large number of ints, return the largest possible product of 3 numbers.
def largeProductFromInts(bigListOfInts):
    threeNumbers = [0,0,0]
    for i in bigListOfInts:
        #check if the new number is higher then our lowest number
        if i > threeNumbers[0]:
            #add the new item to our list
            threeNumbers.append(i)
            #sort our items numerically from low > high
            threeNumbers.sort()
            #remove the first item (lowest number) from our list
            threeNumbers.remove(threeNumbers[0])
    #lastly, multiply everything to get the product
    return threeNumbers[0] * threeNumbers[1] * threeNumbers[2]

#Given a large number of ints, return the fifth largest number
def fromN_5thLargest (bigListOfInts):
    #assuming positive?
    fiveNumbers = [0,0,0,0,0]
    for i in bigListOfInts:
        #check if the new number is higher then our lowest number
        if i > fiveNumbers[0]:
            #add the new item to our list
            fiveNumbers.append(i)
            #sort our items numerically from low > high
            fiveNumbers.sort()
            #remove the first item (lowest number) from our list
            fiveNumbers.remove(fiveNumbers[0])
    #return the lowest (5th largest)
    return fiveNumbers[0]

#Given a large number of ints, return k list of largest numbers.
def kLargest (k, bigListOfInts):
    #assuming positive?
    kNumbers = [0]
    kLength = k
    for i in bigListOfInts:
        #check if the new number is higher then our lowest number
        if i > kNumbers[0]:
            if len(kNumbers) >= kLength:
                kNumbers.pop(0)#pop index 0
            #add the new item to our list
            kNumbers.append(i)
            #sort our items numerically from low > high
            kNumbers.sort()

    #return the lowest (5th largest)
    return kNumbers.reverse()


#“Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order. ”
def findHighFrequencyWords (text_string, k):
    #split the words into an array
    ls_words = text_string.split(' ')

    #create a dictionary storing the frequency of words
    dict = {}
    for word in ls_words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] +=1

    #stora a list of the high freq words as a tuple checking k length of list
    ls_sorted = [('a',0)]
    for key,value in zip(dict.keys(), dict.values()):
        if value > ls_sorted[0][1]:
            if len(ls_sorted) >= k:
                ls_sorted.pop(0)
            ls_sorted.append( (key,value) )
            ls_sorted.sort(key = lambda x: x[1])
    
    #sort in decreasing order and output only the words of our list? (clarifying question)
    ls_sorted[::-1]
    ls_outputText = ""
    for word in ls_sorted:
    	ls_outputText += word[0]
    return ' '.join(ls_outputText)

#CS question a string return True if balanced parethesis
def validParenthesis(string):
    on = 0
    off = 0
    for char in string:
        if char == '[':
            on += 1
        elif char == ']':
            off += 1
            #if closing brackets appear before open
            if off > on:  
                return False
    if on != off:
        return False
    return True

def reverseString(string):
    stack = []
    revWord = ""
    #for i in range(len(string)-1,-1,-1):
    #    stack.append(string[i])
    for char in string:
        stack.append(char)
    #print (stack)
    while stack:
        char = stack.pop(-1)
        revWord += char
    return revWord 

if __name__ == '__main__':
    print(findHighFrequencyWords("a b c d e f e g a g b b",2) )
    print(reverseString("notebook"))


