#compress string char array where each consecutive occuring character is grouped and replaced with that character and its no. of occurence
#for only 1 occurence, the letter is unaffected, for more than 9, append each digit as string followed by the character

## needs to be done in place. given the character array

def stringCompression(chars):
    i = 0
    size = len(chars)
    currentIndex = 0
    while i < size:
        j = i + 1
        while j < size and chars[i] == chars[j]:
            j += 1
       
        chars[currentIndex] = chars[i]
        currentIndex += 1
        groupsize = j - i

        if groupsize > 1:
            strArr = [i for i in str(groupsize)]

            for i in strArr:
                chars[currentIndex] = i
                currentIndex += 1
        i = j
    return currentIndex


chars = ["a","a","b","b","b","c","d","d"]
print(stringCompression(chars))
print(chars)
