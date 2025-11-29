def main():
    while True:
        computer_ask = input("What is the Answer to the Meaning of Life, the Universe, and Everything?: ")
        answer = deep_thought(computer_ask)
        print(answer)
        if answer == "YES":
            break

def deep_thought(core):

    if core in ("42", "forty-two", "forty two"):
        return "YES"
    else:
        return "NO"

main()
