# Create a list that prompts the user for items, one per line,
# until the user inputs control-d to signal the end of input.
# Then output the user's grocery list in all uppercase, sorted alphabetically,
# with each line showing how many times each item was entered.

def main():   # define the main function that will run the program

                    
    grocery_list = {}  # create an empty dictionary to store items and their counts      
    
    while True:        # start an infinite loop to repeatedly ask for input

        try:                    #try to get user input 
            text = input()      # read one line of input from the user
            text = text.upper() # convert the input to uppercase for consistency
        except EOFError:        # this happens when the user presses control-d
            break               # exit the loop if no more input is given
        
        
        if text in grocery_list:       # check if the item is already in the dictionary
            grocery_list[text] += 1    # if so, increase its count by 1
        else:                          # otherwise, this is a new item
            grocery_list[text] = 1     # add it to the dictionary with a count of 1
    
    # loop through the dictionary in alphabetical order of item names
    for item in sorted(grocery_list):
        # print the count first, then the item name   
        print(f"{grocery_list[item]} {item}")

main() # call the main function to start the program