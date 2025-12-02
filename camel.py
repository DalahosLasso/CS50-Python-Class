def main():
    camel_case = input("camelCase: ")
    answer = snake_convert(camel_case)
    print(answer)


def snake_convert(word):
    snake = ""

    for char in word:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char.lower()
    return snake 

main()