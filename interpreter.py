def main():
    express = input("Expression: ")
    answer = number(express)
    print(f"{answer:.1f}")

def number(core):
    x, y, z = core.split(" ")
    x = int(x)
    z = int(z)
    
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    else:
        return "not found"
    

main()
