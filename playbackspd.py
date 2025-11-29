#Put an ellipses between each word inputted by the user
#Calling for user input, variable named playback
playback = input("Enter a few words: ")
#Crreate a variable to be inserted between the words, called seperator
seperator = "..."
#splits the input based on whitespace between them and creates a list, aka turns string into a list. stored in variable called words
words = playback.split()
#calling on the string "..." to rejoin the list of words and stores in a variable called result
result = seperator.join(words)
#prints outcome with the seperator where the whitespace is 
print(result +"...")