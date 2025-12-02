#define the main function
def main():
    tweet = input("Input: ")
    output = birdy(tweet)
    print(output) 


def birdy(word):
    new_string = "Output: "
    for letter in word:
        if letter not in "AEIOUaeiou":
            new_string += letter 
    return new_string
        

main()