def main():
    result = gas_tank()
    print (result)


def gas_tank():
    while True:
            try:
                fuel = input("Fraction: ")
                x_str,y_str = fuel.split("/")
                x = int(x_str)
                y = int(y_str)
                if x < 0 or y <= 0 or x > y:
                    continue

                percent = round((x/y) * 100)

            except (ValueError, ZeroDivisionError):
                 continue
             
            if percent >= 99:
               return "F"
            if percent <= 1:
               return "E"
            else:
                return f"{percent}%"  
        
main()