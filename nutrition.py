def main():
    fruit = input("Fruit: ")

    for item in facts:
        if item["Name"].lower() == fruit.lower():
            print("Calories: " , item["Cals"])
            break
    else:
        pass 

facts = [
    {"Name": "Apple", "Cals": "130"},
    {"Name": "Avocado", "Cals": "50"},
    {"Name": "Banana", "Cals": "110"},
    {"Name": "Cantaloupe", "Cals": "50"},
    {"Name": "Grapefruit", "Cals": "60"},
    {"Name": "Grapes", "Cals": "90"},
    {"Name": "Honeydew Melon", "Cals": "50"},
    {"Name": "Kiwifruit", "Cals": "90"},
    {"Name": "Lemon", "Cals": "15"},
    {"Name": "Lime", "Cals": "20"},
    {"Name": "Nectarine", "Cals": "60"},
    {"Name": "Orange", "Cals": "80"},
    {"Name": "Peach", "Cals": "60"},
    {"Name": "Pear", "Cals": "100"},
    {"Name": "Pineapple", "Cals": "50"},
    {"Name": "Plums", "Cals": "70"},
    {"Name": "Strawberries", "Cals": "50"},
    {"Name": "Sweet Cherries", "Cals": "100"},
    {"Name": "Tangerine", "Cals": "50"},
    {"Name": "Watermelon", "Cals": "80"},
]


main()


