#A program that is a dictionary that looks up meaning of words for you.

import bs4, requests, msvcrt
#Start the loop to keep asking user to search for word until user wishes to stop
while True:
    word = input("Hi, I am smartWordSearch, I can find the meaning of a word in dictionary for you\nPlease write the word you are looking for here >>> ")
    print()
    next = 1 #This brings up the next definition in each parts of speech (noun, adjective, etc.)
    check = [] #The check helps us to know if there are any remaining definition left

    site = requests.get("https://www.lexico.com/definition/" + word)
    site.raise_for_status()
    #The site used for this program shows webpage for non existent words as well, this variable helps to show the message to the user that the searched word doesn't exist. 
    wordFound = False
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    #Start the loop to get one definition in each parts of speech (noun, adjective, etc)
    while True:
        #the for loop below shows user the first definition in each part of speech
        for title in range(3, 20):
            #Get the CSS selector to match the defintion to be displayed           
            heading = soup.select('#content > div.lex-container > div.main-content > div > div > div > div > section:nth-child(%s) > h3 > span'%title)
            definition = soup.select('#content > div.lex-container > div.main-content > div > div > div > div > section:nth-child(%s) > ul > li:nth-child(%s) > div > p > span.ind'%(title, next))
            #this block displays if there are any definition left to show, when there are none check list will be empty
            if len(definition) != 0:
                print(heading[0].text, end = ' >> ')
                print(definition[0].text)
                print()
                check.append(definition[0].text)
                wordFound = True

        if not wordFound:
            print("The word you searched for has no definition.\nTo type the word correctly or search a new word, press any key or Escape-key to exit\n")
            break

        #User can wish to see more or stop looking for remaining definitions here
        if len(check) != 0:
            print("To view more definition in each, press any key or Escape-key to quit\n")
            check = []
            next += 1
        else:
            print("There are no more definitions left to show.\nTo search a new word, press any key to continue or Escape-key to exit\n")
            break
        #User input is required to continue or stop the search for more definitions
        if msvcrt.getch() == chr(27).encode():
            break
    #User input is asked if it wants to look for another word  
    if msvcrt.getch() == chr(27).encode():
        break

print("Thanks for using smartWordSearch Dictionary!")
