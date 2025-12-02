#define main function, i wantt to print the statement once they have paid in full. 
#I will create a new function to solve this problem called ticker
def main():
    change = ticker()
    print(f"Change owed: {change} cents. Here is a Coke")
#created a function called ticker that will iterate over the user input to validate 
#the correct coin amount
def ticker():
    due = 50 
    while due > 0:
        coin = int(input("Insert coin: "))
        if coin in [25,10,5]:
            due -= coin 
            if due > 0:
                print(f"Amount due: {due} cents")
        else:
            print("invalid coin, try again")
    return due
  #the second due is inside the first bc it needs to do two things before printing   
main()

#While due is GREATER THAN zero,
#coin will be equal to the User's input converted into an integer.
#If coin aka the user input equals either 25,10, or 5,
#We will subract the amount inputed from the original value of due which is 50
#once the value of due equals zero, the loop will break
#once the loop breaks, main calls for the value of ticker, which is 0
#the string prints
