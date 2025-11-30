def main():
    prompt = input("Give a Greeting: ")
    answer = money_h(prompt)
    print(answer)

def money_h(kramer):
    clean = kramer.strip().lower()
    if clean.startswith("hello"):
        return "$0.00"
    elif clean.startswith("h"):
        return "$20.00"
    else:
        return "$100.00"
    

main()

