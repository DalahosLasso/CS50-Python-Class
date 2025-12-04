#get user input
#convert MM/DD/YYYY to YYYY-MM-DD
#print YYYY-MM-DD

# list of full month names
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").strip() # remove leading/trailing whitespace
        
        #----------- Numeric format path ---------
        if "/" in date:
            parts = date.split("/") # divide string into list of substrings based on seperator
            if len(parts) != 3:   #check to see how many substrings were created
                print("Please enter in M/D/YYYY format.") #print this if the substrings 
                continue   # proceed to next iteration    # are not a total of 3
            
            month_str, day_str, year_str = parts  #

            try:
                month = int(month_str)
                day = int(day_str)
                year = int(year_str)

                # check ranges
                if not (1 <= month <= 12):  #if month is not between 1 and 12
                    print("Month must be between 1 and 12.")
                    continue

                if not (1 <= day <= 31):
                    print("Day must be bewtween 1 and 31")
                    continue 

                if year < 1:
                    print("Year must be a positive integer")
                    continue
                
            except ValueError:
                print("Month, day, and year must all be numbers")
                continue
            # format as YYYY-MM-DD
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        #----------- Named-month format path -------------------
        elif "," in date:
            try:
                left, right = date.split(",")
            except ValueError:
                print("Please include only one comma in the format MonthName D, YYYY")
                continue

            left = left.strip()
            right = right.strip()

            if not right.isdigit() or int(right) < 1:
                print("Year must be positive number")
                continue
            year = int(right)
            
            left_parts = left.split()
            if len(left_parts) != 2:
                print("Left part must be 'MonthName Day', e.g., September 8")
                continue

            month_name, day_str = left_parts
            month_name = month_name.title()
            if month_name not in months:
                print("Month must be full name, e.g., April")
                continue
            if not day_str.isdigit() or not (1 <= int(day_str) <31):
                print("Day must be a number bewtween 1 and 31")
                continue
            month = months.index(month_name) + 1 #converts to correct month number 
            day = int(day_str)                   #due to list position

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        
        else:
            print("Unrecognized format; use M/D/YYYY or MonthName D, YYYY.")
            continue

main()



            
            
                