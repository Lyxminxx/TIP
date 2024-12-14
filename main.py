from os import system, name
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print("Welcome to TIP!\n")

#Pulls and reads the text-file

pathCheck = False
while not pathCheck:
    userTextfile = input("Give the path to file.\n>")
    userTextfile = userTextfile.replace("\\", "/").replace('"', "")
    try:
        textfile = open(userTextfile, "r", encoding="utf-8")
        text = textfile.read()
        pathCheck = True  
    except FileNotFoundError:
        print("Your file was not found, make sure you provide the right path.")
        input ("Hit ENTER too try again.")
        clear()
clear()

#Removes punctuation
punctuationRemover = dict.fromkeys(map(ord, '!@#$.,":-'), None)
text = text.translate(punctuationRemover)
#Makes all the text lowercase so there wont be duplicates like Yes and yes.
text = text.lower()

#Makes a dictionary that will save the words and how many times the word has been used
wordAmount = {}
#Makes a list and adds each word as it's own list item.
wordlist = text.split()

for i in range (len(wordlist)):
    #If the word is not in the dictionary, add it and give it the value of 1
    if not(wordlist[i] in wordAmount):
        wordAmount[wordlist[i]] = 1
    #If the word is in the dictionary add 1 to the value.
    elif(wordlist[i] in wordAmount):
        wordAmount[wordlist[i]] = wordAmount[wordlist[i]] + 1

#Sorts the list from smallest to largest
wordAmount = dict(sorted(wordAmount.items(), key=lambda item: item[1]))
#reverses the list.
wordAmount = dict(reversed(list(wordAmount.items())))

done = False

while done == False:
    print("TIP\n")
    todo = input("What do you want to do? \n A: See a list of the most used words. \n B: Search for a word. \n C: Look at information about the text. \n D: Exit\n>").strip()
    clear()
    if todo.upper() == "A" or todo.upper() == "LISTE" or todo.upper() == "LIST":
        amountWrittenOut = int(input("How many words do you want to see?\n>"))

        #Prints out a list of words
        if amountWrittenOut > len(wordAmount):
            for i in range (1,len(wordAmount)+1):
                print(f"{i}. Word: '{list(wordAmount)[i]}' - Amount: {list(wordAmount.values())[i]}")
        else:
            for i in range (1,amountWrittenOut+1):
                print(f"{i}. Word: '{list(wordAmount)[i]}' - Amount: {list(wordAmount.values())[i]}")
    elif todo.upper() == "B" or todo.upper() == "SØK" or todo.upper() == "SØKE" or todo.upper() == "SEARCH":
        searchWord = input("Which word are you looking for?\n>").lower()
        if (searchWord in wordAmount):
            print(f"\nThe word '{searchWord}' was used {wordAmount[searchWord]} times in the text.")
        else:
            print(f"\nThe word '{searchWord}' is not in the text.")

    elif todo.upper() == "C" or todo.upper == "info" or todo.upper == "information" or todo.upper == "informasjon":
        print(f"There are {len(wordlist)} words in the text.")

        textfile = open(userTextfile, "r", encoding="utf-8")
        textfile = textfile.read().replace(" ", "")
        charCount = list(textfile)

        print(f"There are {len(charCount)} characters in the text.")
        textfile = text.split()
        wordLength = []
        average = 0
        for i in range (0, len(textfile)):
            wordLength.append(len(textfile[i]))

        for i in range (0,len(wordLength)):
            currentNumber = int(wordLength[i])
            average += int(currentNumber)
        average = round(average / len(textfile),2)
        print(f"At average there is {average} symboles in each word.")
    elif todo.upper() == "D" or todo.upper() == "EXIT":
        done = True
    
    else:
        print("ERROR - You have to choose one of the functions\n")
    input("Hit ENTER to continue!")
    clear()