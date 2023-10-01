# for i in range(3):
#     print("Meow")


# while True:
#     n = int(input("Enter number: "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("Meow")


# Using Function

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("Meow")


main()
