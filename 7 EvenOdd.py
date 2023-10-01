# number = int(input("Enter a number : "))

# if number % 2 == 0:
#     print(f"{number} is Even")
# else:
#     print(f"{number} is Odd")


# Check Even Odd number Using Function

def main():
    number = int(input("Enter a number : "))
    result = is_even(number)
    print(f"{number} is {result}")


def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


main()
