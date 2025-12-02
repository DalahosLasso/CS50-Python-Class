def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):  # Rule 1: all vanity plates must be between 2 and 6 characters
        return False
    
    if not s[:2].isalpha():  # Rule 2: plates must start with two letters
        return False 
    seen_digit = False       # Marks if a number has appeared
    for ch in s:
        # Rule 3: only letters and digits allowed
        if not ch.isalnum():
            return False
        if ch.isdigit():
            # Rule 5: Numbers cannot be used in the middle of a plate; they must come at the end
            if not seen_digit and ch == "0":
                return False
            seen_digit = True
        else:
            if seen_digit:
                return False
    
    return True
   
        
main()
