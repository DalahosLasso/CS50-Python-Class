def main():
    clock = input("What time is it? Enter in Military Time with colon: ")
    answer = convert(clock)
    if 7 <= answer <= 11:
        print("Breakfast Time!")
    elif 12 <= answer <= 16:
        print("Lunch Time!")
    elif 17 <= answer <= 19:
        print("Dinner Time!")
    else:
        print("Drink some water") 




def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    hours_as_floats = hours + minutes / 60
    return hours_as_floats


main()