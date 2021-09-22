#Ashad Khan
#101046422

'''
recursive function that will validate (i.e., return True or False) that
the string passed as an argument does not use any uppercase letters
'''
def checkUpper(string) :
    if string == "" :
        return True

    elif string[0] >= 'A' and string[0] <= 'Z' :
        return False

    else :
        return checkUpper(string[1:])

#test = input("enter a string: ")
#print(checkUpper(test))

'''
recursive function that will take a string as an argument and
produce an integer return value for the index of the leftmost underscore in the string
'''
def leftmost_(string):
    if string == "" :
        return -1

    elif string[0] == "_" :
        return 0

    else :
        index = leftmost_(string[1:])
        if index == -1 :
            return -1
        else :
            index = index + 1

    return index


#test = input("enter a string: ")
#print(leftmost_(test))

'''
recursive function that will take a string as an argument and
produce a list of strings as a return value such that the argument string has been
"split" at each instance of the underscore, using the leftmost_ function above.
'''
def listOfStrings(string) :
    if leftmost_(string) == -1 :
        return [string]

    else :
        return [string[0:leftmost_(string)]] + listOfStrings(string[leftmost_(string)+1:])

'''
recursive function that will take a string as an argument and
produce an integer return value for the index of the leftmost vowel in the string
'''
def leftmostVowel(string) :
    if string == "" :
        return -1

    elif string[0] in ["a","e","i","o","u"] :
        return 0

    else :
        index = leftmostVowel(string[1:])
        if index == -1 :
            return -1
        else :
            index = index + 1

    return index


'''
function (not recursive) that will take a string as an 
argument and produce a string return value by changing that "word" into "Pig Latin",
using the function above
'''
def pigLatin(string) :
    vowIndex = leftmostVowel(string)
    if vowIndex == -1 or vowIndex == 0 :
        newstr = string + "ay"

    else :
        newstr = string[vowIndex:] + string[0:vowIndex] + "ay"

    return newstr


'''
recursive function that will take a list of strings as an argument and
produce a list of strings as a return value such that every element of the argument list
has been passed to the pigLatin function 
'''
def pigLatinLs(list) :
    if list == [] :
        return []

    else :
        newls = [pigLatin(list[0])] + pigLatinLs(list[1:])

    return newls


#test = ["robert", "is", "thirty", "eight"]
#print(pigLatinLs(test))

def main(string) :
    if checkUpper(string) == False :
        return "This program only uses input in Snake Case (no capital letters)"

    else:
        ls = listOfStrings(string)
        return pigLatinLs(ls)

snakeCase = input("Enter a string in Snake Case (No capital letters and words seperated by underscores): ")
print(main(snakeCase))
